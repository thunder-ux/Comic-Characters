import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
characters = pd.read_csv('characters_stats.csv')
# Streamlit app layout
st.title('Comic Characters Stats')
# Sidebar selection for character alignment
alignment = st.sidebar.selectbox(
    "Choose character alignment",
    ("All", "Good", "Bad", "Neutral")
)
if alignment == "Good":
    filtered_characters = characters[characters["Alignment"] == "good"]
elif alignment == "Bad":
    filtered_characters = characters[characters["Alignment"] == "bad"]
elif alignment == "Neutral":
    filtered_characters = characters[characters["Alignment"] == "neutral"]
else:
    filtered_characters = characters
    
# Show some basic information about the filtered characters
st.write(f"Number of characters: {len(filtered_characters)}")
st.write(filtered_characters.head())

# Select visualization type
visualization = st.sidebar.selectbox(
    "Choose visualization type",
    ("Bar Plot", "Pie Chart", "Scatter Plot", "Histogram", "Box Plot")
)
# Bar Plot: Compare different stats for selected characters
if visualization == "Bar Plot":
    st.subheader("Bar Plot: Compare Stats")
    selected_stats = st.multiselect("Select stats to compare", ['Strength', 'Speed', 'Power', 'Intelligence', 'Durability'])
    selected_names = st.multiselect("Select characters", filtered_characters['Name'].unique())
    if selected_stats and selected_names:
        data_to_plot = filtered_characters[filtered_characters['Name'].isin(selected_names)][['Name'] + selected_stats]
        st.bar_chart(data_to_plot.set_index('Name'))


if visualization == "Pie Chart":
    st.subheader("Pie Chart: Stat Distribution")
    selected_character = st.selectbox("Select a character", filtered_characters['Name'].unique())
    selected_stats = ['Strength', 'Speed', 'Power', 'Intelligence', 'Durability']
    character_stats = filtered_characters[filtered_characters['Name'] == selected_character].iloc[0]
    stats_values = character_stats[selected_stats]
    fig, ax = plt.subplots()
    ax.pie(stats_values, labels=selected_stats, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig)

    # Box Plot: Compare stat distribution by alignment
if visualization == "Box Plot":
    st.subheader("Box Plot: Stat Distribution by Alignment")
    selected_stat = st.selectbox("Select stat for box plot", ['Strength', 'Speed', 'Power', 'Intelligence', 'Durability'])
    fig, ax = plt.subplots(figsize=(8,6))
    sns.boxplot(x='Alignment', y=selected_stat, data=characters)
    st.pyplot(fig)

    # Histogram: Show distribution of a stat
if visualization == "Histogram":
    st.subheader("Histogram: Stat Distribution")
    selected_stat = st.selectbox("Select stat for histogram", ['Strength', 'Speed', 'Power', 'Intelligence', 'Durability'])
    fig, ax = plt.subplots()
    ax.hist(filtered_characters[selected_stat], bins=20, color='blue', alpha=0.7)
    ax.set_xlabel(selected_stat)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

     #Scatter Plot: Compare two stats
if visualization == "Scatter Plot":
    st.subheader("Scatter Plot: Compare Stats")
    stat_x = st.selectbox("Select X-axis stat", ['Strength', 'Speed', 'Power', 'Intelligence', 'Durability'])
    stat_y = st.selectbox("Select Y-axis stat", ['Strength', 'Speed', 'Power', 'Intelligence', 'Durability'])
    fig, ax = plt.subplots()
    ax.scatter(filtered_characters[stat_x], filtered_characters[stat_y], alpha=0.7)
    ax.set_xlabel(stat_x)
    ax.set_ylabel(stat_y)
    st.pyplot(fig)