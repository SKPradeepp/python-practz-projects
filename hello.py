def avg(a, b, c):
    return (a + b + c) / 3
name = input("Name: ")
a=float(input("Tamil: "))
b=float(input("English: ")) 
c=float(input("Maths: "))
average = avg(a, b, c)
print("Student:", name)
print("Average: ", average)
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")