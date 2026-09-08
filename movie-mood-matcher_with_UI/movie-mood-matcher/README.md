# Movie Mood Matcher

A beginner Python project that teaches how dictionaries work by building an AI-powered movie recommender. You type how you're feeling, Claude extracts your mood, and Python looks it up in a dictionary to find your film.

---

## What's in this project

```
movie-mood-matcher/
├── app.py                  ← Flask web server (routes only)
├── matcher.py              ← Python dictionary + Claude API logic
├── requirements.txt        ← Python packages to install
├── .env.example            ← Template for your API key
├── .gitignore
└── templates/
    └── index.html          ← The UI (rendered by Flask)
```

---

## Prerequisites

Make sure you have these installed before starting:

- **Python 3.11 or higher** — check with `python --version`
- **pip** — comes with Python
- **An Anthropic API key** — get one at https://console.anthropic.com

---

## Setup steps

### Step 1 — Download the project

Put the entire `movie-mood-matcher/` folder somewhere on your computer, for example your Desktop.

### Step 2 — Open a terminal in the project folder

**Mac / Linux:**
```bash
cd ~/Desktop/movie-mood-matcher
```

**Windows (Command Prompt):**
```cmd
cd C:\Users\YourName\Desktop\movie-mood-matcher
```

### Step 3 — Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your Python installation.

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

You'll know it worked when you see `(venv)` at the start of your terminal prompt.

### Step 4 — Install the required packages

```bash
pip install -r requirements.txt
```

This installs Flask, the Anthropic SDK, and python-dotenv.

### Step 5 — Add your API key

Copy the example file and rename it:

**Mac / Linux:**
```bash
cp .env.example .env
```

**Windows:**
```cmd
copy .env.example .env
```

Now open `.env` in any text editor and replace `your_api_key_here` with your actual key:

```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

Save the file. Do not share this file or commit it to Git — it's already in `.gitignore`.

### Step 6 — Run the app

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 7 — Open the app in your browser

Go to: **http://127.0.0.1:5000**

That's it. The app is running.

---

## How it works

1. You type how you're feeling (e.g. "I feel kind of gloomy today")
2. Flask sends that text to `matcher.py`
3. `matcher.py` calls the Claude API and asks it to map your words to one of the dictionary keys
4. Claude returns a JSON object with the mood key and a recommendation blurb
5. Python does `MOVIES.get(mood)` — a dictionary lookup
6. Flask passes the result to the HTML template, which renders it on screen

The dictionary in `matcher.py` is the core of the app:

```python
MOVIES = {
    "happy":    {"title": "The Grand Budapest Hotel", ...},
    "sad":      {"title": "Inside Out", ...},
    "scared":   {"title": "Get Out", ...},
    "romantic": {"title": "Crazy Rich Asians", ...},
    "bored":    {"title": "Inception", ...},
    "excited":  {"title": "Everything Everywhere All at Once", ...},
}
```

---

## Try extending it

Once the app runs, try these exercises to go deeper on dictionaries:

**Add a new mood:**
Open `matcher.py` and add a new key-value pair to `MOVIES`:
```python
"nostalgic": {"title": "Stand By Me", "genre": "Drama", "year": "1986"},
```

**List all moods:**
Add this to `matcher.py` and call it from `app.py`:
```python
def list_moods():
    return list(MOVIES.keys())
```

**Iterate over the dictionary:**
```python
for mood, movie in MOVIES.items():
    print(f"{mood} → {movie['title']}")
```

**Check if a key exists:**
```python
if "happy" in MOVIES:
    print("We have a movie for that mood")
```

---

## Stopping the app

Press `Ctrl + C` in the terminal to stop Flask.

To deactivate the virtual environment when you're done:
```bash
deactivate
```

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'flask'`**
You're not inside the virtual environment. Run `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows) and try again.

**`AuthenticationError` or `Invalid API key`**
Check that your `.env` file exists, is in the project root (same folder as `app.py`), and contains the correct key with no extra spaces.

**Port already in use**
Another app is using port 5000. Run Flask on a different port:
```bash
flask run --port 5001
```
Then open http://127.0.0.1:5001

**The page shows raw `{{ }}` template code**
You opened `index.html` directly in your browser. Always access the app through `http://127.0.0.1:5000` after running `python app.py`.
