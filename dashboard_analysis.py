import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

risk_df = pd.read_csv("data/risk_register.csv")
audit_df = pd.read_csv("data/audit_findings.csv")
controls_df = pd.read_csv("data/compliance_controls.csv")

avg_risk = risk_df.groupby("department")["risk_score"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=avg_risk.index, y=avg_risk.values)
plt.title("Average Risk Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Risk Score")
plt.tight_layout()
plt.savefig("outputs/department_risk_score.png")
plt.close()

status_counts = controls_df["status"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%")
plt.title("Compliance Control Status")
plt.tight_layout()
plt.savefig("outputs/compliance_status.png")
plt.close()

severity_counts = audit_df["severity"].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(x=severity_counts.index, y=severity_counts.values)
plt.title("Audit Findings by Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Findings")
plt.tight_layout()
plt.savefig("outputs/audit_findings_severity.png")
plt.close()

print("Dashboard charts created successfully in the outputs folder.")
