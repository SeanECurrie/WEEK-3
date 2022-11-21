##########- ROI CALCULATOR WEEKEND PROJECT -##########
import sys

def roi_input(msg, error_msg):
    while True:

        
        try:
            user_input = input(msg)
            if user_input == 'q':
                sys.exit('\nThanks for stopping by\n')
            num = float(user_input)
           
            
            return num
        except ValueError:
            print(error_msg)
            continue
        
def info_input():
    default_error_message = '\nSorry, I didn\'t understand that. Please enter a valid number.\n'
    
    print('\n\nOk, let\'s get started with INCOME from your possible new property: ')
    print('Enter \'q\' at anytime to QUIT the calculator.\n')
    rental_income = roi_input('Please enter your expected RENTAL INCOME: ', default_error_message)
    storage = roi_input('Will you be charging for STORAGE spaces? If so, how much a month: ', default_error_message)
    laundry = roi_input('Does your rental property have money making LAUNDRY machines? If so, how much monthly income do you expect: ', default_error_message)
    misc_income = roi_input('If you can think of any other rental income please enter the expected monthly number now: ', default_error_message)

    print('\n\nOk, let\'s talk about EXPENSES: \n')
    property_tax = roi_input('Enter your monthly PROPERTY TAX: ', default_error_message)
    property_insurance = roi_input('Enter your monthly INSURANCE PAYMENT: ', default_error_message)
    property_util = roi_input('Please enter the amount of UTILITY bills you will be responsible for each month: ', default_error_message)
    property_HOA = roi_input('Please enter the amount per month of the HOA payment, if any: ', default_error_message)
    property_repairs = roi_input('Please enter the amount you will put aside for REPAIRS, if any: ', default_error_message)
    property_CapEx = roi_input('Please enter the amount you will put aside a month for CAPITAL EXPENSES, if any: ', default_error_message)
    property_prop_manage = roi_input('Please enter the amount of monthly PROPERTY MANAGEMENT payments, if any: ', default_error_message)
    property_mortage = roi_input('And finally, please enter your monthly MORTAGE payment: ', default_error_message)

    print('\n\nOk, we are almost there. Now for your Cash on Cash ROI information. If there were no costs for a certain questions, please enter 0.\n')
    property_down_payment = roi_input('Please enter your DOWN PAYMENT: ', default_error_message)
    property_closing = roi_input('Please enter your CLOSING costs: ', default_error_message)
    property_rehab = roi_input('Please enter your REHAB costs: ', default_error_message)
    misc_costs = roi_input('Please enter any OTHER costs: ', default_error_message)

    income = rental_income + storage + laundry + misc_income
    expenses = property_tax + property_insurance + property_HOA + property_util + property_repairs + property_CapEx + property_prop_manage + property_mortage
    total_investment = property_down_payment + property_closing + property_rehab + misc_costs
    mcf = income - expenses
    annual_mcf = mcf * 12
    ROI = annual_mcf / total_investment
    print(f'\n\nHere is some useful information about your potential property and how we got to your ROI:\n\nTotal Income: ${income}\nTotal Expenses: ${expenses}\nMonthly Cash Flow: ${mcf}\nAnnual Cash Flow: ${annual_mcf}\nTotal Investment: ${total_investment}')  
    print(f'\nHere is your expected RETURN ON INVESTMENT: {int(ROI*100)}%\n') 
    print('\nTHANK YOU for using the THIEVES 105 ROI !\nGood luck with your new investment!\n')
    
while True:
    print("\n ------Welcome to the THIEVES 105 Rental Property ROI Calculator------\n\n")
    
    user_choice = input("Are you ready to make some money? [Y]es or [NO] ").lower()
    
    if user_choice == 'y':
        info_input()
        break
    elif user_choice == 'n':
        print("\nOk, too bad!\n")
        break
    else:
        print('\nPlease type Y or N\n')     
        
        

