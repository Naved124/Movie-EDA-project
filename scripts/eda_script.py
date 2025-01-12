
import pandas as pd
import ast
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data_path = "outputs/data/cleaned_tmdb_data.csv"
data = pd.read_csv(data_path)

# Convert string representations of lists into actual lists
columns_to_convert = ['genres', 'keywords', 'production_companies', 'production_countries', 'spoken_languages']
for col in columns_to_convert:
    data[col] = data[col].apply(ast.literal_eval)

# Convert release_date to datetime
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
data['release_year'] = data['release_date'].dt.year

# 1. Genre Analysis
plt.figure(figsize=(8, 5))
genre_counts = data['genres'].explode().value_counts().head(10)
genre_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Top 10 Genres by Movie Count")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("outputs/plots/genre_analysis.png")

# 2. Budget vs Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x='budget', y='revenue', alpha=0.6, color='green')
plt.title("Budget vs Revenue")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/plots/budget_vs_revenue.png")

# 3. Average Runtime Over the Years
avg_runtime_by_year = data.groupby('release_year')['runtime'].mean()
plt.figure(figsize=(8, 5))
avg_runtime_by_year.plot(color='purple')
plt.title("Average Runtime Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Runtime (minutes)")
plt.tight_layout()
plt.savefig("outputs/plots/average_runtime.png")

# 4. Vote Average Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['vote_average'], kde=True, color='orange', bins=20)
plt.title("Distribution of Vote Averages")
plt.xlabel("Vote Average")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/plots/vote_average_distribution.png")

print("EDA completed. Check outputs/plots for visualizations.")
