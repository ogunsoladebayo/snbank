from datetime import date, datetime
import random
import os
def searchfunction(username, password):
    a = open('staff.txt', 'r')
    keywords = ['Username: ' + username, 'Password: ' + password]

    for line in a:
        if all(keyword in line for keyword in keywords):
            print('Login Successful... \n Welcome, ' + username)
            complete = True
            break
        else:
            complete = False
    return complete


def createsession(username):
    today = date.today()
    now = datetime.now()
    # create user session in a file
    with open('session.txt', 'w') as a:
        a.write('session started... \n' + username + '\n' + today.strftime('%B %d, %Y') + '\n' + now.strftime('%H:%M:%S'))


def create_account():
    account_name = input('Enter account name: ')
    opening_balance = input('Enter opening balance: ')
    account_type = input('Enter account type: ')
    account_email = input('Enter account email: ')
    # create account number
    account_number = ''
    for index in range(10):
        account_number += str(random.randint(0, 9))
    # save all details in customer.txt
    with open('customer.txt', 'a') as a:
        a.write('Account Number: ' + account_number + ' ' + ', Account Name: ' + account_name + ', Opening Balance: ' + opening_balance + ', Account Type: ' +  account_type + ', Account Email: ' + account_email + '\n')
    return account_number


def check_details(account_number):
    # read customer file
    a = open('customer.txt', 'r')
    # do some searchings

    for line in a:
        if ('Account Number: ' + account_number in line):
            details = line
        else:
            details = 'No details found'
    return details


def delete_session():
    os.unlink('session.txt')
    print('You have logged out')


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
                createsession(username)
                staff_in_session = True
                while staff_in_session:
                    staff_option = input('Press: \n 1 to Create new bank account \n 2 to Check Account Details \n 3 to Logout \n Input: ')
                    if staff_option == '1' or staff_option == '2' or staff_option == '3':
                        if staff_option == '1':
                            account_number = create_account()
                            print ('A new account has been created. The customer account number is ' + account_number)

                        elif staff_option == '2':
                            account_number = input('Enter customer account number: ') + ' '
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