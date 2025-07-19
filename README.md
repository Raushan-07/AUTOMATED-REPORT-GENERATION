# AUTOMATED-REPORT-GENERATION



# Code Explanation: Automated Employee Salary Report Generator
This Python script is designed to automate the process of data analysis and report generation by reading a dataset (employee_data.csv), performing statistical computations, visualizing key metrics, and producing a well-formatted PDF report using the FPDF library.

Below is a detailed walkthrough of each section of the code:

## 1. Importing Required Libraries
python
Copy
Edit
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
pandas: Used for reading and manipulating the CSV file containing employee data.

matplotlib.pyplot: Used to generate a bar chart for average salary by department.

fpdf: Used to create the formatted PDF document.

## 2. Reading the Input File
python
Copy
Edit
df = pd.read_csv("employee_data.csv")
The employee_data.csv file should include at least three columns: Name, Department, and Salary.

The script loads this data into a DataFrame df for analysis.

## 3. Performing Key Data Analysis
python
Copy
Edit
total_employees = len(df)
avg_salary = df["Salary"].mean()
highest_paid = df[df["Salary"] == df["Salary"].max()]["Name"].values[0]
highest_salary = df["Salary"].max()
Total Employees: Count of rows in the dataset.

Average Salary: Mean salary calculated using .mean().

Highest Paid Employee: Identified using filtering where salary equals max salary.

Highest Salary: Extracted using .max().

These statistics give a quick overview of the workforce and salary distribution.

## 4. Department-wise Aggregation
dept_summary = df.groupby("Department")["Salary"].agg(['count', 'mean']).reset_index()
Grouping by the Department column allows the script to calculate:

count: Number of employees in each department.

mean: Average salary per department.

The reset_index() method is used to convert the groupby object into a flat DataFrame.

## 5. Generating the Bar Chart

plt.figure(figsize=(8, 5))
plt.bar(dept_summary['Department'], dept_summary['mean'], color='skyblue')
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Avg Salary")
plt.tight_layout()
plt.savefig("salary_chart.png")
plt.close()
The bar chart visually represents the average salary in each department.

salary_chart.png is saved locally and will be embedded into the PDF later.

tight_layout() ensures that the plot does not cut off labels or titles.

## 6. Creating the PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 12, "Employee Salary Report", ln=True, align='C')
pdf.ln(10)
A new PDF object is created and a page is added.

The title "Employee Salary Report" is centered at the top using cell().

Summary Section
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 12, "Summary",'B', ln=True, align='C')
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Total Employees: {total_employees}", ln=True)
pdf.cell(0, 10, f"Average Salary: Rs. {avg_salary:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Paid Employee: {highest_paid} (Rs. {highest_salary})", ln=True)
pdf.ln(10)
Displays key metrics calculated earlier: total employees, average salary, and top earner.

Department-Wise Salary Table
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Department", 1)
pdf.cell(40, 10, "Count", 1)
pdf.cell(60, 10, "Avg Salary", 1, ln=True)

pdf.set_font("Arial", '', 12)
for index, row in dept_summary.iterrows():
    pdf.cell(60, 10, row['Department'], 1)
    pdf.cell(40, 10, str(row['count']), 1)
    pdf.cell(60, 10, f"Rs. {row['mean']:.2f}", 1, ln=True)
A formatted table is created to present department-level insights.

Data is drawn row by row from the dept_summary DataFrame.

## 7. Embedding the Salary Chart
pdf.ln(15)
pdf.image("salary_chart.png", x=30, w=160)
Adds the previously saved bar chart to the PDF.

x=30 positions the image horizontally, and w=160 sets the image width.

## 8. Saving the PDF File
pdf.output("enhanced_salary_report.pdf")
print("Enhanced PDF report created successfully: 'enhanced_salary_report.pdf'")
The report is saved in the current working directory with the name enhanced_salary_report.pdf.

# output 
[enhanced_salary_report.pdf](https://github.com/user-attachments/files/21328490/enhanced_salary_report.pdf)
