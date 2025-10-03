# 📘 PDF Retrieval Assistant

A system that allows users to **upload PDFs** and get **AI-powered answers or descriptions** from the document content using **Gemini LLM**.  

Unlike traditional text-only RAG systems, this project works by **converting PDFs into images**, encoding them as **Base64**, and sending them to the LLM for interpretation.

---

## 🚀 Features

- 📤 Upload a PDF file  
- 🖼️ Convert PDF pages into images  
- 🔐 Encode images into Base64 format  
- 🤖 Send Base64 images to **Gemini API**  
- 💬 Receive AI-generated responses describing or summarizing the document  

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Task Queue:** Redis
- **Database:** MongoDB  
- **LLM API:** Google Gemini (via OpenAI-compatible client)  
- **PDF Processing:** pdf2image, Pillow  

---

## 📂 Project Flow

1. User uploads a **PDF**.  
2. System converts the PDF into **images**.  
3. Images are encoded into **Base64 strings**.  
4. Encoded images are sent to **Gemini LLM**.  
5. The **response is stored in MongoDB** and made available through API routes.  

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ayushianand088/pdf-retrieval-assistant.git
cd pdf-retrieval-assistant
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the server
```bash
uvicorn app.main:app --reload
```
---

## Screenshots

### 1. API Routes (Fetch by ID, Upload File)
<img width="1918" height="942" alt="route" src="https://github.com/user-attachments/assets/e2da135a-72e8-4b6f-a4f1-90bdbecfbc70" />


### 2. Upload File Interface
<img width="1918" height="1021" alt="upload_file" src="https://github.com/user-attachments/assets/97ef2c87-814a-44ef-9d0f-2ba89fe40283" />


### 3. Uploaded File Response (File ID)
<img width="1918" height="1013" alt="upload_response" src="https://github.com/user-attachments/assets/f2911ef0-d203-4e41-bea0-232778e1921e" />


### 4. Fetch by ID Interface
<img width="1918" height="838" alt="fetch_response" src="https://github.com/user-attachments/assets/6e6c9324-f14d-47a9-9264-e70e2401400f" />


### 5. Fetch by ID Result
<img width="1918" height="1020" alt="fetch_result" src="https://github.com/user-attachments/assets/390ce654-713f-4a96-bea0-ef291b12746b" />
