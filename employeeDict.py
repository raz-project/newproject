

data ={
    "company": "TechCorp",
    "employees": [
      {
        "id": 1,
        "name": "Alice",
        "department": "Engineering",
        "projects": [
          {"project_id": 101, "name": "Project A", "hours_spent": 120},
          {"project_id": 102, "name": "Project B", "hours_spent": 90}
        ],
        "skills": ["Python", "Django", "AWS"]
      },
      {
        "id": 2,
        "name": "Bob",
        "department": "Marketing",
        "projects": [
          {"project_id": 103, "name": "Project C", "hours_spent": 40}
        ],
        "skills": ["SEO", "Content Writing"]
      },
      {
        "id": 3,
        "name": "Charlie",
        "department": "Engineering",
        "projects": [
          {"project_id": 104, "name": "Project D", "hours_spent": 200},
          {"project_id": 105, "name": "Project E", "hours_spent": 50}
        ],
        "skills": ["Java", "Spring", "Docker"]
      }
    ]
  }

print("-----------------------------------------------------------------------------------------------------------")

for company  in data.items():
    companyName  = data.get("company")
    print(companyName)
    break

print("-----------------------------------------------------------------------------------------------------------")

for employee in data["employees"]:
    total=0
    name = employee.get("name")
    for project in employee.get("projects", []):
        hours_spent = project.get("hours_spent")
        total += hours_spent
    print(f"Employee: {name}, Total Hours Spent:{total}")
    total =0

print("-----------------------------------------------------------------------------------------------------------")

department_hours = {}

for employee in data["employees"]:
    department = employee.get("department")
    total_hours = sum(project.get("hours_spent", 0) for project in employee.get("projects", []))
    department_hours[department] = department_hours.get(department, 0) + total_hours


highest_department = max(department_hours, key=department_hours.get)
highest_hours = department_hours[highest_department]

print(f"The department with the highest hours spent on projects is {highest_department} with {highest_hours} hours")

print("-----------------------------------------------------------------------------------------------------------")

for employee in data["employees"]:
    if "Python" in employee.get("skills", []):
        print(f"Employee with the skill Python: {employee['name']}")

print("-----------------------------------------------------------------------------------------------------------")

for employee in data["employees"]:
    total_hours = sum(project.get("hours_spent", 0)
      for project in employee.get("projects", []))
    if total_hours > 100:
        print(f"Employee: {employee["name"]}, worked over 100 hours")