# 📝 Bucketlist App (Streamlit)

A simple yet functional **Bucketlist (Todo) App** built with [Streamlit](https://streamlit.io/).  
This project demonstrates how to create a user-friendly web interface for managing a bucket list, while using **plain text file storage** for simplicity and scalability.

---

## 🚀 Features

- ✅ Add, view, and manage your bucket list items  
- 🧠 Uses a separate `functions.py` file for logic and file handling  
- 📂 Stores data in a simple `todos.txt` file  
- 🌐 Built using **Streamlit** for a clean and interactive UI  
- 🧩 Designed for easy extension and scaling  

---

## 🗂️ Project Structure

bucketlist-app-streamlit/
├── pycache/ # Compiled Python files
├── venv/ # Virtual environment (optional to include)
├── functions.py # Handles reading/writing todos
├── requirements.txt # Dependencies for the project
├── todos.txt # File storing all bucket list items
├── web.py # Main Streamlit web application

yaml
Copy code

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/jasmininnaka24/bucketlist-app-streamlit.git
cd bucketlist-app-streamlit
2. Create a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Streamlit app
bash
Copy code
streamlit run web.py
🧠 How It Works
The app reads and writes todos from todos.txt.

All file-handling and helper logic is abstracted into functions.py.

Streamlit dynamically updates the UI whenever you add or modify items.

