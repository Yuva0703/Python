class SubfieldsInAI():
    def SubFieldsInAIF():
        subFields=('Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing')
        for items in subFields:
            print(items)

class OddEven():
    def CheckEvenorOdd():
        Num=int(input())
        if(Num%2==0):
            print("Even")
        else:
            print("Odd")

class CheckEligibility():
    def check_marriage_eligibility():
        age=int(input())
        gender=input()
        if gender.lower() == "male":
            if age >= 21:
                return "Eligible for marriage."
            else:
                return "Not eligible for marriage. Minimum age is 21."
        elif gender.lower() == "female":
            if age >= 18:
                return "Eligible for marriage."
            else:
                return "Not eligible for marriage. Minimum age is 18."



class percentage():
    def calculate_percentage():
        Sub1=int(input())
        Sub2=int(input())
        Sub3=int(input())
        Sub4=int(input())
        Sub5=int(input())
        obtained_marks=int(input())
        total_marks=(500)
        percentage=(obtained_marks / total_marks) * 100
        print(percentage)
    