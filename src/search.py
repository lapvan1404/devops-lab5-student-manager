"""
Student Manager — DevOps Lab 5
Module: Search Student
"""

from student import Student


def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo mã hoặc tên."""
    keyword = keyword.lower().strip()

    results = []

    for student in students:
        if (keyword in student.student_id.lower()
                or keyword in student.name.lower()):
            results.append(student)

    return results


if __name__ == "__main__":
    students = [
        Student("dtc235180109", "Nong Van Lap", 22, "K22C"),
        Student("dtc235180096", "Duong Quang Khai", 21, "K22C"),
        Student("dtc235320165", "Lang Thi Khanh Ly", 23, "K22C"),
    ]

    keyword = input("Nhap ma hoac ten sinh vien can tim: ")

    results = search_student(students, keyword)

    if results:
        print("\nKet qua tim kiem:")
        for student in results:
            print(student)
    else:
        print("Khong tim thay sinh vien!")