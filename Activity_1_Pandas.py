import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Create the DataFrame
# -------------------------------
# (This DataFrame is built from our combined survey data.
#  Each row represents the aggregated count for a given response in a given question.)
combined_data = [
    {"Question": "Year of Study", "Response": 1, "Count": 4},
    {"Question": "Year of Study", "Response": 2, "Count": 4},
    {"Question": "Year of Study", "Response": 3, "Count": 11},
    {"Question": "Year of Study", "Response": 4, "Count": 3},
    {"Question": "Preferred Study Method", "Response": 1, "Count": 9},
    {"Question": "Preferred Study Method", "Response": 2, "Count": 8},
    {"Question": "Preferred Study Method", "Response": 3, "Count": 2},
    {"Question": "Preferred Study Method", "Response": 4, "Count": 3},
    {"Question": "Overall Course Quality", "Response": 1, "Count": 1},
    {"Question": "Overall Course Quality", "Response": 2, "Count": 2},
    {"Question": "Overall Course Quality", "Response": 3, "Count": 7},
    {"Question": "Overall Course Quality", "Response": 4, "Count": 4},
    {"Question": "Overall Course Quality", "Response": 5, "Count": 8},
    {"Question": "Instructor Satisfaction", "Response": 1, "Count": 4},
    {"Question": "Instructor Satisfaction", "Response": 2, "Count": 2},
    {"Question": "Instructor Satisfaction", "Response": 3, "Count": 4},
    {"Question": "Instructor Satisfaction", "Response": 4, "Count": 4},
    {"Question": "Instructor Satisfaction", "Response": 5, "Count": 8},
    {"Question": "Engaging Assignments/Projects", "Response": 1, "Count": 1},
    {"Question": "Engaging Assignments/Projects", "Response": 2, "Count": 1},
    {"Question": "Engaging Assignments/Projects", "Response": 3, "Count": 4},
    {"Question": "Engaging Assignments/Projects", "Response": 4, "Count": 9},
    {"Question": "Engaging Assignments/Projects", "Response": 5, "Count": 7},
    {"Question": "Course Materials", "Response": 1, "Count": 5},
    {"Question": "Course Materials", "Response": 2, "Count": 2},
    {"Question": "Course Materials", "Response": 3, "Count": 2},
    {"Question": "Course Materials", "Response": 4, "Count": 5},
    {"Question": "Course Materials", "Response": 5, "Count": 8},
    {"Question": "Instructor Explains", "Response": 1, "Count": 1},
    {"Question": "Instructor Explains", "Response": 2, "Count": 3},
    {"Question": "Instructor Explains", "Response": 3, "Count": 4},
    {"Question": "Instructor Explains", "Response": 4, "Count": 9},
    {"Question": "Instructor Explains", "Response": 5, "Count": 5},
    {"Question": "Student Participation", "Response": 1, "Count": 2},
    {"Question": "Student Participation", "Response": 2, "Count": 2},
    {"Question": "Student Participation", "Response": 3, "Count": 5},
    {"Question": "Student Participation", "Response": 4, "Count": 5},
    {"Question": "Student Participation", "Response": 5, "Count": 8},
    {"Question": "Instructor Approachable", "Response": 1, "Count": 1},
    {"Question": "Instructor Approachable", "Response": 2, "Count": 2},
    {"Question": "Instructor Approachable", "Response": 3, "Count": 4},
    {"Question": "Instructor Approachable", "Response": 4, "Count": 9},
    {"Question": "Instructor Approachable", "Response": 5, "Count": 6},
    {"Question": "Well-Equipped Classroom", "Response": 1, "Count": 4},
    {"Question": "Well-Equipped Classroom", "Response": 2, "Count": 1},
    {"Question": "Well-Equipped Classroom", "Response": 3, "Count": 2},
    {"Question": "Well-Equipped Classroom", "Response": 4, "Count": 7},
    {"Question": "Well-Equipped Classroom", "Response": 5, "Count": 8},
    {"Question": "Effective Lab Sessions", "Response": 1, "Count": 2},
    {"Question": "Effective Lab Sessions", "Response": 2, "Count": 1},
    {"Question": "Effective Lab Sessions", "Response": 3, "Count": 2},
    {"Question": "Effective Lab Sessions", "Response": 4, "Count": 7},
    {"Question": "Effective Lab Sessions", "Response": 5, "Count": 10},
    {"Question": "University Resources", "Response": 1, "Count": 5},
    {"Question": "University Resources", "Response": 2, "Count": 1},
    {"Question": "University Resources", "Response": 3, "Count": 2},
    {"Question": "University Resources", "Response": 4, "Count": 9},
    {"Question": "University Resources", "Response": 5, "Count": 5},
    {"Question": "Study Hours", "Response": 0, "Count": 3},
    {"Question": "Study Hours", "Response": 2, "Count": 1},
    {"Question": "Study Hours", "Response": 3, "Count": 1},
    {"Question": "Study Hours", "Response": 4, "Count": 2},
    {"Question": "Study Hours", "Response": 5, "Count": 2},
    {"Question": "Study Hours", "Response": 6, "Count": 1},
    {"Question": "Study Hours", "Response": 7, "Count": 1},
    {"Question": "Study Hours", "Response": 8, "Count": 1},
    {"Question": "Study Hours", "Response": 10, "Count": 1},
    {"Question": "Study Hours", "Response": 12, "Count": 2},
    {"Question": "Study Hours", "Response": 14, "Count": 1},
    {"Question": "Study Hours", "Response": 20, "Count": 2},
    {"Question": "Study Hours", "Response": 24, "Count": 1},
    {"Question": "Study Hours", "Response": 26, "Count": 1},
    {"Question": "Lecture Attendance", "Response": 1, "Count": 11},
    {"Question": "Lecture Attendance", "Response": 2, "Count": 5},
    {"Question": "Lecture Attendance", "Response": 3, "Count": 4},
    {"Question": "Lecture Attendance", "Response": 4, "Count": 2},
    {"Question": "Biggest Challenges", "Response": 1, "Count": 10},
    {"Question": "Biggest Challenges", "Response": 2, "Count": 11},
    {"Question": "Biggest Challenges", "Response": 3, "Count": 12},
    {"Question": "Biggest Challenges", "Response": 4, "Count": 8},
    {"Question": "Biggest Challenges", "Response": 5, "Count": 6},
]

df = pd.DataFrame(combined_data)

# ------------------------------------------------
# Data Inspection
# ------------------------------------------------
print("First 5 rows of the DataFrame:")
print(df.head())

print("\nLast 5 rows of the DataFrame:")
print(df.tail())

print("\nDataFrame Info:")
df.info()

print("\nDataFrame Summary Statistics:")
print(df.describe())

# ------------------------------------------------
# Data Cleaning
# ------------------------------------------------
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# (Assuming no missing values in our aggregated data;
#  if any are found, you can choose to drop or fill them.)
df_cleaned = df.dropna()

# Remove duplicate rows if any
df_cleaned = df_cleaned.drop_duplicates()
print("\nDataFrame after cleaning (dropping missing and duplicate rows):")
print(df_cleaned)

# ------------------------------------------------
# Filtering and Querying
# ------------------------------------------------
# Filter rows where 'Count' exceeds 5
filtered_df = df_cleaned[df_cleaned["Count"] > 5]
print("\nRows where Count > 5:")
print(filtered_df)

# Use .query() to extract data where Response is greater than 3
query_df = df_cleaned.query("Response > 3")
print("\nRows where Response > 3 using .query():")
print(query_df)

# ------------------------------------------------
# Grouping and Aggregation
# ------------------------------------------------
# Group the data by 'Question' and calculate aggregate statistics for 'Count'
grouped = df_cleaned.groupby("Question")["Count"].agg(["sum", "mean", "count"])
print("\nGrouped Data (aggregated 'Count') by Question:")
print(grouped)

# ------------------------------------------------
# Sorting and Ranking
# ------------------------------------------------
# Sort the DataFrame by 'Count' in descending order
sorted_df = df_cleaned.sort_values(by="Count", ascending=False)
print("\nDataFrame sorted by Count (descending):")
print(sorted_df)

# Rank the values in the 'Count' column and add as a new column
df_cleaned["Rank"] = df_cleaned["Count"].rank(ascending=False)
print("\nDataFrame with Rank based on Count:")
print(df_cleaned)

# ------------------------------------------------
# Visualization
# ------------------------------------------------
# Plot a histogram of the 'Count' column
plt.figure(figsize=(10, 6))
plt.hist(df_cleaned["Count"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram of 'Count'")
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.show()

# Plot a boxplot of 'Response'
plt.figure(figsize=(8, 6))
sns.boxplot(x=df_cleaned["Response"])
plt.title("Boxplot of 'Response'")
plt.show()

# Scatterplot between 'Response' and 'Count'
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cleaned, x="Response", y="Count", hue="Question")
plt.title("Scatterplot of Response vs Count")
plt.show()

# Plot the correlation matrix of numerical columns ('Response' and 'Count')
corr = df_cleaned[["Response", "Count"]].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# ------------------------------------------------
# Column Operations
# ------------------------------------------------
# Create a new column that is a transformation of existing columns.
# For example, create a 'Score' column as Response multiplied by Count.
df_cleaned["Score"] = df_cleaned["Response"] * df_cleaned["Count"]
print("\nDataFrame with new 'Score' column:")
print(df_cleaned)

# Drop a column that you find irrelevant.
# For example, if we decide the 'Rank' column is not needed, we can drop it.
df_cleaned = df_cleaned.drop(columns=["Rank"])
print("\nDataFrame after dropping the 'Rank' column:")
print(df_cleaned)
