# # # # Write a function to take in a sentence and assign a numeric value to each letter.
# # # # No two letters should have the same numeric value, and each letter should have a
# # # # dedicated value (so that the same letter does not have two numeric values).

# # # def ranking(sentence):
# # #     number = {}
# # #     indi = []
# # #     z = 0
# # #     for i in sentence:
# # #         if i.

# # # import re

# # # with open('regex_test.txt') as f:
# # #     data = f.read()
# # #     print(data)

# # # pattern = re.compile(r"^([A-Z]([a-z]+|.)\s*){2,3}$")    
# # # match = pattern.findall(data)

# # # print(match)


# # # Week 3: Day 3 - Whiteboard

# # # Fizz Buzz
# # # Write a function to that takes one parameter
# # # If the number is divisible by 3, print 'Fizz' instead of the number
# # # If the number is divisible 5, print 'Buzz' instead of the number
# # # If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# # # Otherwise, simply print the number

# # # def fizz_buzz(input):
# # #     if input % 3 == 0 and input % 5 == 0:
# # #         print("FizzBuzz")
# # #         return
# # #     if input % 3 == 0:
# # #         print("Fizz")

# # #     elif input % 5 == 00:
# # #         print("Buzz")

# # #     else:
# # #         print(input)

# # # fizz_buzz(22)


# # # Python3 program to
# # # Check if the string is pangram

  
# # def ispangram(str):
# #     alphabet = "abcdefghijklmnopqrstuvwxyz"
# #     for char in alphabet:
# #         if char not in str.lower():
# #             return False
  
# #     return True
      
# # # Driver code
# # string = 'the quick brown fox jumps over the lazy dog'
# # if(ispangram(string) == True):
# #     print("Yes")
# # else:
# #     print("No")



# # Given a string s consisting of words and spaces, return the length of the last word in the string.

# # A word is a maximal substring consisting of non-space characters only.

 

# # Example 1:

# # Input: s = "Hello World"
# # Output: 5
# # Explanation: The last word is "World" with length 5.
# # Example 2:

# # Input: s = "   fly me   to   the moon  "
# # Output: 4
# # Explanation: The last word is "moon" with length 4.
# # Example 3:

# # Input: s = "luffy is still joyboy"
# # Output: 6
# # Explanation: The last word is "joyboy" with length 6.
# #import re
# # s = "   fly me   to   the moon  "

# # pattern = re.search(r'[a-zA-Z]')

# # match =print(pattern.string)

# # print (match)

# # def last_length(str):
# #     str_arr = str.split()
# #     return len(str_arr[-1])








# # #input :[8,5,2,9,5,6,3]

# # lst = ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST']
# # lst2 = []
# # def bubble_sort(lst):
# #     lst2 = []
# #     isSorted = False
# #     while not isSorted:
# #         isSorted = True
# #         for idx in range(len(lst)-1):
# #             if lst[idx] == 'NORTH' and lst[idx+1] == 'SOUTH' or lst[idx] == 'EAST' and lst[idx+1] == 'WEST':
                
# #                 del lst[idx+1] 
            
# #                 isSorted = False
# #     return lst
                
            
                               

                
        
   

# # bubble_sort(lst)
# # print(lst)
# # print(lst2)
# text = "Hi there"
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# myfont = ImageFont.truetype("verdanab.ttf", 12)
# size = myfont.getsize(text)
# img = Image.new("1",size,"black")
# draw = ImageDraw.Draw(img)
# draw.text((0, 0), text, "white", font=myfont)
# pixels = np.array(img, dtype=np.uint8)
# chars = np.array([' ','#'], dtype="U1")[pixels]
# strings = chars.view('U' + str(chars.shape[1])).flatten()
# print( "\n".join(strings))




#-------------------ROI CALC------------
# import sys

# def roi_input(msg, error_msg):
#     while True:

        
#         try:
#             user_input = input(msg)
#             if user_input == 'q':
#                 sys.exit('\nThanks for stopping by\n')
#             num = float(user_input)
           
            
#             return num
#         except ValueError:
#             print(error_msg)
#             continue
        
# def info_input():
#     default_error_message = '\nSorry, I didn\'t understand that. Please enter a valid number.\n'
    
#     print('\n\nOk, let\'s get started with INCOME from your possible new property: ')
#     print('Enter \'q\' at anytime to QUIT the calculator.\n')
#     rental_income = roi_input('Please enter your expected RENTAL INCOME: ', default_error_message)
#     storage = roi_input('Will you be charging for STORAGE spaces? If so, how much a month: ', default_error_message)
#     laundry = roi_input('Does your rental property have money making LAUNDRY machines? If so, how much monthly income do you expect: ', default_error_message)
#     misc_income = roi_input('If you can think of any other rental income please enter the expected monthly number now: ', default_error_message)

#     print('\n\nOk, let\'s talk about EXPENSES: \n')
#     property_tax = roi_input('Enter your monthly PROPERTY TAX: ', default_error_message)
#     property_insurance = roi_input('Enter your monthly INSURANCE PAYMENT: ', default_error_message)
#     property_util = roi_input('Please enter the amount of UTILITY bills you will be responsible for each month: ', default_error_message)
#     property_HOA = roi_input('Please enter the amount per month of the HOA payment, if any: ', default_error_message)
#     property_repairs = roi_input('Please enter the amount you will put aside for REPAIRS, if any: ', default_error_message)
#     property_CapEx = roi_input('Please enter the amount you will put aside a month for CAPITAL EXPENSES, if any: ', default_error_message)
#     property_prop_manage = roi_input('Please enter the amount of monthly PROPERTY MANAGEMENT payments, if any: ', default_error_message)
#     property_mortage = roi_input('And finally, please enter your monthly MORTAGE payment: ', default_error_message)

#     print('\n\nOk, we are almost there. Now for your Cash on Cash ROI information. If there were no costs for a certain questions, please enter 0.\n')
#     property_down_payment = roi_input('Please enter your DOWN PAYMENT: ', default_error_message)
#     property_closing = roi_input('Please enter your CLOSING costs: ', default_error_message)
#     property_rehab = roi_input('Please enter your REHAB costs: ', default_error_message)
#     misc_costs = roi_input('Please enter any OTHER costs: ', default_error_message)

#     income = rental_income + storage + laundry + misc_income
#     expenses = property_tax + property_insurance + property_HOA + property_util + property_repairs + property_CapEx + property_prop_manage + property_mortage
#     total_investment = property_down_payment + property_closing + property_rehab + misc_costs
#     mcf = income - expenses
#     annual_mcf = mcf * 12
#     ROI = annual_mcf / total_investment
#     print(f'\n\nHere is some useful information about your potential property and how we got to your ROI:\n\nTotal Income: ${income}\nTotal Expenses: ${expenses}\nMonthly Cash Flow: ${mcf}\nAnnual Cash Flow: ${annual_mcf}\nTotal Investment: ${total_investment}')  
#     print(f'\nHere is your expected RETURN ON INVESTMENT: {int(ROI*100)}%\n') 
#     print('\nTHANK YOU for using the THIEVES 105 ROI !\nGood luck with your new investment!\n')
    
# while True:
#     print("\n ------Welcome to the THIEVES 105 Rental Property ROI Calculator------\n\n")
    
#     user_choice = input("Are you ready to make some money? [Y]es or [NO] ").lower()
    
#     if user_choice == 'y':
#         info_input()
#         break
#     elif user_choice == 'n':
#         print("\nOk, too bad!\n")
#         break
#     else:
#         print('\nPlease type Y or N\n')

##########- ASCII TABLE -##########

# importing required library
from prettytable import PrettyTable
  
# creating an empty PrettyTable
x = PrettyTable()
  
# adding data into the table
# row by row
income= 1000
expenses= 1000
mcf= 1000
annual_mcf = 1000
total_investment = 1000
x.field_names = ["Total Income", "Total Expenses", "Monthly Cash Flow", "Annual Cash Flow", "Total Investment"]
x.add_row([income, expenses, mcf, annual_mcf, total_investment])

  
# printing generated table
print(x)















# #------------------- FIRST ROI CALC ATTEMPT----------------
# import sys

# def roi_input(msg):
    
#     try:
#         user_input = float(input(msg))
#     except ValueError:
#         if msg == 'q':
#             sys.exit('Thanks for coming.')
#         else:   
#             print("\nSorry, I didn't understand that.\n")
        
            
#     return user_input


# def info_input():

    
#         print('\n\nOk, let\'s get started with INCOME from your possible new property: \n')
#         default_error_message = '\nSorry, I didn\'t understand that.'
#         while True:
            
#             try:
#                 rental_income = float(input('Please enter your expected RENTAL INCOME: '))
                

                
#             except ValueError:
                
#                 print("\nSorry, I didn't understand that. Please enter a number to proceed.\n")
#                 continue
            

#             else:
#                 break
#         while True:
#             try:
#                 storage = float(input('Will you be charging for STORAGE spaces? If so, how much a month: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break
#         while True:
#             try:
#                 laundry = roi_input('Does your rental property have money making LAUNDRY machines? If so, how much monthly income do you expect: ')
                
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break
#         while True:
#             try:
#                 misc_income = float(input('If you can think of any other rental income please enter the expected monthly number now: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break
        
#         print('\n\nOk, let\'s talk about EXPENSES: \n')

#         while True:
#             try:
#                 property_tax = float(input('Enter your monthly PROPERTY TAX: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_insurance = float(input('Enter your monthly INSURANCE PAYMENT: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_util = float(input('Please enter the amount of UTILITY bills you will be responsible for each month: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_HOA = float(input('Please enter the amount per month of the HOA payment, if any: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_repairs = float(input('Please enter the amount you will put aside for REPAIRS, if any: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_CapEx = float(input('Please enter the amount you will put aside a month for CAPITAL EXPENSES, if any: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_prop_manage = float(input('Please enter the amount of monthly PROPERTY MANAGEMENT payments, if any: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_mortage = float(input('And finally, please enter your monthly MORTAGE payment: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break


#         print('\n\nOk, we are almost there. Now for your Cash on Cash ROI information. If there were no costs for a certain questions, please enter 0.\n')

#         while True:
#             try:
#                 property_down_payment = float(input('Please enter your DOWN PAYMENT:  '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_closing = float(input('Please enter your CLOSING costs: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 property_rehab = float(input('Please enter your REHAB costs: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break

#         while True:
#             try:
#                 misc_costs = float(input('Please enter any OTHER costs: '))
#             except ValueError:
#                 print("\nSorry, I didn't understand that.\n")
#                 continue
#             else:
#                 break
  
        
#         income = rental_income + storage + laundry + misc_income
#         expenses = property_tax + property_insurance + property_HOA + property_util + property_repairs + property_CapEx + property_prop_manage + property_mortage
#         total_investment = property_down_payment + property_closing + property_rehab + misc_costs

#         mcf = income - expenses
#         annual_mcf = mcf * 12
#         ROI = annual_mcf / total_investment
#         print(f'\n\nHere is some useful information about your potential property and how we got to your ROI:\n\nTotal Income: ${income}\nTotal Expenses: ${expenses}\nMonthly Cash Flow: ${mcf}\nAnnual Cash Flow: ${annual_mcf}\nTotal Investment: ${total_investment}')  
#         print(f'\nHere is your expected RETURN ON INVESTMENT: {int(ROI*100)}%\n') 
#         print('\nTHANK YOU for using the THIEVES 105 ROI !\nGood luck with your new investment!\n')
        


# while True:
#     print("\n ------Welcome to the THIEVES 105 Rental Property ROI Calculator------\n\n")
    
#     user_choice = input("Are you ready to make some money? [Y]es or [NO] ").lower()
    
#     if user_choice == 'y':
#         info_input()
#         break
#     elif user_choice == 'n':
#         print("\nOk, too bad!\n")
#         break
#     else:
#         print('\nPlease type Y or N\n')