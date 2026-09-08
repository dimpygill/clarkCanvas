from flask import Flask, render_template, request
from dotenv import load_dotenv
from matcher import extract_mood, get_movie, MOVIES

load_dotenv()   # reads ANTHROPIC_API_KEY from .env

app = Flask(__name__)
app.secret_key = "dev-secret"


@app.route("/", methods=["GET", "POST"])
def index():
    result         = None
    not_found_mood = None
    mood_input     = None
    error          = None

    if request.method == "POST":
        mood_input = request.form.get("mood_input", "").strip()

        if not mood_input:
            error = "Describe how you're feeling first."
        else:
            try:
                mood, blurb = extract_mood(mood_input)
                result = get_movie(mood, blurb)
                if result is None:
                    not_found_mood = mood or "unknown"
            except Exception as e:
                error = f"Something went wrong: {e}"

    return render_template(
        "index.html",
        result=result,
        not_found_mood=not_found_mood,
        mood_input=mood_input,
        error=error,
        movies=MOVIES,           # pass dict to template for the viewer
    )


if __name__ == "__main__":
    app.run(debug=True)
