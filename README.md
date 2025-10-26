# 📝 Bucketlist App (Streamlit)

## 📘 Overview
The **Bucketlist App** is a simple and interactive web-based **Todo application** built using [Streamlit](https://streamlit.io/).  
It allows users to **add**, **view**, and **manage** their bucket list items in a clean interface, while storing data in a local text file for simplicity.

This project demonstrates **Streamlit app structure**, **modular Python design**, and **file-based data persistence** — making it a great starting point for beginners learning how to build full-stack Python apps.

---

## 🗂️ Project Structure

| Folder / File | Description |
|----------------|-------------|
| **__pycache__/** | Stores Python's compiled bytecode files. |
| **venv/** | (Optional) Virtual environment for dependency management. |
| **functions.py** | Handles reading and writing of todos from the text file. |
| **requirements.txt** | Lists the dependencies required for running the app. |
| **todos.txt** | Simple text file where all bucket list items are stored. |
| **web.py** | Main Streamlit web app script that runs the UI and logic. |

---

## ⚙️ Features

- ✅ **Add and manage bucket list items** dynamically via Streamlit.  
- 🧠 **Uses separate logic module (`functions.py`)** for clean code structure.  
- 💾 **File-based storage (`todos.txt`)** — lightweight and simple.  
- 🌐 **Built with Streamlit** for an easy-to-use and responsive UI.  
- 🧩 **Easily scalable** — can be extended to use databases later.  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/jasmininnaka24/bucketlist-app-streamlit.git
cd bucketlist-app-streamlit
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run web.py
```

---

## 🧠 How It Works

- When the app starts, it reads all items from `todos.txt`.
- Users can add new items, which are then written back to the same file.
- Streamlit's session state dynamically updates the list in real time.
- All core logic for reading/writing is handled by `functions.py`.
