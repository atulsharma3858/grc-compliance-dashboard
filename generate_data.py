import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Number of records
num_records = 100

departments = [
    "IT",
    "Finance",
    "HR",
    "Operations",
    "Security"
]

frameworks = [
    "NIST",
    "ISO27001",
    "SOC2",
    "GDPR"
]

statuses = [
    "Compliant",
    "Non-Compliant",
    "Partial"
]

risk_data = []

for i in range(num_records):

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

df = pd.DataFrame(risk_data)

print(df.head())

df.to_csv("risk_register.csv", index=False)

print("Risk register dataset created successfully.")
