import sqlite3
import pandas as pd

# === Loading chinook.db ===
with sqlite3.connect("lesson-17/homework/chinook.db") as connection:
    customer = pd.read_sql("SELECT * FROM customers", con=connection)
    invoices = pd.read_sql("SELECT * FROM invoices", con=connection)

# Inner join
merge_pd = pd.merge(customer, invoices, on="CustomerId", how="inner")

# Total invoices per customer
invoice_counts = merge_pd.groupby(["CustomerId", "FirstName", "LastName"]).size().reset_index(name="Total_invoices")
print("=== Invoice Counts ===")
print(invoice_counts.head())

# === Loading the movie.csv file ===
movie = pd.read_csv("lesson-17/homework/movie.csv")

# Two smaller DataFrames
color = movie[['director_name', 'color']].drop_duplicates()
reviews = movie[['director_name', 'num_critic_for_reviews']].drop_duplicates()

# Left join
left_join = pd.merge(color, reviews, on='director_name', how="left")
print("\n=== Left Join rows:", len(left_join))

# Full outer join
full_outer_join_df = pd.merge(color, reviews, on='director_name', how='outer')
print("Full Outer Join rows:", len(full_outer_join_df))

# === Titanic Analysis ===
titanic = pd.read_excel("lesson-17/homework/titanic.xlsx")
pclass_group = titanic.groupby('Pclass')

# Aggregation
titanic_summary = pclass_group.agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'
}).rename(columns={'Age': 'Avgage', 'Fare': 'TotalFare', 'PassengerId': 'PassengerCount'})
print("\n=== Titanic Summary ===")
print(titanic_summary)

# === Multi-level grouping in Movies ===
movie = movie.dropna(subset=['color', 'director_name', 'num_critic_for_reviews', 'duration'])
multi_group = movie.groupby(['color', 'director_name'])
movie_grouped = multi_group.agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
}).rename(columns={'num_critic_for_reviews': 'Total_Reviews', 'duration': 'AvgDuration'})
print("\n=== Movie Grouped Summary ===")
print(movie_grouped.head())

# === Nested Grouping on Flights ===
flights = pd.read_parquet("lesson-17/homework/flights", 
                          columns=['Year', 'Month', 'Flight_Number_Reporting_Airline', 'ArrDelay', 'DepDelay'])

flights = flights.head(500)

flights['ArrDelay'] = pd.to_numeric(flights['ArrDelay'], errors='coerce')
flights['DepDelay'] = pd.to_numeric(flights['DepDelay'], errors='coerce')

flights_grouped = flights.groupby(['Year', 'Month']).agg({
    'Flight_Number_Reporting_Airline': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
}).rename(columns={
    'Flight_Number_Reporting_Airline': 'TotalFlights',
    'ArrDelay': 'AvgArrivalDelay',
    'DepDelay': 'MaxDepartureDelay'
})
print("\n=== Flights Summary by Year & Month ===")
print(flights_grouped)


# === Applying a Custom Function on Titanic ===
titanic['Age_Group'] = titanic['Age'].apply(
    lambda x: 'Unknown' if pd.isnull(x) else ('Child' if x < 18 else 'Adult')
)
print("\n=== Titanic Age Groups ===")
print(titanic[['Age', 'Age_Group']].head())

# === Normalize Employee Salaries ===
employee = pd.read_csv("lesson-17/homework/employee.csv")
employee['NORMALIZED_SALARY'] = employee.groupby('DEPARTMENT')['BASE_SALARY'].transform(
    lambda x: (x - x.mean()) / x.std()
)
print("\n=== Normalized Employee Salaries ===")
print(employee[['DEPARTMENT', 'BASE_SALARY', 'NORMALIZED_SALARY']].head())

# === Custom Function on Movies: Short / Medium / Long ===

# Reload movie data and drop NaNs in duration
movie = pd.read_csv("lesson-17/homework/movie.csv")
movie = movie.dropna(subset=['duration'])

# Define classification function
def classify(x):
    if x < 60:
        return "Short"
    elif x <= 120:
        return "Medium"
    else:
        return "Long"

# Apply function with lambda
movie['Length_Category'] = movie['duration'].apply(lambda x: classify(x))

print("\n=== Movie Length Categories ===")
print(movie[['duration', 'Length_Category']].head(10))
#Pipeline on Titanic
titanic_pipeline = (titanic[titanic['Survived']==1].assign(Age = lambda df : df["Age"].fillna(df["Age"].mean()))
                    .assign(Fare_per_age = lambda df: df["Fare"]/df["Age"])
)
print(titanic_pipeline.head())
#print(flights.columns) used to check for the names of columns in flight
#Pipeline on Flights
flights_pipeline = (
    flights[flights["DepDelay"] > 30]
    .assign(Delay_Per_Hour=lambda df: df["DepDelay"] / df["ArrDelay"])
)
print(flights_pipeline.head())