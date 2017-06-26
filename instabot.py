# Request library allows to send HTTP request
import requests

# App access token is imported from key file. it can also be created here!
from keys import APP_ACCESS_TOKEN

# term color module is used to import color to some string so as to increase readability
from termcolor import *
import colorama
colorama.init()

# We have BASE URL in gloal variable whose lifetime is runtme of the program
BASE_URL = 'https://api.instagram.com/v1/'


# Function declaration to get your own info
def self_info():

    # here user/self is the path for the functionality and access toke is the query string
    request_url = (BASE_URL + 'users/self/?access_token=%s') % APP_ACCESS_TOKEN

    # this will print the request url
    print 'GET request url : %s' % request_url

    # .json is used while handling json data .it act as a json decoder.
    user_info = requests.get(request_url).json()

    # jsn objects received are displayed in this format which is done by using concept of string formatting.
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


# Function declaration to get the ID of a user by username
# Which takes the Instagram username as an input and returns the user ID of the user.
def get_user_id(insta_username):
    request_url = (BASE_URL + 'user'
                              's/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    # len function checks if the length of data is invalid or not i.e nuLL or not null
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


# Function declaration to get the info of a user by username
# which takes the instagram username as input and returns the information of the user.
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):

            # here string formatting is done to increase readability which is the zen of python
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'

# here we have defined the start bot function which will start or bot application
def start_bot():

    # while loop in python is used to repeatedly execute a set a target statements as listed below
    while True:
        print '\n'
        # C print is used for colored printing of a string
        cprint ('Hey! Welcome to instaBot!', 'blue')
        cprint ('Here are your menu options:', 'red')
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        choice=raw_input("Enter you choice: ")
        if choice == "a":
            self_info()

        # elif keyword is used while handling with cases having multiple choices
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        else:
            cprint("wrong choice", 'green')

start_bot()