import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Student Performance Dashboard", layout="centered")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("student-mat.csv", sep=";")

df = load_data()
df['avg_grade'] = (df['G1'] + df['G2'] + df['G3']) / 3

# Title
st.title("📊 Student Performance Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filters")
study_time = st.sidebar.slider("Study Time (1=<2h, 4=>10h)", 1, 4, (1, 4))
internet = st.sidebar.selectbox("Internet Access", ["all"] + df["internet"].unique().tolist())
failures = st.sidebar.slider("Failures", 0, df["failures"].max(), (0, df["failures"].max()))

# Apply filters
filtered_df = df[
    (df['studytime'] >= study_time[0]) &
    (df['studytime'] <= study_time[1]) &
    (df['failures'] >= failures[0]) &
    (df['failures'] <= failures[1])
]

if internet != "all":
    filtered_df = filtered_df[filtered_df["internet"] == internet]

st.subheader("📋 Dataset Preview")
st.dataframe(filtered_df.head())

# Histogram of average grade
st.subheader("📈 Distribution of Average Grades")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df['avg_grade'], kde=True, color='skyblue', ax=ax1)
st.pyplot(fig1)

# Boxplot: Study Time vs Grade
st.subheader("📚 Study Time vs Average Grade")
fig2, ax2 = plt.subplots()
sns.boxplot(x='studytime', y='avg_grade', data=filtered_df, ax=ax2)
st.pyplot(fig2)

# Boxplot: Failures vs Grade
st.subheader("❌ Failures vs Average Grade")
fig3, ax3 = plt.subplots()
sns.boxplot(x='failures', y='avg_grade', data=filtered_df, ax=ax3)
st.pyplot(fig3)

# Correlation Heatmap
st.subheader("🔗 Correlation Heatmap")
fig4, ax4 = plt.subplots(figsize=(10, 8))
numeric = filtered_df.select_dtypes(include='number')
sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax4)
st.pyplot(fig4)

st.success("Dashboard loaded successfully!")
