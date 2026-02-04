from src.Student_Grade_Calculator import Student_Grade_Calculator


def test_Student_Grade_Calculator():

    # test cases

    assert Student_Grade_Calculator(70, 80, 90, 100, 50) == "A"

    assert Student_Grade_Calculator(70, 80, 90, 100, 50) == "B"


# print(test_Student_Grade_Calculator())
