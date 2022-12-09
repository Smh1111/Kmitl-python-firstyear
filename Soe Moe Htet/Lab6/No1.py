from tokenize import String


def grade_Checking(marks):
    if(marks < 0 or marks > 100):
        print("Error")
    
    elif(marks >=80 and marks <= 100):
        print("A")
    elif(marks >= 70 and marks < 80):
        print("B")
    elif(marks >= 60 and marks < 70):
        print("C")
    elif(marks >= 50 and marks < 60):
        print("D")
    elif(marks < 50):
        print("F")

    

def main():
    grade_Checking(69)
main()