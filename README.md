# student_performance_analysis
A Streamlit dashboard for visualizing student performance using UCI dataset. Analyze how factors like study time, internet access, and parental education affect grades through interactive charts and filters. Built with Python, Pandas, and Seaborn.
Here’s a well-structured `README.md` content for your **Student Performance Analysis Dashboard** project:

---

# Student Performance Analysis Dashboard

An interactive web dashboard built using **Python**, **Pandas**, **Seaborn**, and **Streamlit** to visualize and analyze student performance data from the UCI Machine Learning Repository.

---

## 🔍 Project Overview

This project transforms raw educational data into meaningful visual insights. It helps users explore how different factors—such as **study time**, **failures**, **internet access**, and **parental education**—influence student grades. A new feature, `avg_grade`, is computed as the average of G1, G2, and G3.

---

## 📊 Features

* Interactive filtering by gender, study time, failures, and more
* Dynamic visualizations: histograms, boxplots, heatmaps
* Correlation analysis to reveal performance drivers
* Clean, user-friendly interface using Streamlit

---

## 🗂 Dataset

* **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
* **Attributes**: 30+ variables including G1, G2, G3 (grades), demographic and behavioral data
* **Target Variable**: `avg_grade` (computed as average of G1, G2, G3)

---

## 🛠 Tech Stack

* **Language**: Python 3
* **Libraries**:

  * `pandas` for data manipulation
  * `seaborn` & `matplotlib` for data visualization
  * `streamlit` for building the interactive dashboard

---

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/student-performance-dashboard.git
   cd student-performance-dashboard
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 📷 Preview

(Add a screenshot of your dashboard here)

---

## 📄 License

This project is licensed under the MIT License.

---



