"""Student marks calculations used by q49.py."""

def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    if not marks:
        raise ValueError("At least one mark is required")
    return total_marks(marks) / len(marks)

def result(marks, passing_mark=40):
    return "Pass" if marks and all(mark >= passing_mark for mark in marks) else "Fail"
