# 🚀 Reddit Insights Summarizer: An LLM-Powered Tool for Extracting and Summarizing Key Insights from comments for any Reddit search query on any Subreddit (For Free, uses all free APIs)

---

## 🌟 Project Overview
This project uses the power of **Large Language Models (LLMs)** to analyze and summarize Reddit comments for any search query on any subreddit. With the ability to extract the most insightful, popular, and frequently mentioned points, this tool helps you gain actionable insights from Reddit discussions with ease.

### **How It Works**:
1. **Reddit Data Fetching**:
   - The tool connects to the Reddit API to search for posts and comments based on your `KEYWORDS` and `SUBREDDIT`.
   - Example: Searching for `python freelancing` in the `all` subreddit.

2. **Text Summarization**:
   - Comments are passed to **Google Gemini** (gemini-2.0-flash-exp currently, chosen because it supports Input token limit 1,048,576 and combining 1000s of Reddit comments can get long), which generates a concise summary of the top insights from the extracted data.

3. **Output**:
   - The result is a well-organized summary of the top 10 key points extracted from the Reddit comments.

---

## 🔧 Setting Things Up

### 1. Preferred Python Version
- This project works best with **Python 3.9 or newer**.

---

### 2. Setting Up Reddit API Credentials

To access Reddit data, you'll need API credentials. Follow these steps:

1. **Go to Reddit Apps**: [Create a new app](https://old.reddit.com/prefs/apps/).
2. **Create an Application**:
   - Scroll to the bottom and click on **"Create App"** or **"Create Another App"**.
   - Select **"Script"** as the type.
   - Fill out the form:
     - **Name**: Your app name (e.g., `RedditSummarizer`).
     - **Redirect URI**: Use `http://localhost:8080` (default for script apps).
   - Click **"Create App"**.
3. **Update `keys.py`**:
   - Copy the `client_id`, `client_secret`, and `user_agent` from the app you created.
   - Update `keys.py` with these values:
     ```python
     REDDIT_CLIENT_ID = "your_client_id"
     REDDIT_CLIENT_SECRET = "your_client_secret"
     REDDIT_USER_AGENT = "your_user_agent"
     ```

---

### 3. Setting Up Google Gemini API Credentials
Google Gemini powers the LLM summarization in this project. To configure it:

1. **Go to Google AI Studio**: [Google AI Studio API Key](https://aistudio.google.com/app/apikey).
2. **Generate an API Key**:
   - Log in with your Google account.
   - Navigate to the API Keys section and create a new key by:
     1. Clicking `Create API key`.
     2. Selecting `Gemini API` from the dropdown.
     3. Clicking the `Create Key` button.
3. **Update `keys.py`**:
   - Add the generated key to `keys.py`:
     ```python
     GOOGLE_API_KEY = "your_gemini_api_key"
     ```

---

## 💻 Setting Up the Environment (Preferred)

### First-Time Setup
1. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```
2. Activate the environment:
   - **Linux/Mac**:
     ```bash
     source env/bin/activate
     ```
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```

### Installing Dependencies
Install all the required libraries:
```bash
pip3 install -r requirements.txt
```

### Running the Code
Run the tool:
```bash
python3 main.py
```

---

## 🎯 Example Usage

### Input:
- **Subreddit**: `all`
- **Keywords**: `python freelancing`

### Output:
**Top 10 Points from Reddit Comments on Python Freelancing**:
1. **Experience is Key**: Many commenters stress that real-world experience is more valuable than knowing just the syntax of Python.
2. **Portfolio Matters**: A strong portfolio showcasing real projects is essential for landing freelance gigs.
3. **Networking is Important**: Successful freelancers emphasize networking through meetups, online forums, and personal connections.
4. **Avoid Over-Reliance on Platforms**: Platforms like Upwork/Fiverr can be competitive, leading to low pay. Building your brand is recommended.
5. **Soft Skills are Crucial**: Communication, problem-solving, and client management are vital for freelancing success.
6. **Specialize and Build a Niche**: Focus on a specific Python domain (e.g., web dev, data science) to stand out.
7. **Focus on Real Projects**: Build projects solving real problems instead of relying solely on tutorials.
8. **Pricing is a Challenge**: Pricing services is tricky. Consider task complexity, experience, and living costs.
9. **ATS-Friendly Resumes**: Keep resumes simple for easy parsing by Applicant Tracking Systems.
10. **It’s a Long Journey**: Freelancing isn’t a quick-money scheme. It takes patience, learning, and persistence.

---

## 📂 Project Structure
```
reddit-insights-summarizer/
├── main.py             # Main entry point for the application
├── reddit_scraper.py   # Handles Reddit API data fetching
├── llm_text_analysis.py # Handles text summarization using LLM
├── keys.py             # Stores API credentials
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📌 Key Features
- **FREE APIs**: Uses all free APIs, Reddit API and Google Gemini API, both are free.
- **LLM-Powered Summarization**: Uses Google Gemini for concise, accurate summaries.
- **Customizable Search**: Works with any subreddit and search keywords.
- **Scalable**: Handles large datasets by chunking and summarizing incrementally.

---

## 🚨 Notes
1. Ensure your API keys for both Reddit and Google Gemini are set correctly in `keys.py`.
2. Stay within the API token limits for both services to avoid rate-limiting issues.

---

## 🌟 Contributions
Feel free to fork, improve, and submit pull requests! For issues or feature requests, create an issue on the [GitHub repository](#).

---

## 📜 License
This project is licensed under the **MIT License**.
