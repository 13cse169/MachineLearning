data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [23, 45, 31, 22, 35],
    "Salary": [25000, 50000, 35000, 22000, 42000]
}

# 1. Show employees with Salary > 30000
high_salary = [emp for emp in zip(data["Name"], data["Salary"]) if emp[1] > 30000]
print("Employees with Salary > 30000:", high_salary)

# 2. Show employee with max salary
max_salary = max(data["Salary"])
max_salary_emp = [emp for emp in zip(data["Name"], data["Salary"]) if emp[1] == max_salary]
print("Employee with max salary:", max_salary_emp)

# 3. Show average salary
average_salary = sum(data["Salary"]) / len(data["Salary"])
print("Average salary:", average_salary)

# 4. Add new column Tax = Salary * 0.05
data["Tax"] = [salary * 0.05 for salary in data["Salary"]]
print("Data with Tax column:", data)

# 5. Sort by Age
sorted_data = sorted(zip(data["Name"], data["Age"], data["Salary"], data["Tax"]), key=lambda x: x[1])
print("Data sorted by Age:", sorted_data)