# AI Travel Planner (Flask + LLM)

## Quick start
1. Create virtualenv:
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\\Scripts\\activate

2. Install:
   pip install -r requirements.txt

3. Copy `.env.example` to `.env` and set OPENAI_API_KEY.

4. Run:
   export FLASK_APP=app.py
   flask run

   Or:
   python app.py

5. Open http://127.0.0.1:5000

## Architecture
- Frontend: Tailwind-powered Jinja2 templates
- Backend: Flask handling prompt composition and LLM calls
- Prompt engineering: strict schema + few-shot hints, JSON-only requirement
- Validation: extract JSON, fallback attempts, user-friendly messages

## Extensions
- Add Google Places / local events via web APIs (to ground recommendations)
- Add caching & user sessions; save itineraries per user (SQLite / Firebase)
- Export PDF (WeasyPrint / wkhtmltopdf)
- Add unit tests and CI

## Security & costs
- Keep OPENAI_API_KEY secret. Rate-limit requests and validate user input in production to avoid abuse.
- Monitor tokens and set reasonable `max_tokens` / `temperature`.
