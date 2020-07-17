Q1 = """1.What is output of 33 == 33.0
a - False
b - True
c - 33
d - None of the above"""

Q2 ="""2.What is output for − b = [11,13,15,17,19,21]
print(b[::2])
a - [19,21]
b - [11,15]
c - [11,15,19]
d - [13,17,21]"""

Q3 ="""3.Which operator is right-associative?
a - *
b - =
c - +
d - %"""

Q4 ="""4.Which module is used in python to create Graphics?
a - Turtle
b - Canvas
c - Tkinter
d - Graphics"""

Q5 ="""5.Suppose we are given with two sets(s1&s2) then what is the output of the code − S1 + S2 
a - Adds the elements of the both the sets.
b - Removes the repeating elements and adds both the sets.
c - It is an illegal command.
d - Output will be stored in S1."""

questions={Q1:"b",Q2:"c",Q3:"b",Q4:"a",Q5:"c"}

name=input("Enter your name:")
print("Hello",name,",Welcome to the quiz world")

score=0
for i in questions:
    print(i)
    ans=input("Enter the Answer (a/b/c/d):")
    if ans==questions[i]:
        print("Correct answer,you got 1 point")
        score+=1
        print("Your current score is,", score)
    else:
        print("Wrong answer,you lost 1 point")
        score-=1
        print("Your current score is,",score)
print("Final score is:",score)

print("Suggestions:")
if(score==5):
    print("Excellent,Keep going")
elif(score==4):
    print("Good job")
else:
    print("Could've been done Good,Give another try")