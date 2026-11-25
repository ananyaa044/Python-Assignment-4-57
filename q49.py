# 49. Create a student marks module and use it to calculate the total and average marks.
from student_marks import total_marks, average_marks, result

marks = [78, 85, 91, 66, 80]
print("Marks:", marks)
print("Total:", total_marks(marks))
print("Average:", average_marks(marks))
print("Result:", result(marks))
