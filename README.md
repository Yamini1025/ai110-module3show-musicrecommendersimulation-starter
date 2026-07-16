# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My understanding of how real-world recommendations systems work is that they use user behavior signals like what you played, liked, skipped, etc., item characteristics such as genre, tempo, mood, energy, etc., and ranking models, which score many candidate songs and present the best ones first. My version will prioritize genre as the main feature, along with mood and energy, and give a smaller preference to acousticness as well, if the user likes or dislikes acoustic songs. Each Song uses : genre, mood, energy, tempo_bpm, valence, acousticness, and artist and title for identification. The UserProfile stores a favorite genre, a favorite mood, a target energy level, and a preference for whether the user likes acoustic songs. The Recommender computes a score for each song by comparing the song's features to the user's preferences. For example, it gives a strong reward if the song matches the user's preferred genre. It gives a smaller reward if the song matches the preferred mood. 

This music recommender uses a content-based filtering approach. Instead of learning from other users, it recommends songs by comparing a user's preferences with the features of each song. Real-world recommendation systems use information such as listening history, likes, skips, playlists, and song characteristics. This simplified version focuses on matching song attributes such as genre, mood, and energy level to the user's taste profile.

Each song is represented using features from the songs dataset, including:
- Genre
- Mood
- Energy level

Each user profile contains:
- Favorite genre
- Favorite mood
- Target energy level

Algorithm Recipe :
The recommender calculates a score for every song based on how well it matches the user's preferences.

Scoring rules:
- Genre match: +5 points
- Mood match: +3 points
- Energy similarity: up to +2 points

For numerical features like energy, the system calculates similarity by measuring how close the song's energy is to the user's target energy:

'energy_similarity = 1 - abs(song_energy - user_energy)'

After scoring each song, the system ranks all songs from highest score to lowest score and returns the top recommendations.

Potential Biases and Limitations :

This recommender may over-prioritize certain features, such as genre, and miss songs that match a user's mood or energy but belong to a different genre. The quality of recommendations is also limited by the features available in the dataset and may not fully represent a user's complete musical preferences.

---

## Sample Recommendation Output 
Recommendations for: genre=pop, mood=happy, energy=0.8
==================================================

1. Sunrise City — Neon Echo
   Score:  9.96
   Reasons: genre match (+5), mood match (+3), energy similarity (+2.0)

2. Gym Hero — Max Pulse
   Score:  6.74
   Reasons: genre match (+5), energy similarity (+1.7)

3. Rooftop Lights — Indigo Parade
   Score:  4.92
   Reasons: mood match (+3), energy similarity (+1.9)

4. Golden Hour Drive — Marina Vale
   Score:  1.92
   Reasons: energy similarity (+1.9)

5. Night Drive Loop — Neon Echo
   Score:  1.90
   Reasons: energy similarity (+1.9)

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



