# 🖼️ Image Detection Web App

This project is a **Flask-based Machine Learning web application** that detects whether a given image is present in an uploaded image database.

Users can upload:
- A **database (ZIP)** file containing multiple images  
- A **single image** to test  

The system compares the uploaded image with all images in the database using **OpenCV** and displays whether a match is found.

---

## 🚀 Features
- Upload both an image database and a test image  
- Detect if the uploaded image exists in the database  
- Built using Flask and OpenCV  
- Responsive, simple, and colorful web UI  

---

## 🧠 Tech Stack
- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **Libraries:** OpenCV, NumPy  

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/M-Nivetha7/Image_detection.git
2. Navigate to the Project Directory
bash
Copy code
cd Image_detection
3. Create and Activate Virtual Environment (Optional but Recommended)
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
4. Install Dependencies
bash
Copy code
pip install -r requirements.txt
5. Run the Flask App
bash
Copy code
python3 app.py
6. Open in Browser
Go to:

cpp
Copy code
http://127.0.0.1:5001/
📸 Preview
Upload a database ZIP file and a test image.
The app checks if the image is present in the database and displays the result.

🧾 Example Folder Structure
cpp
Copy code
Image_detection/
│
├── app.py
├── static/
│   ├── style.css
│
├── templates/
│   ├── index.html
│
├── requirements.txt
└── README.md
🧩 Requirements File
```
👩‍💻 Developed By
M. Nivetha
B.Tech Artificial Intelligence and Machine Learning
R.M.D. Engineering College

⭐ Don’t forget to star the repo if you find it useful!
