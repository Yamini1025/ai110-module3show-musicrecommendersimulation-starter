"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}


    profiles = [
        {
            "name" : "Energetic Rock Fan",
            "prefs" : {"genre": "rock", "mood": "energetic", "energy": 0.9}
        },
        {
            "name" : "Chill Jazz Listener",
            "prefs" : {"genre": "jazz", "mood": "relaxed", "energy": 0.3}
        },
        {
            "name" : "Classical Music Enthusiast",
            "prefs" : {"genre": "classical", "mood": "calm", "energy": 0.2}
        },
        {
            "name" : "Hip-Hop Aficionado",
            "prefs" : {"genre": "hip-hop", "mood": "confident", "energy": 0.7}
        },
        {
            "name" : "Electronic Dance Partygoer",
            "prefs" : {"genre": "electronic", "mood": "upbeat", "energy": 0.8}
        }
    ]


    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Show the profile we're recommending for.
    print(
        f"\nRecommendations for: genre={user_prefs['genre']}, "
        f"mood={user_prefs['mood']}, energy={user_prefs['energy']}"
    )
    print("=" * 50)

    for rank, rec in enumerate(recommendations, start=1):
        # Each item is a (song, score, explanation) tuple.
        song, score, explanation = rec
        print(f"\n{rank}. {song['title']} — {song['artist']}")
        print(f"   Score:  {score:.2f}")
        print(f"   Reasons: {explanation}")

    
    for profile in profiles:
        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        print(f"\n{profile['name']}")
        print(f"Preferences: {profile['prefs']}")
        print("=" * 50)

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n{rank}. {song['title']} — {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")

        print("\n")

    print()


if __name__ == "__main__":
    main()
