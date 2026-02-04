def Student_Grade_Calculator(marks_1, marks_2, marks_3, marks_4, marks_5):

    # Calculating the vd of the marks
    avg = (marks_1 + marks_2 + marks_3 + marks_4 + marks_5) / 5

    # print(f"Average: {avg}")

    # Conditioning the grade based on Average marks
    if avg >= 90:
        return "A+"

    elif avg >= 75:
        return "A"

    elif avg >= 60:
        return "B"

    elif avg >= 50:
        return "C"

    else:
        return "Fail"


if __name__ == "__main__":
    marks_1 = float(input("Enter the 1st subject marks out of 100: "))
    marks_2 = float(input("Enter the 2nd subject marks out of 100: "))
    marks_3 = float(input("Enter the 3rd subject marks out of 100: "))
    marks_4 = float(input("Enter the 4th subject marks out of 100: "))
    marks_5 = float(input("Enter the 5th subject marks out of 100: "))

    print(Student_Grade_Calculator(marks_1, marks_2, marks_3, marks_4, marks_5))
