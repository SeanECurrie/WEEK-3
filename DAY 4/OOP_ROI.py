

def info_input():

    
        print('\n\nOk, let\'s get started with INCOME from your possible new property: \n')

        while True:
            try:
                rental_income = float(input('Please enter your expected RENTAL INCOME: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break
        while True:
            try:
                storage = float(input('Will you be charging for STORAGE spaces? If so, how much a month: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break
        while True:
            try:
                laundry = float(input('Does your rental property have money making LAUNDRY machines? If so, how much monthly income do you expect: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break
        while True:
            try:
                misc_income = float(input('If you can think of any other rental income please enter the expected monthly number now: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break
        
        print('\n\nOk, let\'s talk about EXPENSES: \n')

        while True:
            try:
                property_tax = float(input('Enter your monthly PROPERTY TAX: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_insurance = float(input('Enter your monthly INSURANCE PAYMENT: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_util = float(input('Please enter the amount of UTILITY bills you will be responsible for each month: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_HOA = float(input('Please enter the amount per month of the HOA payment, if any: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_repairs = float(input('Please enter the amount you will put aside for REPAIRS, if any: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_CapEx = float(input('Please enter the amount you will put aside a month for CAPITAL EXPENSES, if any: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_prop_manage = float(input('Please enter the amount of monthly PROPERTY MANAGEMENT payments, if any: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_mortage = float(input('And finally, please enter your monthly MORTAGE payment: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break


        print('\n\nOk, we are almost there. Now for your Cash on Cash ROI information. If there were no costs for a certain questions, please enter 0.\n')

        while True:
            try:
                property_down_payment = float(input('Please enter your DOWN PAYMENT:  '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_closing = float(input('Please enter your CLOSING costs: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                property_rehab = float(input('Please enter your REHAB costs: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break

        while True:
            try:
                misc_costs = float(input('Please enter any OTHER costs: '))
            except ValueError:
                print("\nSorry, I didn't understand that.\n")
                continue
            else:
                break
  
        
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


        
        
        

