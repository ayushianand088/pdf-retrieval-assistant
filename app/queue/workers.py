from ..db.collections.files import files_collection
from bson import ObjectId
from pdf2image import convert_from_path
import os
import base64
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDPQdwob0KKYMEIe4jEcqSJUu3KIRRfrrU",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def encode_image(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    return base64.b64encode(image_bytes).decode("utf-8")

async def process_file(id: str, file_path: str):
    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "processing"
        }
    })
    
    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "Converting pdf to image"
        }
    })
    
    # convert pdf(unstructured data) to image  
    pages = convert_from_path(file_path)
    images = []
    
    for i, page in enumerate(pages):
        image_save_path = f"/mnt/uploads/images/{id}/image-{i}.jpg"
        os.makedirs(os.path.dirname(image_save_path), exist_ok=True)
        page.save(image_save_path, 'JPEG')
        images.append(image_save_path)
        
    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "pdf to image converted successfully"
        }
    })
    
    images_base64 = [encode_image(img) for img in images]
    
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Based on the resume, Roast this resume"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{images_base64[0]}"}}
                ]
            }
        ]
    )
    
    await files_collection.update_one({"_id": ObjectId}, {
        "$set": {
            "status": "processed",
        }
    })
    
    print(response.choices[0].message.content)
