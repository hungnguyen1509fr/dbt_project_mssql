# ⚽ YouTube Football Analytics: Real Madrid vs Barcelona

This project analyzes and compares **YouTube performance metrics** of two iconic football clubs: **Real Madrid** and **FC Barcelona**, focusing on their digital visibility, engagement, and audience growth. The analysis is part of a broader portfolio in **Analytics Engineering** showcasing skills in **data extraction, transformation, modeling, and visualization**.

---

## 📊 Project Goal

To answer the question:  
**"Who owns the digital spotlight on YouTube: Real Madrid or Barcelona?"**

We analyzed:
- **Engagement**: Likes, comments, views
- **Visibility**: Video uploads, subscriber count
- **Growth**: Monthly changes over time

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|------|---------|
| **YouTube Data API v3** | Data extraction (video statistics & channel metadata) |
| **Python (Pandas, Requests)** | API calls, data processing |
| **dbt (data build tool)** | Data transformation & modeling |
| **Snowflake** | Cloud data warehouse for storage and processing |
| **Power BI** | Final data visualization and dashboarding |
| **Git & GitHub** | Version control and project collaboration |

---

## 🗂️ Project Structure

```bash
📁 youtube-football-analytics
│
├── 📁 data
│   ├── raw/               # Raw API data
│   └── processed/         # Cleaned & transformed CSVs
│
├── 📁 notebooks
│   └── data_collection.ipynb   # Python code for YouTube API scraping
│
├── 📁 dbt_project/
│   ├── models/
│   │   ├── staging/       # Clean & format raw data
│   │   └── marts/         # Final analytics-ready tables
│   └── dbt_project.yml
│
├── 📁 powerbi/
│   └── youtube_kpi_dashboard.pbix  # Final dashboard
│
├── .gitignore
└── README.md
