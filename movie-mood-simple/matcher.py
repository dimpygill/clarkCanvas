import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

# ── The Python dictionary ──────────────────────────────────────────────────
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


def extract_mood(user_input):
    keys = ", ".join(MOVIES.keys())

    prompt = f"""The user says: "{user_input}"

Map their mood to exactly one of these dictionary keys: {keys}

Respond with JSON only, no explanation:
{{"mood": "<one of the keys above, or null if none fit>", "blurb": "<one sentence recommending the matched movie>"}}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )

    data = json.loads(message.content[0].text.strip())
    return data.get("mood"), data.get("blurb", "")


def main():
    print("\n🎬  Movie Mood Matcher")
    print("─" * 30)

    user_input = input("\nHow are you feeling? ")

    if not user_input.strip():
        print("Please describe how you're feeling.")
        return

    print("\nThinking...\n")

    mood, blurb = extract_mood(user_input)
    movie = MOVIES.get(mood)

    if movie is None:
        print(f"Mood detected : {mood}")
        print("Sorry, that mood isn't in the dictionary yet.")
        print(f"Try adding:  \"{mood}\": {{\"title\": \"...\", \"genre\": \"...\", \"year\": \"...\"}}")
    else:
        print(f"🎯 Mood detected : {mood}")
        print(f"🎥 Movie         : {movie['title']}")
        print(f"🎭 Genre         : {movie['genre']}")
        print(f"📅 Year          : {movie['year']}")
        print(f"💬 Why           : {blurb}")

    print()


if __name__ == "__main__":
    main()
