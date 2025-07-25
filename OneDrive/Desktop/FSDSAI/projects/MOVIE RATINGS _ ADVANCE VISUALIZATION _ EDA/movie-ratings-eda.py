import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the CSV file
# print(os.getcwd())
path = r"C:\Users\dell\OneDrive\Desktop\FSDSAI\projects\MOVIE RATINGS _ ADVANCE VISUALIZATION _ EDA 1\data\Movie-Rating.csv"
movies = pd.read_csv(path)

# Columns rename
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

# Data type conversion
movies['Film'] = movies['Film'].astype('category')
movies['Genre'] = movies['Genre'].astype('category')
movies['Year'] = movies['Year'].astype('category')

# Visualization settings
sns.set_theme(style="darkgrid")

def plot_jointplots(movies):
    plt.figure()
    # KDE Jointplot: shows point density with smooth contours
    sns.jointplot(data=movies, x="CriticRating", y="AudienceRating", kind="kde", fill=True)
    plt.suptitle("Critic vs Audience Rating — KDE Jointplot", y=1.02)
    plt.show()

    # Hexbin Jointplot: useful when there are many overlapping points
    sns.jointplot(data=movies, x="CriticRating", y="AudienceRating", kind="hex")
    plt.suptitle("Critic vs Audience Rating — Hexbin Plot", y=1.02)
    plt.show()
    
    # Regression Jointplot
    sns.jointplot(data=movies, x="CriticRating", y="AudienceRating", kind="reg", scatter_kws={'alpha':0.5})
    plt.suptitle("Critic vs Audience Rating — Regression Plot", y=1.02)
    plt.show()

def plot_histograms(movies):
    plt.figure()
    # Histogram for AudienceRating
    sns.histplot(data=movies, x="AudienceRating", bins=15, kde=True)
    plt.title("Audience Rating Distribution")
    plt.xlabel("Audience Rating")
    plt.ylabel("Count")
    plt.show()

    # Histogram for BudgetMillions
    sns.histplot(data=movies, x="BudgetMillions", bins=15, kde=True)
    plt.title("Budget (Millions) Distribution")
    plt.xlabel("Budget (Millions)")
    plt.ylabel("Count")
    plt.show()

def plot_budget_by_genre_stacked(movies):
    genres = movies["Genre"].unique()
    # Build list of BudgetMillions by genre
    data = [movies[movies.Genre == g]["BudgetMillions"] for g in genres]
    plt.figure(figsize=(10,6))
    plt.hist(data, bins=20, stacked=True, label=genres, alpha=0.7)
    plt.title("Stacked Histogram: Budget by Genre")
    plt.xlabel("Budget (Millions)")
    plt.ylabel("Number of Movies")
    plt.legend(title="Genre")
    plt.show()

def plot_lmplot_by_genre(movies):
    # lmplot: scatter with genre color coding (no regression line)
    sns.lmplot(data=movies, x="CriticRating", y="AudienceRating", hue="Genre", fit_reg=False, aspect=1.5)
    plt.title("Critic vs Audience Rating by Genre")
    plt.xlabel("Critic Rating")
    plt.ylabel("Audience Rating")
    plt.show()

def plot_facet_grid(movies):
    # FacetGrid: scatterplots split by Genre and Year
    g = sns.FacetGrid(movies, row="Genre", col="Year", hue="Genre", margin_titles=True, height=2.2)
    g.map_dataframe(sns.scatterplot, x="CriticRating", y="AudienceRating", alpha=0.5)
    g.set_axis_labels("Critic Rating", "Audience Rating")
    g.add_legend()
    plt.show()

plot_jointplots(movies)
plot_histograms(movies)
plot_budget_by_genre_stacked(movies)
plot_lmplot_by_genre(movies)
plot_facet_grid(movies)

# python is not vectorize programming language
# Building dashboards (dashboard - combination of chats)

def plot_movie_dashboard(movies):
    # Dashboard: Combined Plots
    sns.set_style('dark', {'axes.facecolor': 'black'})
    fig, axes = plt.subplots(2, 2, figsize=(15, 15))
    # Audience vs Budget KDE
    sns.kdeplot(x=movies.BudgetMillions, y=movies.AudienceRating, shade=True, fill=True, cmap='inferno', ax=axes[0,0])
    axes[0,0].set_title("Budget vs Audience Rating (KDE)")
    # Critic vs Budget KDE
    sns.kdeplot(x=movies.BudgetMillions, y=movies.CriticRating, shade=True, fill=True, cmap='magma', ax=axes[0,1])
    axes[0,1].set_title("Budget vs Critic Rating (KDE)")
    # Drama Genre Violin Plot
    sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating', ax=axes[1,0])
    axes[1,0].set_title("Drama Movies: Year vs Critic Rating")
    # Critic vs Audience KDE
    sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, cmap='coolwarm', ax=axes[1,1])
    axes[1,1].set_title("Critic vs Audience Rating (KDE)")
    plt.tight_layout()
    plt.show()

plot_movie_dashboard(movies)


