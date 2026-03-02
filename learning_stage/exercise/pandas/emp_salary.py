try:
          import pandas as pd
except Exception:
          print("Pandas is not installed.")
          exit()


def emp_salary():
          data = {
                    "Name": ["A", "B", "C", "D", "E"],
                    "Age": [23, 45, 31, 22, 35],
                    "Salary": [25000, 50000, 35000, 22000, 42000],
                    "Department": ["IT", "HR", "IT", "HR", "Finance"]
          }
          
          df = pd.DataFrame(data)
          print("\n The employees data are : \n\n", df.to_string())
          
          print("\n-----------------------------------------------------\n")
          
          # 1. Show employees with Salary > 30000
          high_salary = df[df['Salary'] > 30000]
          print("\n Employees with Salary > 30000 : \n\n", high_salary.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 2. Show employee with max salary
          max_salary = df[df['Salary'] == df['Salary'].max()]
          print("\n Employee with max salary : \n\n", max_salary.to_string())
          
          emp_max_salary = df.loc[df['Salary'].idxmax()]
          print("\n Other way to Employee with max salary : \n\n", emp_max_salary.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 3. Show average salary
          average_salary = df['Salary'].mean()
          print("\n Average salary : ", average_salary)
          
          print("\n-----------------------------------------------------")
          
          # 4. Add new column Tax = Salary * 0.05
          df['Tax'] = df['Salary'] * 0.05
          print("\n Data with Tax column : \n\n", df.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 5. Sort by Age
          sorted_df = df.sort_values(by='Age')
          print("\nData sorted by Age : \n\n", sorted_df.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 6. Average salary by Department
          dept_avg_sal = df.groupby('Department')['Salary'].mean()
          print("\n Average salary by Department : \n\n", dept_avg_sal.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 7. Total salary by Department
          dept_ttl_sal = df.groupby('Department').sum()
          print("\n Total salary by Department : \n\n", dept_ttl_sal.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 8. Show highest salary per department
          dept_high_sal = df.groupby('Department')['Salary'].max()
          print("\n Highest salary per department : \n\n", dept_high_sal.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 9. Employee count per department
          dept_count_emp = df.groupby('Department')['Name'].count()
          print("\n Employee count per department : \n\n", dept_count_emp.to_string())
          
          print("\n-----------------------------------------------------")

def merge_join():
          emp = pd.DataFrame({
                    "EmpID": [1, 2, 3],
                    "Name": ["A", "B", "C"]
          })
          print("\n Employees Data : \n\n", emp.to_string())
          
          salary = pd.DataFrame({
                    "EmpID": [1, 2, 4],
                    "Salary": [30000, 40000, 50000]
          })
          print("\n Salary Data : \n\n", salary.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 1. Inner Join
          inner_join = pd.merge(emp, salary, on='EmpID', how='inner')
          print("\n Inner Join : \n\n", inner_join)
          
          print("\n-----------------------------------------------------")
          
          # 2. Left Join
          left_join = pd.merge(emp, salary, on='EmpID', how='left')
          print("\n Left Join : \n\n", left_join)
          
          print("\n-----------------------------------------------------")
          
          # 3. Right Join
          right_join = pd.merge(emp, salary, on='EmpID', how='right')
          print("\n Right Join : \n\n", right_join)
          
          print("\n-----------------------------------------------------")
          
          # 4. Outer Join
          outer_join = pd.merge(emp, salary, on='EmpID', how='outer')
          print("\n Outer Join : \n\n", outer_join)
          
          print("\n-----------------------------------------------------")

def level_1_practice():
          df = pd.DataFrame({
                    "Name": ["A", "B", "C", "D", "E", "F"],
                    "Department": ["IT", "HR", "IT", "HR", "Finance", "IT"],
                    "Salary": [30000, 25000, 40000, 35000, 45000, 38000],
                    "Experience": [2, 5, 3, 4, 6, 2]
          })
          print("\n Employees Data : \n\n", df.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 1. Highest Paid Employee Overall
          highest_paid = df.loc[df['Salary'].idxmax()]
          print("Highest paid employee : \n\n", highest_paid)
          
          print("\n-----------------------------------------------------")
          
          # 2. Department with Highest Total Salary
          dept_total = df.groupby('Department')['Salary'].sum()
          highest_dept = dept_total.idxmax()
          print("Department with highest total salary : \n\nn", highest_dept)
          print(dept_total)
          
          print("\n-----------------------------------------------------")
          
          # 3. Employees with Experience > 3 and Salary > 35000
          filtered = df[(df['Experience'] > 3) & (df['Salary'] > 35000)]
          print("Filtered employees:\n\n", filtered)
          
          print("\n-----------------------------------------------------")
          
          # 4. Add Bonus Column - 10% for IT, 5% for others
          df['Bonus'] = df.apply(
                    lambda row: row['Salary'] * 0.10 if row['Department'] == 'IT'
                    else row['Salary'] * 0.05,
                    axis=1
          )
          print("\n After adding Bonus : \n\n", df.to_string())
          
          print("\n-----------------------------------------------------")
          
          # 5. Rank Employees Based on Salary
          df['Rank'] = df['Salary'].rank(ascending=False)
          print("\n Rank Employees Based on Salary : \n\n", df.sort_values("Rank"))
          
          print("\n-----------------------------------------------------")
          
          pivot = pd.pivot_table(
                    df,
                    values="Salary",
                    index="Department",
                    aggfunc="mean"
          )

          print(pivot)

def main():
          # emp_salary()
          # merge_join()
          level_1_practice()
          
if __name__ == "__main__":
          main()
          