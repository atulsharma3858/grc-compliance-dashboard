import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("risk_register.csv")

# Show first rows
print(df.head())

# Average risk score by department
avg_risk = df.groupby("department")["risk_score"].mean()

print(avg_risk)

# Create bar chart
plt.figure(figsize=(8,5))

sns.barplot(
    x=avg_risk.index,
    y=avg_risk.values
)

plt.title("Average Risk Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Risk Score")

plt.tight_layout()

plt.savefig("department_risk_chart.png")

print("Chart created successfully.")
