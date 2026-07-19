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
This project implements a content-based music recommendation system that suggests songs based on a user's taste profile. The system compares user preferences, including favorite genre, mood, and target energy level, with song features from a music dataset. Each song receives a score based on how closely it matches the user's preferences, and the highest-scoring songs are returned as recommendations. The project explores how simple recommendation algorithms work, how feature weighting affects results, and how bias can appear in recommendation systems.

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My understanding of how real-world recommendations systems work is that they use user behavior signals like what you played, liked, skipped, etc., item characteristics such as genre, tempo, mood, energy, etc., and ranking models, which score many candidate songs and present the best ones first.The current implementation prioritizes genre, mood, and energy similarity. Although the dataset contains additional features like acousticness and danceability, they are not currently included in the scoring algorithm. Each Song uses : genre, mood, energy, tempo_bpm, valence, acousticness, and artist and title for identification. The UserProfile stores a favorite genre, favorite mood, and target energy level. The class structure also supports additional preferences like acoustic preference for future improvements. The Recommender computes a score for each song by comparing the song's features to the user's preferences. For example, it gives a strong reward if the song matches the user's preferred genre. It gives a smaller reward if the song matches the preferred mood. 

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

## Phase 4 Output
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

Energetic Rock Fan
Preferences: {'genre': 'rock', 'mood': 'energetic', 'energy': 0.9}
==================================================

1. Storm Runner — Voltline
   Score: 6.98
   Reasons: genre match (+5), energy similarity (+2.0)

2. Electric Harbor — Northline
   Score: 4.94
   Reasons: mood match (+3), energy similarity (+1.9)

3. Neon Boulevard — The Velvet Frames
   Score: 1.98
   Reasons: energy similarity (+2.0)

4. Gym Hero — Max Pulse
   Score: 1.94
   Reasons: energy similarity (+1.9)

5. Golden Hour Drive — Marina Vale
   Score: 1.88
   Reasons: energy similarity (+1.9)



Chill Jazz Listener
Preferences: {'genre': 'jazz', 'mood': 'relaxed', 'energy': 0.3}
==================================================

1. Coffee Shop Stories — Slow Stereo
   Score: 9.86
   Reasons: genre match (+5), mood match (+3), energy similarity (+1.9)

2. Spacewalk Thoughts — Orbit Bloom
   Score: 1.96
   Reasons: energy similarity (+2.0)

3. Library Rain — Paper Lanterns
   Score: 1.90
   Reasons: energy similarity (+1.9)

4. Quiet Cathedral — Aria Vale
   Score: 1.84
   Reasons: energy similarity (+1.8)

5. Focus Flow — LoRoom
   Score: 1.80
   Reasons: energy similarity (+1.8)



Classical Music Enthusiast
Preferences: {'genre': 'classical', 'mood': 'calm', 'energy': 0.2}
==================================================

1. Quiet Cathedral — Aria Vale
   Score: 6.96
   Reasons: genre match (+5), energy similarity (+2.0)

2. Spacewalk Thoughts — Orbit Bloom
   Score: 1.84
   Reasons: energy similarity (+1.8)

3. Library Rain — Paper Lanterns
   Score: 1.70
   Reasons: energy similarity (+1.7)

4. Coffee Shop Stories — Slow Stereo
   Score: 1.66
   Reasons: energy similarity (+1.7)

5. Focus Flow — LoRoom
   Score: 1.60
   Reasons: energy similarity (+1.6)



Hip-Hop Aficionado
Preferences: {'genre': 'hip-hop', 'mood': 'confident', 'energy': 0.7}
==================================================

1. Neon Boulevard — The Velvet Frames
   Score: 4.62
   Reasons: mood match (+3), energy similarity (+1.6)

2. Sunlit Echoes — Solstice Choir
   Score: 1.94
   Reasons: energy similarity (+1.9)

3. Golden Thread — Kaia Rivers
   Score: 1.94
   Reasons: energy similarity (+1.9)

4. Night Drive Loop — Neon Echo
   Score: 1.90
   Reasons: energy similarity (+1.9)

5. Rooftop Lights — Indigo Parade
   Score: 1.88
   Reasons: energy similarity (+1.9)



Electronic Dance Partygoer
Preferences: {'genre': 'electronic', 'mood': 'upbeat', 'energy': 0.8}
==================================================

1. Sunrise City — Neon Echo
   Score: 1.96
   Reasons: energy similarity (+2.0)

2. Golden Hour Drive — Marina Vale
   Score: 1.92
   Reasons: energy similarity (+1.9)

3. Rooftop Lights — Indigo Parade
   Score: 1.92
   Reasons: energy similarity (+1.9)

4. Night Drive Loop — Neon Echo
   Score: 1.90
   Reasons: energy similarity (+1.9)

5. Electric Harbor — Northline
   Score: 1.86
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

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---
I tested how changing the importance of different features affected recommendations. The original scoring system used:

- Genre match: +5 points
- Mood match: +3 points
- Energy similarity: up to +2 points

For the experiment, I reduced the genre weight to +2.5 points and increased energy similarity to provide up to +4 points.

The results showed that recommendations became more influenced by energy level rather than exact genre matches. For example, the Energetic Rock Fan profile originally prioritized "Storm Runner" because of the genre match, but after increasing the energy weight, "Electric Harbor" ranked higher because its energy and mood were closer to the user's preferences.

This experiment showed that changing scoring weights can significantly affect recommendation behavior. A system that prioritizes one feature too heavily may create less variety, while a system that balances multiple features may provide more diverse recommendations.

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

This recommender has several limitations:

- It only works with a small dataset of 20 songs, so it cannot represent the full range of musical preferences.
- It relies on manually assigned features such as genre, mood, and energy instead of learning directly from user behavior.
- Exact genre matching can create filter bubbles by favoring songs from the same category.
- Users with preferences that are not represented in the dataset may receive recommendations based mostly on energy similarity rather than their actual taste.
- Important musical characteristics such as lyrics, artist similarity, listening history, and personal context are not considered.

These limitations show why real-world recommendation systems require larger datasets and more complex models.

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommendation systems transform user preferences and item features into predictions. I learned that even a simple scoring algorithm can create recommendations that feel personalized when the right features and weights are chosen. However, I also learned that small design decisions, such as giving genre more importance than energy, can significantly change the recommendations a user receives.

AI tools helped me brainstorm scoring strategies, debug implementation issues, and analyze unexpected recommendation results. However, I needed to verify suggestions by running the program, testing different user profiles, and checking whether the outputs actually matched the intended behavior. This project showed me that recommendation systems are not only about writing code, but also about making careful decisions about data, features, and evaluation.

If I continued developing this project, I would add more songs, include additional features like tempo and danceability, and explore machine learning approaches that learn from user interactions such as likes, skips, and playlists.


