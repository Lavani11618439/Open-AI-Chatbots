# Azure OpenAI Chatbot 🤖

This is a **Streamlit-based chatbot** powered by **Azure OpenAI**. It features a secure login system and interactive chat functionality.

## 🚀 Features
- **Azure OpenAI GPT integration**
- **User authentication (username & password)**
- **Session-based chat history**
- **Secure API key storage with `.env`**
- **Streamlit-powered UI**

## 🛠️ Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
Create a `.env` file in the project root and add:
```ini
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
AZURE_OPENAI_DEPLOYMENT=your_model_deployment
AZURE_OPENAI_API_VERSION=your_api_version
BOT_USERNAME=your_username
BOT_PASSWORD=your_password
```

### 5️⃣ **Run the Chatbot**
```sh
streamlit run app.py
```

## 📌 Usage
1. Open **http://localhost:8501/** in your browser.
2. Log in with the credentials from your `.env` file.
3. Start chatting with the Azure OpenAI chatbot! 🎉

## 📸 Screenshots
![Chatbot Screenshot](screenshot.png)

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact
For any inquiries, feel free to reach out via (lavani11618439@gmail.com).

