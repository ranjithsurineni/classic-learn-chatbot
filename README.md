# 📚 Classic Learn Chatbot

🚀 A **Flask + Streamlit-powered chatbot** designed for answering FAQs related to **Classic Learn's courses** and services. The chatbot uses **TF-IDF vectorization** to find the most relevant answer based on predefined **JSON-based Q&A data**.

---

## 🌟 Features
✅ Answer common questions about **Classic Learn courses**  
✅ **Fallback mechanism** for unmatched queries  
✅ **Streamlit UI** for an interactive experience  
✅ **Publicly accessible** with free hosting options  

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ranjithsuineni/classic-learn-chatbot.git
cd classic-learn-chatbot
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Chatbot Locally**
#### **🔹 Using Flask API**
```bash
python backend/app.py
```
#### **🔹 Using Streamlit App**
```bash
streamlit run backend/app_streamlite.py
```

---

## 🚀 Usage Instructions
1. **Enter a question** in the input box.  
2. Click **Enter** or **Ask** to get an answer.  
3. The chatbot finds the **most relevant response**.  
4. If no exact match is found, it suggests a **closely related answer**.  

📌 *Try asking about courses, schedules, or general queries about Classic Learn!*

---

## 🎨 Customization
- **Modify `data01.json`** to update FAQs.  
- Change UI styles in `app_streamlite.py` using **Streamlit + CSS**.  

---

## 🌍 Deploying on Streamlit Cloud
### **1️⃣ Upload to GitHub**
Ensure your repository is updated and public.

### **2️⃣ Deploy on Streamlit Sharing**
1. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Connect your GitHub repository.
3. Select `backend/app_streamlite.py` as the main file.
4. Deploy and get a **public link**.

![image](https://github.com/user-attachments/assets/69aea437-3797-4f90-b0fd-c31627e20a3e)

![image](https://github.com/user-attachments/assets/a262cd17-a9d2-4bf8-9582-f9d56ad1cbca)

---

# 🌐 Classic Learn Chatbot - Flask Web App Frontend

This is the **frontend web application** built with **Flask**, designed to host and serve the Classic Learn Chatbot. The chatbot utilizes a **TF-IDF-based question-answering system** to respond to user queries related to Classic Learn's courses and services.

---

## 📦 Project Structure
```bash
frontend/ 
│ 
├── static/ # Static assets (CSS, JS, images) 
│     ├── style.css 
│  
├── templates/ # HTML templates (Jinja2) 
│     ├── index.html # Main chatbot UI
│ 
├── chatbot_pipeline.py # Imports and runs the Q&A logic
│ 
└── data01.json
│ 
└── DockerFile 
└── docker-compoose.yml
│ 
└── requirements.txt 
```

---

## 🚀 Features

✅ Web-based chatbot interface  
✅ Embeds the Classic Learn chatbot pipeline  
✅ Custom HTML/CSS for interactive UI  
✅ Handles user input and returns chatbot responses  
✅ Modular and extendable design  

---

## ⚙️ Installation & Setup

> Make sure to set up the backend before running the frontend.

###  Clone the Repository

```bash
git clone https://github.com/ranjithsuineni/classic-learn-chatbot.git
cd classic-learn-chatbot/frontend
```

 Install Dependencies
```bash
pip install -r ../requirements.txt
```


 Run the Flask Web App

```bash
python app.py
```

Once running, open your browser and go to:

```cpp
http://127.0.0.1:5000
```
---

![image](https://github.com/user-attachments/assets/516809a8-0ceb-4606-aab9-be9174c5f59c)

![image](https://github.com/user-attachments/assets/02449426-bf90-469c-aa97-4e034fc97eaf)

---
# 🧠 How It Works
The Flask frontend (app.py) receives user input via a simple form.

It sends the input to the chatbot_pipeline.py, which internally uses the TF-IDF vectorizer and JSON-based Q&A from the backend.

The chatbot pipeline returns the best-matched response or a fallback message.

The UI renders this response dynamically on the same page.

--
### 🖌 Customization
🧠 Update Q&A Data
Modify ../backend/data01.json to change the chatbot's knowledge base.

### 🎨 Change UI Styles
Edit static/style.css and templates/index.html to redesign the user interface.


---

## 🤝 Contributing
Pull requests are welcome! If you have suggestions, feel free to open an issue.

---

## 📜 License
This project is open-source under the **MIT License**.

