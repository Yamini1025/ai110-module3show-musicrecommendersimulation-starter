# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

MusicFinder
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---
MusicFinder is a content-based music recommender that suggests songs based on a user's preferred genre, mood, and energy level. The system predicts which songs are most similar to a user's taste profile by comparing user preferences with song attributes.

### Intended Use:
- Demonstrating how content-based recommendation systems work.
- Suggesting songs based on simple user preferences.
- Exploring how different scoring rules affect recommendations.

### Non-Intended Use:
- This system should not be used as a real-world music recommendation platform.
- It should not be used to predict a person's complete musical taste because it only considers a limited number of features and does not learn from user behavior.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---
MusicFinder uses a weighted scoring approach. Each song receives points based on how well it matches the user's preferences:
- Genre match: +5 points
- Mood match: +3 points
- Energy similarity: up to +2 points

Songs with higher scores are ranked higher and returned as recommendations. The system prioritizes exact preference matches while using energy similarity to fine-tune rankings.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The recommender uses a dataset of 20 songs stored in `songs.csv`. Each song contains features such as title, artist, genre, mood, and energy level. The system uses these features to calculate recommendation scores.

The dataset is small and manually created, so it does not represent the full diversity of music preferences. Some genres and moods have fewer examples than others, which can affect recommendation quality.

## Experiment : 
For this experiment, I reduced the genre weight from +5 to +2.5 and increased the maximum energy similarity score from +2 to +4 while keeping the mood weight at +3.

The recommendations changed noticeably. Songs with energy levels closer to the user's preference moved higher in the rankings, even if they did not match the preferred genre. For example, for the "Energetic Rock Fan" profile, **Electric Harbor** moved ahead of **Storm Runner** because its mood and energy matched well enough to outweigh the reduced importance of genre. Overall, the recommendations became more influenced by energy similarity, producing more varied results but making genre a less dominant factor.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
MusicFinder works well when a user's preferences are represented in the dataset. Users with a matching genre and mood receive recommendations that align closely with their stated preferences. For example, the High-Energy Pop profile successfully recommended songs that matched pop genre, happy mood, and high energy.

The scoring system is also easy to understand and explain because each recommendation includes reasons for its score. Users can see whether a song was recommended because of genre, mood, or energy similarity.

Another strength is that the system can adapt to different user profiles. Changing the user's preferences produces noticeably different rankings, showing how recommendation algorithms use user information to personalize results.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

This recommender relies heavily on exact genre and mood matches, which can create filter bubbles where users are mostly recommended songs from the same category. Users whose preferred genre is not represented in the dataset may receive recommendations based mostly on energy similarity rather than their actual musical preferences. The small dataset also creates representation bias, meaning genres with more songs receive more personalized recommendations than genres with fewer examples. Additionally, the system only considers genre, mood, and energy, so other important musical features such as tempo, acousticness, and danceability are ignored.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.


I tested the recommender with several different user profiles:
- High-Energy Pop
- Energetic Rock Fan
- Chill Jazz Listener
- Classical Music Enthusiast
- Hip-Hop Aficionado
- Electronic Dance Partygoer

The recommendations changed based on each user's preferences. The High-Energy Pop profile recommended songs that matched both pop genre and happy mood, while the Energetic Rock Fan profile prioritized rock songs with high energy. The Chill Jazz Listener and Classical Music Enthusiast profiles received lower-energy recommendations because their target energy values were closer to calm songs in the dataset.

One surprising result was the Electronic Dance Partygoer profile. Since the dataset did not contain a strong electronic genre match, the recommender relied mostly on energy similarity and returned songs from other genres. This showed that the recommender performs best when the user's preferences are represented in the dataset.

The weight experiment also showed that changing the scoring rules affects recommendation behavior. Increasing the importance of energy caused songs with similar energy levels to rank higher, even when they did not match the user's preferred genre. Reducing the genre weight made recommendations more diverse but sometimes less aligned with the user's stated musical style.


- **High-Energy Pop vs Energetic Rock Fan:** Both profiles preferred high-energy songs, but the top recommendations differed because genre matching had the strongest influence on scoring.

- **Chill Jazz Listener vs Classical Music Enthusiast:** Both profiles favored lower-energy music, but jazz and classical genre preferences caused different songs to rank first.

- **Hip-Hop Aficionado vs Electronic Dance Partygoer:** Neither profile had a perfect genre match in the dataset, so recommendations relied more heavily on mood and energy similarity.

- **Original Weights vs Energy-Focused Experiment:** The original system prioritized genre, while the modified version allowed energy similarity to have a larger impact, creating more diverse but sometimes less genre-specific recommendations.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
If I continued developing this project, I would expand the dataset, add more meaningful music features, and explore machine learning approaches that learn from user interactions such as likes, skips, and playlists.


## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

## Biggest Learning Moment
My biggest learning moment was realizing that even a simple scoring system can create meaningful-looking recommendations. Small changes to feature weights can significantly change the ranking of songs, showing how important algorithm design decisions are.

## How AI Tools Helped
AI tools helped me brainstorm recommendation strategies, debug implementation issues, and explain why certain songs ranked higher. However, I still needed to verify the AI suggestions by running experiments and checking whether the results matched my expected behavior.

## What Surprised Me
I was surprised that a simple algorithm using only genre, mood, and energy could produce recommendations that felt personalized. Even without machine learning, carefully chosen features and weights were enough to create different results for different user profiles.
