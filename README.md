
# RAG System for Tools in Data Science (IIT Madras)

This project is a Retrieval-Augmented Generation (RAG) system that answers student questions using Discourse forum posts and course content from the 'Tools in Data Science' course.

## Components
- `preprocess.py`: Converts Discourse and Markdown data into chunks and generates embeddings.
- `app.py`: A FastAPI app to serve a /query endpoint.
- `downloaded_threads/`: Discourse post JSON files.
- `markdown_files/`: Course material in markdown.
- `knowledge_base.db`: SQLite database created by preprocessing.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Set your `.env`:
```
API_KEY=your_api_key_here
```

3. Preprocess the data:
```
python preprocess.py
```

If you're using a virtual environment (venv), activate it first:
# For Windows
```
.\venv\Scripts\activate
```
Then install Uvicorn:

bash
```
pip install uvicorn
```
```
pip install numpy
```
```
uvicorn app:app --reload
```
```
```
npm install -g promptfoo
```
```
promptfoo --version
```
```
node -v
```
promptfoo eval -c promptfooconfig.yaml --env-file .env
```


## Deployment

Deployable on platforms like Vercel (serverless) or better: Railway, Render, or Fly.io for persistent DB support.

---
    