# Movie Mood Matcher (Simple Version)

No web server, no HTML. Just Python in the terminal.

## Project files

```
movie-mood-simple/
├── matcher.py        ← the dictionary + Claude API call
├── requirements.txt  ← two packages to install
├── .env              ← your API key (you create this)
└── .gitignore
```

## Setup

### Step 1 — Open a terminal in this folder

### Step 2 — Create and activate a virtual environment

Mac / Linux:
```
python3 -m venv venv
source venv/bin/activate
```

Windows:
```
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install packages

```
pip install -r requirements.txt
```

### Step 4 — Add your API key

Copy the example file:

Mac / Linux:  cp .env.example .env
Windows:      copy .env.example .env

Open .env and replace the placeholder with your real key:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

Get a key at: https://console.anthropic.com

### Step 5 — Run it

```
python matcher.py
```

## Example output

```
🎬  Movie Mood Matcher
──────────────────────────────

How are you feeling? I feel kind of gloomy today

Thinking...

🎯 Mood detected : sad
🎥 Movie         : Inside Out
🎭 Genre         : Animation · Drama
📅 Year          : 2015
💬 Why           : A deeply moving film for when life feels heavy.
```

## Try extending it

Add a new mood to the MOVIES dictionary in matcher.py:

```python
"nostalgic": {"title": "Stand By Me", "genre": "Drama", "year": "1986"},
```

The AI will automatically start recognising that mood — no other changes needed.
