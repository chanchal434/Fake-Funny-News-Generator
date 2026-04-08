📰 Fake News Generator

An AI-powered Fake News Generator built with Python & Streamlit that creates humorous, creative, and entertaining fake news articles.
Users can either generate news automatically using AI APIs or customize inputs like place, person, and news type.


🚀 Features
🤖 AI-Based News Generation (API integration)
✍️ Custom Input Mode (user-defined details)
🎭 Multiple News Categories (Politics, Sports, Entertainment, etc.)
😂 Funny & Satirical Output
🔄 Regenerate news instantly
📥 Download news as text
🎨 Clean and user-friendly Streamlit UI
⚡ Fast and lightweight

🛠️ Tech Stack
Python
Streamlit (UI)
OpenAI API / Requests (Text generation)
Faker / Random (Optional dummy data)

📂 Project Structure
Fake-News-Generator/
│
├── main.py            # Streamlit app
├── utils.py           # Helper functions
├── api_handler.py     # API integration and processing data
├── requirements.txt   # Dependencies and libraries
└── README.md          # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/fake-news-generator.git
cd fake-news-generator


2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Mac/Linux


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Add API Key

Create a .env file and add your API key:

OPENAI_API_KEY=your_api_key_here


▶️ Run the Application
streamlit run main.py

Then open your browser at:
👉 http://localhost:8501

🧠 How It Works
User selects mode:
Auto Generate → AI creates random funny news
Custom Input → User enters details
Inputs include:
Place 📍
Person 👤
News Type 🗞️
Tone 😄
App generates:
📰 Headline
📄 News Content

📸 Example Output

Headline:

"Aliens Appoint Pune Man as Earth's New Manager"

Content:

In a shocking turn of events, aliens landed in Pune and selected a local resident to manage Earth’s operations...

🔮 Future Improvements
🌙 Dark Mode
📜 Save News History
📤 Share to Social Media
🌍 Multi-language Support
🎙️ Voice News Generation

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.

🙌 Acknowledgements
Streamlit
GEMINI API
Python Community

💡 Author

Your Name

GitHub: https://github.com/chanchal434

⭐ If you like this project, don’t forget to star the repository!
