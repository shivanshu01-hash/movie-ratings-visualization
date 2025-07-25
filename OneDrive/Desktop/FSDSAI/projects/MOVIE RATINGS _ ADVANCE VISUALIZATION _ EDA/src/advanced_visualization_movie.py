import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

print("Working directory:", os.getcwd())

# Load data
df = pd.read_csv('C:\Users\dell\OneDrive\Desktop\FSDSAI\projects\MOVIE RATINGS _ ADVANCE VISUALIZATION _ EDA 1\data\Movie-Rating.csv')

# Data Cleaning
df.dropna(inplace=True)

# Descriptive stats
print(df.describe())

# Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Genre', y='AudienceRating')
plt.title('Audience Rating by Genre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/audience_rating_by_genre.png')
plt.show()
