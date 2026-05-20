import pandas as pd
import random
import os

os.makedirs("data", exist_ok=True)

departments = ["IT", "Finance", "HR", "Operations", "Security"]
frameworks = ["NIST", "ISO27001", "SOC2", "GDPR"]
statuses = ["Compliant", "Non-Compliant", "Partial"]
severities = ["Low", "Medium", "High", "Critical"]

risk_data = []

for i in range(100):
    likelihood = random.randint(1, 5)
    impact = random.randint(1, 5)
    risk_score = likelihood * impact

    risk_data.append({
        "risk_id": f"RISK-{i+1}",
        "department": random.choice(departments),
        "framework": random.choice(frameworks),
        "likelihood": likelihood,
        "impact": impact,
        "risk_score": risk_score,
        "status": random.choice(statuses)
    })

risk_df = pd.DataFrame(risk_data)
risk_df.to_csv("data/risk_register.csv", index=False)

audit_data = []

for i in range(50):
    audit_data.append({
        "finding_id": f"FIND-{i+1}",
        "department": random.choice(departments),
        "severity": random.choice(severities),
        "status": random.choice(["Open", "Closed", "In Progress"])
    })

audit_df = pd.DataFrame(audit_data)
audit_df.to_csv("data/audit_findings.csv", index=False)

control_data = []

for i in range(80):
    control_data.append({
        "control_id": f"CTRL-{i+1}",
        "framework": random.choice(frameworks),
        "department": random.choice(departments),
        "status": random.choice(statuses)
    })

control_df = pd.DataFrame(control_data)
control_df.to_csv("data/compliance_controls.csv", index=False)

print("All datasets created successfully in the data folder.")
