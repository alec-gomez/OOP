import StudentClass as sc


stu_id = 1001
name = "John"
birth = "10/11/2001"
classification = "junior"

student1 = sc.StudentClass(stu_id, name, birth, classification)

student1.calc_age()
student1.calc_register()

print(f"Student age is: {student1.get_age()}")
print(f"Student can register between {student1.get_register()}")
