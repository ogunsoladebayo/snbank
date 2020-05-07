def searchfunction(username, password):
    if username == 'admin' and password == 'admin':
    # search in staff.txt and set complete to true if found
        complete = True
    else:
        complete = False
    return complete


def createsession():
    # create user session in a file
    print ('session created')


def create_account():
    account_name = input('Enter account name: ')
    opening_balance = input('Enter opening balance: ')
    account_type = input('Enter account type: ')
    account_email = input('Enter account email: ')
    # create account number
    # save all details in customer.txt
    account_number = account_name + opening_balance + account_type + account_email
    return account_number


def check_details(account_number):
    if account_number == 'found':
        details = account_number
    # do some searchings
    else:
        details = 'No details found'
    return details #probably in an array if found


def delete_session():
    print('session deleted')


apprunning = True
while apprunning:

    welcome = input('Press: \n 1 for Staff Login \n 2 to Close App \n Input: ')
    if welcome == '1':
        staffverify = False

        while staffverify == False:
            username = input ('Please enter your staff Username: ')
            password = input ('Enter your Password: ')
            
            # call function to search collected username and password and return true
            if searchfunction(username, password) == True:
                staffverify = True
                # continue to next step
                createsession()
                staff_in_session = True
                while staff_in_session:
                    staff_option = input('Press: \n 1 to Create new bank account \n 2 to Check Account Details \n 3 to Logout \n Input: ')
                    if staff_option == '1' or staff_option == '2' or staff_option == '3':
                        if staff_option == '1':
                            account_number = create_account()
                            print ('A new account has been created. The customer account number is ' + account_number)

                        elif staff_option == '2':
                            account_number = input('Enter customer account number: ')
                            customer_details = check_details(account_number)
                            print ('Customer details: ' + customer_details)
                        
                        elif staff_option == '3':
                            delete_session()
                            staff_in_session = False
                            
                    else:
                        print('You have entered an invalid option')

            else:
                print ('Username or Password is incorrect')
                # pass goes back to search user
                pass

    elif welcome == '2':
        apprunning = False
    else:
        print ('You have entered an incorrect option')