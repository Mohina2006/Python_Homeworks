import requests
import random

API_KEY = "b9285cefa5c006c74445a5e2450789b2"

def get_genres():
    try:
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raise exception for HTTP errors
        data = response.json()
        
        genres = data.get('genres', [])
        if not genres:
            print("⚠️ No genres found in the response.")
            return {}

        print("\nAvailable Genres:")
        for genre in genres:
            print(f"{genre['id']}: {genre['name']}")
        
        return {genre['name'].lower(): genre['id'] for genre in genres}
    
    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching genres: {e}")
        return {}

def get_movies_by_genre(genre_id):
    try:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        movies = data.get('results', [])
        if not movies:
            print("No movies found for this genre")
        return movies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []
    
def recommend_random_movie(movies):
    if not movies:
        print("Cannot recommend a movie from an empty list!")
        return
    movie = random.choice(movies)
    print(f"\n🎬 Recommended Movie:")
    print(f"Title: {movie.get('title', 'Unknown')}")
    print(f"Overview: {movie.get('overview', 'No description available.')}")
    print(f"Release Date: {movie.get('release_date', 'N/A')}")
    print(f"Rating: {movie.get('vote_average', 'N/A')}/10")

genre_dict = get_genres()

if genre_dict:
    try:
        user_input = input("\n👉 Enter a genre from the list above: ").lower().strip()
        genre_id = genre_dict.get(user_input)
        if genre_id :
            movies = get_movies_by_genre(genre_id)
            recommend_random_movie(movies)
        else:
            print("Genre not recognized!")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
else:
    print("Can't proceed without genre data")


