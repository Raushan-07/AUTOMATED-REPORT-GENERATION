import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Read data
df = pd.read_csv("employee_data.csv")

# Analysis
total_employees = len(df)
avg_salary = df["Salary"].mean()
highest_paid = df[df["Salary"] == df["Salary"].max()]["Name"].values[0]
highest_salary = df["Salary"].max()

# Group by department
dept_summary = df.groupby("Department")["Salary"].agg(['count', 'mean']).reset_index()

# Bar Chart: Avg Salary per Department
plt.figure(figsize=(8, 5))
plt.bar(dept_summary['Department'], dept_summary['mean'], color='skyblue')
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Avg Salary")
plt.tight_layout()
plt.savefig("salary_chart.png")
plt.close()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 12, "Employee Salary Report", ln=True, align='C')
pdf.ln(10)

# Summary Section

pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 12, "Summary",'B', ln=True, align='C')
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Total Employees: {total_employees}", ln=True)
pdf.cell(0, 10, f"Average Salary: Rs. {avg_salary:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Paid Employee: {highest_paid} (Rs. {highest_salary})", ln=True)
pdf.ln(10)

# Department Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Department", 1)
pdf.cell(40, 10, "Count", 1)
pdf.cell(60, 10, "Avg Salary", 1, ln=True)

# Table Data
pdf.set_font("Arial", '', 12)
for index, row in dept_summary.iterrows():
    pdf.cell(60, 10, row['Department'], 1)
    pdf.cell(40, 10, str(row['count']), 1)
    pdf.cell(60, 10, f"Rs. {row['mean']:.2f}", 1, ln=True)

# Add Graph Image
pdf.ln(15)
pdf.image("salary_chart.png", x=30, w=160)

# Save PDF
pdf.output("enhanced_salary_report.pdf")
print("Enhanced PDF report created successfully: 'enhanced_salary_report.pdf'")
