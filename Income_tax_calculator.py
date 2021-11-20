# This project is made by Karanveer Singh (12006560), Sourav(12013365) and Murli Manohar(12019400)
# The line count difference in this repository project and report screenshots is because these two comments have been added later

name=input('''Hello, this is an income tax calculator.
Please enter your name: ''')
age=int(input("Please enter your age: "))

income=int(input("Please enter your annual income: "))
taxableIncome=income
tax=0
cess=0

#if the person has taken a home loan, the interest paid on the home loan can be deducted from total income
homeLoan=input("Do you have a home loan? Press 'y' for yes or 'n' for no: ")
if(homeLoan== 'y'):
    LoanInterest=int(input("Please enter the amount of interest you pay annually: "))
    if(LoanInterest<=200000):
        LoanInterest=LoanInterest
    else:
        LoanInterest=200000
    LoanPrincipal=int(input("Please enter the principal amount you pay annually: "))
    if(LoanPrincipal<=150000):
        LoanPrincipal=LoanPrincipal
    else:
        LoanPrincipal=150000
else:
    LoanInterest=0
    LoanPrincipal=0
taxableIncome=income-LoanInterest- LoanPrincipal

#If the person has medical insurance, it can be used to reduce taxable income further. We are adding the option
#How much taxable income can be reduced by insurance, it depends upon age of th person and his parents(if insured)
Insurance=input("Do you have medical insurance? Press 'y' for yes or 'n' for no: ")
if(Insurance=='y'):
    P_insurance=input("Do you have also covered your parents under medical insurance? Press 'y' for yes or 'n' for no: ")
    if(P_insurance=='y'):          # Medical insurance of a person's parents can also reduce taxable income
        P_age=int(input("Enter the age of your eldest parent: "))       
        if(age<=60 and P_age<=60):
            InsuranceCost=int(input(("Please enter the cost of your insurance annually: ")))
            if InsuranceCost<=50000:
                InsuranceCost=InsuranceCost
            else:
                InsuranceCost=50000
        elif (age<=60 and P_age>60):
            InsuranceCost=int(input(("Please enter the cost of your insurance: ")))
            if InsuranceCost<=75000:
                InsuranceCost=InsuranceCost
            else:
                InsuranceCost=75000
        elif (age>60 and P_age>60):
            InsuranceCost=int(input(("Please enter the cost of your insurance: ")))
            if InsuranceCost<=100000:
                InsuranceCost=InsuranceCost
            else:
                InsuranceCost=100000
    else:
        if(age<=60):
            InsuranceCost=int(input("Please enter the cost of your insurance: "))
            if InsuranceCost<=25000:
                InsuranceCost=InsuranceCost
            else:
                InsuranceCost=25000
        else:
            InsuranceCost=int(input("Please enter the cost of your insurance: "))
            if InsuranceCost<=50000:
                InsuranceCost=InsuranceCost
            else:
                InsuranceCost=50000
else:
    InsuranceCost=0
taxableIncome=taxableIncome-InsuranceCost

# Starting income tax calculations now

if(taxableIncome<=250000):
    tax=0
elif taxableIncome<=500000:
    tax=(taxableIncome-250000)*0.05
elif taxableIncome<=750000:
    tax=12500+(taxableIncome-500000)*0.10
elif taxableIncome<=1000000:
    tax=37500+(taxableIncome-750000)*0.15    
elif taxableIncome<=1250000:
    tax=75000+(taxableIncome-1000000)*0.20
elif taxableIncome<=1500000:
    tax=125000+(taxableIncome-250000)*0.25
elif taxableIncome>1500000:
    tax=187500+(taxableIncome-250000)*0.30
cess=tax*0.04
ttax=tax + cess

print("Hello ", name+",",
  "Your total taxable income is " ,"Rs", taxableIncome)
print("Income tax: ", tax)
print("Health and education cess: ","Rs",cess)
print("Total Income tax: ","Rs",ttax)