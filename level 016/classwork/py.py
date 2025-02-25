for i in range(0, 201, 6):
    print(i)
for char in "Goodbye World!":
    print(char)
for i in range(1000, -1, -1):
    print(i)
age = int(input("შეიყვანე ასაკი: "))

if age < 18:
    print("თქვენ მიიღეთ 50% ფასდაკლება!")
else:
    print("ფასდაკლება არ გაქვთ.")
age = int(input("შეიყვანე ასაკი: "))

if age < 18:
    print("თქვენ მიიღეთ 50% ფასდაკლება!")
elif age == 18:
    print("თქვენ მიიღეთ 25% ფასდაკლება!")
else:
    print("ფასდაკლება არ გაქვთ.")
age = int(input("შეიყვანე ასაკი: "))
is_student = input("სტუდენტი ხარ? (დიახ/არა): ").strip().lower()

if age < 18 or is_student == "დიახ":
    print("თქვენ მიიღეთ 50% ფასდაკლება!")
else:
    print("ფასდაკლება არ გაქვთ.")