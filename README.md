# 📊 Adult Census Income Interactive Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Dash-Plotly-00814d?style=for-the-badge&logo=dash&logoColor=white" alt="Dash">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle">
</p>

---

## 🚀 Project Overview
> **Goal:** Develop a sophisticated socio-economic intelligence tool to identify key factors influencing high-earning potential (>50K/year).

This dashboard transforms raw census data into **22 dynamic visualizations**, providing an immersive experience to explore correlations between education, job roles, and demographics.

---

## 🛠️ Technical Deep Dive

### 🧠 Data Pipeline (`data_processing.py`)

| Phase | Action | Result |
| :--- | :--- | :--- |
| **Ingestion** | `kagglehub` API | Fully automated dataset fetching & sync. |
| **Cleaning** | Null Management | Replaced `?` with `Unknown` for data integrity. |
| **Engineering** | Feature Synthesis | Grouped 16+ Edu levels & 14+ Occupations into tiers. |
| **Binning** | Categorical Bucketing | Converted `Age` & `Hours` into logical ranges. |

---

### 📊 Visualization Strategy
The dashboard utilizes advanced statistical charts to uncover hidden patterns:

* **Advanced Analytics:**
    * **Conditional Probabilities:** $P(\text{Income} > 50K | \text{Work Intensity})$.
    * **Correlation Heatmaps:** Occupation vs. Education impact matrix.
* **Gap Analysis:**
    * **Gender Wage Gap:** Multi-line tracking across academic levels.
    * **Distribution Analysis:** Box plots for outlier detection in workclasses.

---

## ✨ Key Interactive Features

### 🗂️ Multi-Tab Navigation
* **📈 Overview**: Summary KPIs (Total Records, High Earners %, Avg Age).
* **👥 Demographics**: Income analysis by **Race**, **Gender**, and **Nationality**.
* **💼 Work & Income**: Analysis of **Workclass**, **Occupation**, and **Work Intensity**.
* **🎓 Education**: The direct correlation between degrees and wealth.
* **💑 Relationships**: Financial trends based on marital and family status.

### 🕹️ User Controls
* **Global Age Filter**: Reactive dropdown updating **all 22 charts** instantly.
* **Modern UI/UX**: Custom **CSS** with a gradient "Glassmorphism" header and responsive grid layout.

---

## ⚙️ Installation & Usage

1. **Setup Environment**:
   ```bash
   # Clone the repository
   git clone https://github.com/Emanorabi254/Adult-Census-Income-Analysis-Dashboard.git
   # Enter the directory
   cd Adult-Census-Income-Analysis-Dashboard
2. **Install Libraries**:
   ```bash
   pip install -r requirements.txt
3. **Run Application**:
   ```bash
   python app.py
4. **Access UI**:  Open http://127.0.0.1:8050/ in your browser.

---
## ✉️ Contact

<p align="center">
  <a href="https://www.linkedin.com/in/eman-orabi254/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  &nbsp; 
  <a href="emanorabi254@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</p>
