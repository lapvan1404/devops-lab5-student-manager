"""
Student Manager — DevOps Lab 5
Module: Main Application
"""

from student import Student


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("dtc235180109", "Nong Van Lap", 22, "K22C"),
        Student("dtc235180096", "Duong Quang Khai", 21, "K22C"),
        Student("dtc235320165", "Lang Thi Khanh Ly", 23, "K22C"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()