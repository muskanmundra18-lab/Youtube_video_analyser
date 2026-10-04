# AI YouTube Video Analyser

An agentic AI application that accepts a YouTube URL and analyzes the video's available content using an LLM-powered agent. The application is built with **Agno**, **Groq**, **YouTubeTools**, **SQLite**, and **Streamlit**.

## Features

- Accepts a YouTube video URL through a Streamlit interface
- Uses an Agno agent to orchestrate video analysis
- Retrieves YouTube video information through `YouTubeTools`
- Uses Groq's `openai/gpt-oss-120b` model for analysis
- Produces structured analysis, summaries, key information, and answers to questions based on available video content
- Uses SQLite for agent/database persistence

## Architecture

```text
YouTube URL
    ↓
Streamlit UI
    ↓
Agno Agent
    ↓
YouTubeTools
    ↓
Video / transcript / metadata
    ↓
Groq LLM
    ↓
Structured analysis
```

## Tech Stack

- Python
- Agno
- Groq
- `openai/gpt-oss-120b`
- Streamlit
- SQLite
- python-dotenv

## Project Structure

```text
Youtube_video_analyser/
├── ui.py
├── videoanalyser.py
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/muskanmundra18-lab/Youtube_video_analyser.git
cd Youtube_video_analyser
```

### 2. Install dependencies

Install the packages used by the project:

```bash
pip install agno groq streamlit python-dotenv
```

### 3. Configure the API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit API keys to GitHub.

### 4. Run the application

```bash
streamlit run ui.py
```

Open the local Streamlit URL, paste a YouTube URL, and start the analysis.

## Design Goal

The project explores how an **agentic workflow** can combine external tools with an LLM to turn a raw YouTube URL into useful, structured information rather than requiring the user to manually watch the entire video.

## Future Improvements

- Add conversation history in the UI
- Add timestamps and citations to extracted information
- Support follow-up questions about the same video
- Add transcript download/export
- Add caching for repeated video analysis
- Add evaluation for factual consistency and hallucination rate

## Author

**Muskan Mundra**

[GitHub](https://github.com/muskanmundra18-lab)
