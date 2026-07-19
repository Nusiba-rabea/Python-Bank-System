# # 1. Function to calculate performance bonu
# # def calculate_bonus(base_salary,performance_rating):
# #     if performance_rating==5:
# #         bonus_percentage=0.2   
# #     elif performance_rating==3 or performance_rating==4:
# #         bonus_percentage=0.1
        
# #     elif performance_rating <3:
# #         bonus_percentage=0 
# #     return bonus_percentage*base_salary  
# # #Function to calculate progressive tax deductions
# # def calculate_tax(gross_salary):
# #     if gross_salary>7000:  
# #         taxes=0.15
# #     elif 3000<=gross_salary<=7000:
# #         taxes=0.1
# #     elif gross_salary<3000:
# #         taxes=0.0
# #     return taxes*gross_salary   
# # #3. Core runtime application          
# # def main_hr_app():
# #     print("--- 🏢 Corporate Payroll System 🏢 ---")
# #     employ_name=input("Enter name : ")
# #     department=input("Enter Department: ")
# #     base_salary=float(input("enter your base_salary: "))
# #     performance_rate=int(input("enter your performance rate:"))
# #     if performance_rate < 1 or performance_rate > 5 or base_salary < 0:
# #         print("Invalid input! Please check the salary and performance rating.")
# #         return
# #     bonus= calculate_bonus(base_salary,performance_rate)
# #     gross_salary=base_salary+bonus
# #     tax=calculate_tax(gross_salary)
# #     net_salary=gross_salary-tax
# #     # Output Statement Generator
# #     print("*"*40)
# #     print(f" PAYROLL STATEMENT FOR: {employ_name}")
# #     print(f" Department: {department}")
# #     print("*"*40)
# #     print(f"Base_salary = {base_salary :.2f} EGY")
# #     print(f"Bonus = {bonus: .2f} EGY ")
# #     print(f"Gross_salary = {gross_salary :.2f} EGY")
# #     print(f"Tax Deduction = {tax :.2f} EGY")
# #     print("="*40)
# #     print(f"💰 NET PAYABLE CASH: {net_salary:.2f} EGP")
# #     print("="*40)
# # main_hr_app() 
# import os
# # print(os.getcwd()) 
# print(os.path.abspath(__file__))
# #file=open(r"c:\Users\PowerTech\Desktop\New folder\y.py")
# file=open(r"C:\Users\PowerTech\Desktop\New folder\nusiba.txt","r")
# # print(file.name)
# # print(file.encoding)
# # print(file.mode)
# # print(file.read(5))
# print(file.read())
# file.close()

file=open("Downloads","a")
file.write("nusiba rabee khalf")
file.truncate(4)


