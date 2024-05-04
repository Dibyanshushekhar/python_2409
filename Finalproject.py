import random

def create_checklist(students, start_year, end_year, age_limit, required_skills):
    checklist = []
    for student in students:
        if (start_year <= student['year_of_completion'] <= end_year and
            student['cgpa'] > 7.5 and
            student['age'] <= age_limit and
            all(skill in student['skills'] for skill in required_skills)):
            checklist.append(student)
    return checklist

def main():
    students = []
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        name = input("Enter student name: ")
        degree = input("Enter student degree (Engineering/Degree): ")
        programming_language = input("Enter programming language: ")
        year_of_completion = int(input("Enter year of completion: "))
        cgpa = float(input("Enter CGPA: "))
        age = int(input("Enter student age: "))
        skills = input("Enter student skills (comma-separated): ").split(',')
        student_data = {'name': name, 'degree': degree, 'programming_language': programming_language,
                        'year_of_completion': year_of_completion, 'cgpa': cgpa, 'age': age, 'skills': skills}
        students.append(student_data)

    start_year = random.randint(2000, 2020)
    end_year = random.randint(start_year, 2024)  # Ensure end year is after start year
    age_limit = int(input("Enter maximum age limit for students: "))
    required_skills = input("Enter required skills (comma-separated): ").split(',')

    checklist = create_checklist(students, start_year, end_year, age_limit, required_skills)

    print("\nChecklist for students who completed their degree/engineering with more than a 7.5 CGPA between", start_year, "and", end_year)
    print("------------------------------------------------------------------------------")
    print("Name\t\t\tDegree\t\t\tProgramming Language\t\tYear of Completion\t\tCGPA\t\tAge\t\tSkills")
    print("------------------------------------------------------------------------------")
    for student in checklist:
        print(f"{student['name']}\t\t{student['degree']}\t\t{student['programming_language']}\t\t\t{student['year_of_completion']}\t\t\t{student['cgpa']}\t\t{student['age']}\t\t{', '.join(student['skills'])}")

if __name__ == "__main__":
    main()
