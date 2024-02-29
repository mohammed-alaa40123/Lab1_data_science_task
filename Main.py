users=[]
num =int(input("please enter how many students"))
for i in range(num):
    student_name = input("please enter your name: ")
    student_id = input("please enter your ID :")
    student_age = int(input("please enter student age: ")(
    users.append((student_id, studen_name, student_age))


for i in users:
    print(f"student ID: {users[i][0]}\nstudent name: {users[i][1]}\n age: {users[i][2]}")
