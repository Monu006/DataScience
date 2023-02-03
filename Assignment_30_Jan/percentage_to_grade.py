# Write a program to accept percentage from the user and display the grade according to the following


marks = int(input("Enter your percentage:\n"))
if marks > 90:
    print("Congrats!! You got 'A' Grade:")
elif (marks <= 90 and marks >80):
    print("Excellent!! You got 'B' Grade:")
elif (marks>=60 and marks<=80):
    print("Good! You got 'C' Grade:")
elif (marks<60):
    print("Do Hard work! you got 'D' Grade")
else:
    print('Seems Invalid Input!!')
    print('Changes made in code')


