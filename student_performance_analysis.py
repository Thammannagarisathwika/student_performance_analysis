import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Display first few rows
print(df.head())

# Basic Info
print("\nData Info:")
print(df.info())

# Summary statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Add a final grade average column
df['avg_grade'] = (df['G1'] + df['G2'] + df['G3']) / 3

# Distribution plot of average grades
plt.figure(figsize=(8,5))
sns.histplot(df['avg_grade'], kde=True, color='skyblue')
plt.title("Distribution of Average Grades")
plt.xlabel("Average Grade")
plt.ylabel("Count")
plt.show()

# Correlation heatmap
plt.figure(figsize=(12,8))
correlation = df.select_dtypes(include='number').corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Study time vs final grade
plt.figure(figsize=(8,5))
sns.boxplot(x='studytime', y='avg_grade', data=df)
plt.title("Study Time vs Average Grade")
plt.xlabel("Study Time (1= <2h, 4= >10h)")
plt.ylabel("Average Grade")
plt.show()

# Failures vs average grade
plt.figure(figsize=(8,5))
sns.boxplot(x='failures', y='avg_grade', data=df)
plt.title("Failures vs Average Grade")
plt.xlabel("Number of Past Failures")
plt.ylabel("Average Grade")
plt.show()

# Internet access vs grade
plt.figure(figsize=(6,4))
sns.boxplot(x='internet', y='avg_grade', data=df)
plt.title("Internet Access vs Average Grade")
plt.xlabel("Internet Access")
plt.ylabel("Average Grade")
plt.show()

# Parental education impact
plt.figure(figsize=(8,5))
sns.boxplot(x='Medu', y='avg_grade', data=df)
plt.title("Mother's Education vs Average Grade")
plt.xlabel("Mother's Education Level (0 to 4)")
plt.ylabel("Average Grade")
plt.show()
