import os
import json
import re
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-turbo")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable is required. See .env.example")

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change_me")

# ---------- Prompt Engineering ----------
BASE_PROMPT = """
You are an expert travel planner and travel-copywriter. Produce a clear, practical, and enjoyable travel itinerary.
Requirements:
- Output MUST be valid JSON and parseable. No commentary outside the JSON.
- Use the exact JSON schema specified below.
- Keep day activities realistic and feasible for the time of day.
- Include short local tips for safety, transport, and best experience.
- Provide budget estimates in the specified currency or local currency if none provided.

JSON schema:
{{
  "destination": "<string>",
  "duration_days": <integer>,
  "dates": {{ "start": "<YYYY-MM-DD or empty>", "end": "<YYYY-MM-DD or empty>" }},
  "budget": {{ "level": "<Low|Medium|High>", "estimate": "<approx amount and currency>" }},
  "interests": ["<string>", ...],
  "itinerary": [
    {{
      "day": <1-based integer>,
      "title": "<short title>",
      "morning": "<activity>",
      "afternoon": "<activity>",
      "evening": "<activity>",
      "estimated_cost": "<approx>",
      "local_tips": "<short tips>"
    }}, ...
  ],
  "packing_list": ["<item>", ...],
  "travel_tips": "<short overall tips>"
}}

User details (fill in values):
Destination: {destination}
Days: {days}
Dates: {dates}
Budget: {budget}
Preferred Currency: {currency}
Interests: {interests}
"""

# Regex to extract JSON safely
JSON_RE = re.compile(r"(\{.*\}|\[.*\])", re.S)

def extract_json_from_text(text: str):
    """Extracts the first valid JSON object or array from a string."""
    match = JSON_RE.search(text)
    if not match:
        return None
    raw = match.group(0)
    raw = re.sub(r",\s*}", "}", raw)
    raw = re.sub(r",\s*]", "]", raw)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        for start in range(len(raw)):
            if raw[start] != "{":
                continue
            for end in range(len(raw) - 1, start, -1):
                if raw[end] != "}":
                    continue
                chunk = raw[start:end + 1]
                try:
                    return json.loads(chunk)
                except Exception:
                    continue
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        destination = request.form.get("destination", "").strip()
        days = int(request.form.get("days", "3"))
        start_date = request.form.get("start_date", "").strip()
        end_date = request.form.get("end_date", "").strip()
        budget = request.form.get("budget", "Medium")
        currency = request.form.get("currency", "").strip() or "local currency"
        interests = request.form.get("interests", "").strip() or "general"

        if not destination:
            flash("Please provide a destination.", "error")
            return redirect(url_for("index"))

        # Fill the prompt
        filled_prompt = BASE_PROMPT.format(
            destination=destination,
            days=days,
            dates=json.dumps({"start": start_date, "end": end_date}),
            budget=budget,
            currency=currency,
            interests=interests
        )

        system_message = {
            "role": "system",
            "content": "You are a helpful, concise travel itinerary generator that only outputs JSON according to a strict schema."
        }
        user_message = {"role": "user", "content": filled_prompt}

        try:
            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=[system_message, user_message],
                temperature=0.35,
                max_tokens=1000
            )
            llm_text = response.choices[0].message["content"]
        except Exception as e:
            app.logger.exception("LLM API call failed.")
            flash(f"Failed to generate itinerary: {e}", "error")
            return redirect(url_for("index"))

        parsed = extract_json_from_text(llm_text)
        if parsed is None:
            flash("The AI returned an invalid JSON. Trying a safer fallback...", "warning")
            try:
                safe_response = openai.ChatCompletion.create(
                    model=OPENAI_MODEL,
                    messages=[
                        system_message,
                        {"role": "user", "content": filled_prompt + "\nIf unsure, return empty JSON with all schema keys."}
                    ],
                    temperature=0.2,
                    max_tokens=800
                )
                llm_text = safe_response.choices[0].message["content"]
                parsed = extract_json_from_text(llm_text)
            except Exception as e:
                flash(f"Retry failed: {e}", "error")
                return redirect(url_for("index"))

        if parsed is None:
            flash("Failed to parse itinerary output. Please try again.", "error")
            return redirect(url_for("index"))

        return render_template("result.html", itinerary=parsed, raw_text=llm_text)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
