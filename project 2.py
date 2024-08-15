class Course:
    def __init__(self, name, code, duration, level, price, teacher):
        self.name = name
        self.__code = code
        self.__duration = duration
        self.__level = level
        self.__price = price
        self.__teacher = teacher
        self.course_days = []

    def __str__(self):
        return f"{self.name} code:{self.__code} \n teacher: {self.__teacher}\n level: {self.__level}\n duration: {self.__duration}\n course days: {self.course_days}\n price: {self.__price}\n"

    def add_day(self, day):
        self.course_days.append(day)

class Python(Course):
    def __init__(self, name, code, duration, level, price, teacher):
        super().__init__(name, code, duration, level, price, teacher)

class Java(Course):
    def __init__(self, name, code, duration, level, price, teacher):
        super().__init__(name, code, duration, level, price, teacher)

class PHP(Course):
    def __init__(self, name, code, duration, level, price, teacher):
        super().__init__(name, code, duration, level, price, teacher)

py1 = Python("Py1", 1, "Two weeks", "Basic", 100, "Ahmad")
py1.add_day("Sunday")

py2 = Python("Py2", 2, "One month", "Advance", 250, "Ahmad")
py2.add_day("Thursday")

java1 = Java("Java1", 3, "3 days", "Basic", 70, "Ali")
java1.add_day("Monday")

java2 = Java("Java2", 4, "One week", "Advance", 120, "Mohsen")
java2.add_day("Sunday")
java2.add_day("Wednesday")

php1 = PHP("PHP1", 5, "One week", "Basic", 60, "Omid")
php1.add_day("Monday")
php1.add_day("Tuesday")

php2 = PHP("PHP2", 6, "One month", "Advance", 100, "Mehdi")
php2.add_day("Monday")

courses = [py1, py2, java1, java2, php1, php2]
for obj in courses:
    print(obj)