class Mobile:
    def __init__(self):
        self.__pin = 27102004
        self.__photos = ["img1", "img2"]
        self.__docs = ["doc1", "doc2", "doc3", "doc4"]
        self.__is_unlocked = False

    def lock(self, current_pin):
        if self.__pin == current_pin:
            self.__is_unlocked = True
            print("All apps visible")
        else:
            print("Entered wrong password")

    def show_photos(self):
        if self.__is_unlocked:
            print("Photos:", self.__photos)
        else:
            print("Access denied. Please unlock the phone first.")

    def show_docs(self):
        if self.__is_unlocked:
            print("Documents:", self.__docs)
        else:
            print("Access denied. Please unlock the phone first.")


# Object creation and method calls
a = Mobile()
c_pin = int(input("Enter pin: "))
a.lock(c_pin)

# Try accessing photos and docs
a.show_photos()
a.show_docs()




class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name            # private variable
        self.__roll_no = roll_no      # private variable
        self.__marks = marks          # private variable

    # Public method to get student details
    def get_details(self):
        return f"Name: {self.__name}, Roll No: {self.__roll_no}, Marks: {self.__marks}"

    # Public method to update marks
    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks. Must be between 0 and 100.")

    # Public method to get marks
    def get_marks(self):
        return self.__marks

# ------------------------------
# Usage
student1 = Student("Chiran", "CSE101", 88)
print(student1.get_details())

student1.update_marks(93)
print("Updated Marks:", student1.get_marks())


