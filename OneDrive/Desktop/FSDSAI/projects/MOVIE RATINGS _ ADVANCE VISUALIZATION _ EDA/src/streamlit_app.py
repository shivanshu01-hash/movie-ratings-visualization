import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🎬 Movie Ratings - All Seaborn Plots")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(r'C:\Users\dell\OneDrive\Desktop\FSDSAI\projects\MOVIE RATINGS _ ADVANCE VISUALIZATION _ EDA 1\data\Movie-Rating.csv')

df = load_data()
df.dropna(inplace=True)

# Columns rename
df.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

# Data type conversion
df['Film'] = df['Film'].astype('category')
df['Genre'] = df['Genre'].astype('category')
df['Year'] = df['Year'].astype('category')

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Select numeric and categorical columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

# Plot options
plot_types = ["Boxplot", "Violinplot", "Barplot", "Histogram", "KDEplot", "Countplot", "Stripplot", "Swarmplot", "Heatmap"]
plot_choice = st.selectbox("Choose a plot type:", plot_types)

if plot_choice == "Boxplot":
    x = st.selectbox("X-axis (categorical):", categorical_cols)
    y = st.selectbox("Y-axis (numeric):", numeric_cols)
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=x, y=y, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Violinplot":
    x = st.selectbox("X-axis (categorical):", categorical_cols)
    y = st.selectbox("Y-axis (numeric):", numeric_cols)
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x=x, y=y, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Barplot":
    x = st.selectbox("X-axis (categorical):", categorical_cols)
    y = st.selectbox("Y-axis (numeric):", numeric_cols)
    fig, ax = plt.subplots()
    sns.barplot(data=df, x=x, y=y, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Histogram":
    x = st.selectbox("Choose numeric column:", numeric_cols)
    bins = st.slider("Number of bins:", 5, 50, 10)
    fig, ax = plt.subplots()
    sns.histplot(df[x], bins=bins, kde=False, ax=ax)
    st.pyplot(fig)

elif plot_choice == "KDEplot":
    x = st.selectbox("Choose numeric column:", numeric_cols)
    fig, ax = plt.subplots()
    sns.kdeplot(df[x], fill=True, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Countplot":
    x = st.selectbox("Choose categorical column:", categorical_cols)
    fig, ax = plt.subplots()
    sns.countplot(data=df, x=x, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Stripplot":
    x = st.selectbox("X-axis (categorical):", categorical_cols)
    y = st.selectbox("Y-axis (numeric):", numeric_cols)
    fig, ax = plt.subplots()
    sns.stripplot(data=df, x=x, y=y, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Swarmplot":
    x = st.selectbox("X-axis (categorical):", categorical_cols)
    y = st.selectbox("Y-axis (numeric):", numeric_cols)
    fig, ax = plt.subplots()
    sns.swarmplot(data=df, x=x, y=y, ax=ax)
    st.pyplot(fig)

elif plot_choice == "Heatmap":
    corr = df[numeric_cols].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
