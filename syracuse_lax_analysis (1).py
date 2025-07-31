# Syracuse Lacrosse 2024 Season Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn theme
sns.set(style="whitegrid")

# --- 1. Top 5 Scorers ---
top_scorers = pd.DataFrame({
    "Player": ["Owen Hiltz", "Joey Spallina", "Christian Mulé", "Michael Leo", "Sam English"],
    "Goals": [38, 37, 25, 28, 23]
})

plt.figure(figsize=(8, 5))
sns.barplot(data=top_scorers, x="Player", y="Goals", palette="Blues_d")
plt.title("Top 5 Syracuse Scorers - 2024 Season")
plt.ylabel("Goals")
plt.xlabel("Player")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 2. Game Results Pie Chart ---
game_results = pd.DataFrame({
    "Result": ["Wins", "Losses"],
    "Count": [12, 6]
})

plt.figure(figsize=(6, 6))
plt.pie(game_results["Count"], labels=game_results["Result"], autopct='%1.1f%%', colors=["green", "red"])
plt.title("Game Results - 2024 Season")
plt.show()

# --- 3. Goals by Period ---
goals_by_period = pd.DataFrame({
    "Period": ["1st", "2nd", "3rd", "4th", "OT"],
    "Syracuse": [77, 57, 77, 54, 0],
    "Opponents": [62, 43, 46, 44, 3]
})

goals_by_period_melted = goals_by_period.melt(id_vars="Period", var_name="Team", value_name="Goals")

plt.figure(figsize=(8, 5))
sns.barplot(data=goals_by_period_melted, x="Period", y="Goals", hue="Team")
plt.title("Goals by Period - Syracuse vs Opponents")
plt.ylabel("Goals")
plt.xlabel("Game Period")
plt.tight_layout()
plt.show()
