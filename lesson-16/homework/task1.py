import pandas as pd
import sqlite3

# Part 1: Reading Files

# --- chinook.db ---
with sqlite3.connect("lesson-16/homework/chinook.db") as connection:
    customer = pd.read_sql("SELECT * FROM customers", con=connection)
print(customer.head(10))

# --- iris.json ---
iris = pd.read_json("lesson-16/homework/iris.json")
print(iris.head())
print("Column Names:", list(iris.columns))
print("Dataset Shape:", iris.shape)

# --- titanic.xlsx ---
titanic = pd.read_excel("lesson-16/homework/titanic.xlsx")
print(titanic.head())

# --- movie.csv ---
movie = pd.read_csv("lesson-16/homework/movie.csv")
print(movie.sample(10))

# --- flights.parquet ---
flights_info = pd.read_parquet("lesson-16/homework/flights")  # Read all for .info()
print(flights_info.info())

# Part 2: Exploring DataFrames

# -- iris.json --
iris.columns = iris.columns.str.lower()
iris_selected = iris[['sepallength', 'sepalwidth']]
print(iris_selected.head())

# -- titanic.xlsx --
age_above_30 = titanic[titanic['Age'] > 30]
print(age_above_30.head())

# ✅ FIXED: Added () to call the function
gender_counts = titanic["Sex"].value_counts()
print(gender_counts)

# -- movie.csv --
long_movies = movie[movie['duration'] > 120]
sorted_long_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print(sorted_long_movies.head())

# -- flights.parquet --
flights_subset = flights_info[["origin", "dest", "carrier"]]  # You already read it
print(flights_subset.head())

unique_destinations = flights_subset["dest"].nunique()
print(f"Number of unique destinations: {unique_destinations}")

# Part 3: Challenges and Explorations

# -- iris.json --
print("Means:\n", iris.mean(numeric_only=True))
print("Medians:\n", iris.median(numeric_only=True))
print("Standard Deviations:\n", iris.std(numeric_only=True))

# -- titanic.xlsx --
print("Minimum age:", titanic['Age'].min())
print("Maximum age:", titanic['Age'].max())
print("Sum of ages:", titanic['Age'].sum())

# -- movie.csv --
director_likes = movie.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()
top_likes = director_likes.max()
print(f"Top director: {top_director} with {top_likes} likes")

longest_movies = movie[['movie_title', 'duration', 'director_name']].sort_values(by='duration', ascending=False).head(5)
print(longest_movies)

# -- flights.parquet (missing values) --
missing_vals = flights_info.isnull().sum()
print("Missing values per column:\n", missing_vals)

# Fill missing in a numerical column (example: dep_delay)
if 'dep_delay' in flights_info.columns:
    flights_info['dep_delay'] = flights_info['dep_delay'].fillna(flights_info['dep_delay'].mean())
    print("Missing values in 'dep_delay' after filling:", flights_info['dep_delay'].isnull().sum())
else:
    print("'dep_delay' column not found to fill missing values.")
