import os
import json
import anthropic

# ── The Python dictionary ──────────────────────────────────────────────────
# This is the core data structure we're teaching.
# Each key is a mood string, each value is movie metadata.

MOVIES = {
    "happy":    {"title": "The Grand Budapest Hotel", "genre": "Comedy · Adventure", "year": "2014"},
    "sad":      {"title": "Inside Out",               "genre": "Animation · Drama",  "year": "2015"},
    "scared":   {"title": "Get Out",                  "genre": "Horror · Thriller",  "year": "2017"},
    "romantic": {"title": "Crazy Rich Asians",        "genre": "Romance · Comedy",   "year": "2018"},
    "bored":    {"title": "Inception",                "genre": "Sci-Fi · Thriller",  "year": "2010"},
    "excited":  {"title": "Everything Everywhere All at Once", "genre": "Action · Sci-Fi", "year": "2022"},
}

# ── Claude API client ──────────────────────────────────────────────────────
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def extract_mood(user_input: str) -> tuple[str | None, str]:
    """
    Send the user's free-text input to Claude.
    Claude returns the closest mood key from our dictionary,
    plus a one-sentence movie recommendation blurb.
    """
    keys = ", ".join(MOVIES.keys())

    prompt = f"""The user says: "{user_input}"

Your job is to map their mood to exactly one of these dictionary keys: {keys}

Respond with a JSON object only — no explanation, no markdown fences:
{{"mood": "<one of the keys above, or null if none fit>", "blurb": "<one sentence recommending the matched movie for this mood>"}}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    data = json.loads(raw)
    return data.get("mood"), data.get("blurb", "")


def get_movie(mood: str | None, blurb: str) -> dict | None:
    """
    Look up the mood in the dictionary using .get() with a None default.
    Returns the full movie record, or None if the mood isn't a key.
    """
    movie = MOVIES.get(mood)       # ← the dictionary lookup
    if movie is None:
        return None
    return {"mood": mood, "blurb": blurb, **movie}
