# Request library allows to send HTTP request
# urllib is used to fetch data across world wide web
import requests, urllib

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
    request_url = (BASE_URL + 'user''s/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
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

# let us define a function to get id of self id's recent post and download the image
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            cprint ('Your image has been downloaded!', 'blue')
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

# let us define a function to get user recent post id..
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s' % (user_id, APP_ACCESS_TOKEN))
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            # downloaded image is saved in a variable image_name
            image_name = user_media['data'][0]['id'] + '.jpeg'
            # url of the image is provided which is to be downloaded
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            # urllib is used to fetch data across world wide web .
            # urllib library is installed using command pip install urllib
            urllib.urlretrieve(image_url, image_name)
            cprint ('user image has been downloaded!', 'blue')
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

# here we have defined the start bot function which will start or bot application
def start_bot():

    # while loop in  python is used to repeatedly execute a set a target statements as listed below
    while True:
        print '\n'
        # C print is used for colored printing of a string
        cprint ('Hello! Welcome to instaBot!', 'blue')
        cprint ('you have following options :', 'red')
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.get your own post\n"
        print "d.get users recent post \n"
        choice=raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        # elif keyword is used while handling with cases having multiple choices
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
            print get_own_post()
        elif choice =="d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        else:
            cprint("wrong choice", 'green')

start_bot()