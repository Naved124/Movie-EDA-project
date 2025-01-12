
# Movie EDA Project

This project explores the **TMDB 5000 Movies Dataset** to uncover insights about the movie industry through exploratory data analysis (EDA). It includes data cleaning, visualizations, and key observations about genres, budgets, revenues, and more.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Dataset](#dataset)
4. [Setup and Installation](#setup-and-installation)
5. [EDA Highlights](#eda-highlights)
6. [Results](#results)
7. [License](#license)

---

## Overview
The goal of this project is to perform a deep exploratory analysis of the TMDB 5000 Movies dataset, identify patterns, and create insightful visualizations. This analysis provides an understanding of:
- Popular genres.
- Relationship between budgets and revenues.
- Runtime trends over the years.
- Distribution of vote averages and more.

---

## Project Structure
```plaintext
Movie-EDA-Project/
├── notebooks/
│   └── eda_notebook.ipynb       # Interactive Jupyter notebook for EDA
├── scripts/
│   └── eda_script.py            # Python script for EDA
├── outputs/
│   ├── data/
│   │   └── cleaned_tmdb_data.csv # Cleaned dataset
│   ├── plots/
│   │   ├── genre_analysis.png    # Genre analysis plot
│   │   ├── budget_vs_revenue.png # Budget vs Revenue plot
│   │   ├── average_runtime.png   # Average runtime over the years
│   │   └── vote_average_distribution.png # Vote average distribution
├── README.md                    # Project description
└── requirements.txt             # Dependencies for the project
```

---

## Dataset
The dataset contains detailed information about 5000 movies, including:
- **Genres**: List of genres for each movie.
- **Budget and Revenue**: Financial details in dollars.
- **Runtime**: Length of the movie in minutes.
- **Vote Average**: Audience ratings.

You can download the original dataset from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

---

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Movie-EDA-Project.git
   cd Movie-EDA-Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/eda_notebook.ipynb
   ```

4. Alternatively, execute the Python script:
   ```bash
   python scripts/eda_script.py
   ```

---

## EDA Highlights
Key insights discovered:
- **Top Genres**: The most popular genres include Drama, Comedy, and Thriller.
- **Budget-Revenue Correlation**: High-budget movies generally earn higher revenues.
- **Runtime Trends**: Average movie runtimes have varied over the years.
- **Audience Ratings**: Most movies have a vote average between 6 and 8.

---

## Results
The visualizations generated during the analysis are stored in the `outputs/plots/` directory.

---

## License
This project is licensed under the [MIT License](LICENSE).
