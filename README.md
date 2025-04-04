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

---

## 🤝 Contributing
Pull requests are welcome! If you have suggestions, feel free to open an issue.

---

## 📜 License
This project is open-source under the **MIT License**.

