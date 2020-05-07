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
            break
        else:
            details = 'No details found'
    return details


def delete_session():
    os.unlink('session.txt')
    print('You have logged out')

