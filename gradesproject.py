# create a program for grades input with the following
#    80-100 -A
#    60-79 -B
#    50-59 -C
#    30-49 -D
#    Below 30- Fail
#   negative and above 100- invalid input

grade = int(input("Enter marks:"))

if grade>79 and grade<101:
    print("A")
elif grade>59 and grade<80:
    print("B")
elif grade>49 and grade<60:
    print("C")
elif grade>29 and grade<50:
    print("D")
elif grade<30 and grade>0:
    print("Fail")
elif grade<1 and grade>100:
    print("Invalid")