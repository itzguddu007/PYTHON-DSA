def calculate_average(student):
    avg_assignment = sum(student["assignment"]) / len(student["assignment"])
    avg_test = sum(student["test"]) / len(student["test"])
    avg_lab = sum(student["lab"]) / len(student["lab"])
    final_score = (0.10 * avg_assignment) + (0.70 * avg_test) + (0.20 * avg_lab)
    return final_score

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_scores(category):
    scores = input(f"Enter {category} scores separated by spaces: ")

    return list(map(float, scores.split()))

def main():
    name = input("Enter student name: ")

    assignment_scores = get_scores("assignment")
    test_scores = get_scores("test")
    lab_scores = get_scores("lab")

    student = {
        "name": name,
        "assignment": assignment_scores,
        "test": test_scores,
        "lab": lab_scores
    }

    avg_score = calculate_average(student)
    grade = assign_grade(avg_score)

    print(f"\nAverage marks of {student['name']} is : {avg_score:.3f}")
    print(f"Letter Grade of {student['name']} is : {grade}")

if __name__ == "__main__":
    main()

