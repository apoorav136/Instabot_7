# Request library allows to send HTTP request
# urllib is used to fetch data across world wide web
import requests, urllib

#  access token owner : me
#   sandbox users : kajalangural , g_garkoti , Shubham.is.here

# For Sentiment Analysis in Python, we use the library TextBlob.
from textblob import TextBlob
# we need to import the text blob library and the classifier for sentiment analysis
from textblob.sentiments import NaiveBayesAnalyzer

# App access token is imported from key file. it can also be created here!
from keys import APP_ACCESS_TOKEN

# term color module is used to import color to some string so as to increase readability
from termcolor import *
import colorama

colorama.init()

# We have BASE URL in global variable whose lifetime is runtime of the program
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
    print 'GET request url : %s' % request_url
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
    print 'GET request url : %s' % request_url
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
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % APP_ACCESS_TOKEN
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            cprint('Your image has been downloaded!', 'blue')
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
            cprint('user image has been downloaded!', 'blue')
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


# get_post_id function will help us to get media id on which we can add like or comment
def get_post_id(insta_username):
    # Here we are calling GET_USER_ID function to get user id
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


# function declaration to get the recent media liked by the user.
#  this function will get media id liked by user and will download the image
def recent_media_liked():
    request_url = (BASE_URL + 'users/self/media/liked?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    liked_post = requests.get(request_url).json()
    if liked_post['meta']['code'] == 200:
        if len(liked_post['data']):
            image_name = liked_post['data'][0]['id'] + '.jpeg'
            image_url = liked_post['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'image has been downloaded'
        else:
            print('no post liked')
    else:
        print('status code error')


# let us create a function to like a post on instagram
def like_a_post(insta_username):
    # HERE WE ARE CALLING GET_POST_ID FUNCTION
    # SO AS TO GET POST ON WHICH WE CAN ADD LIKE
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)

    #  Access Token is sent in payload to authenticate the like that we're making.
    # payload act as a data handler  from whiere data is passed
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like has been made successfully!'
    else:
        print 'Your like was unsuccessful.please Try again!'


# function declaration to get list of likes on a media
def list_of_likes(insta_username):
    # here we are fetching media id from which we will get like list
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'get request url : %s' % request_url
    likes_info = requests.get(request_url).json()
    if likes_info['meta']['code'] == 200:
        if len(likes_info['data']):
            for x in range(0, len(likes_info['data'])):
                print likes_info['data'][x]['username']
        else:
            print 'no existing like'
    else:
        print 'status code error'


# function declaration to post a comment on user media
def comment_on_post(insta_username):
    media_id = get_post_id(insta_username)

    # here we are entering the comment we waant to postt by using RAW_INPUT
    comment_text = raw_input('enter your comment : ')
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)

    # while adding a comment payload will consist of access token and text we want to enter
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    print 'POST request url : %s' % (request_url)
    make_comment = requests.post(request_url, payload).json()
    if make_comment['meta']['code'] == 200:
        print 'comment has been posted successfully!'
    else:
        print 'Your comment was unsuccessful. please Try again!'


# function declaration to get list of comments on a media
def list_of_comments(insta_username):
    # here we are fetching media id from which we will get comment list
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'get request url : %s' % request_url
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                print comment_info['data'][x]['text']
        else:
            print 'no existing comment'
    else:
        print 'status code error'


# let us define a function which will delete negative comments on posts of any user
def delete_negative_comment(insta_username):
    # here we are  calling get post id function
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            # Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                # blob.sentiment will analyse comment if neg > pos it will del the comment using delete request
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    # url is passed and saved which is used for deleting a comment from post
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                        media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()
                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


# let us create a function to fetch users post in a creative way asking the criteria from the user through the console
# choose the post in a creative way
# this function will aloow the user to enter a username and he post no which user want to access or fetch..
def get_media_of_your_choice(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'user does not exist'
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            # here we will ask for the post number which we want to get.
            post_number = raw_input("enter no of post which you want : ")
            # python takes input as string it must be converted to integer using int type.
            post_number = int(post_number)
            # list has zero based indexing do data entered must be subtracted from 1 so as to get actual data entered.
            x = post_number - 1
            image_name = user_media['data'][x]['id'] + '.jpeg'
            image_url = user_media['data'][x]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print'user media does not exist'
    else:
        print 'status code error'


# here we have defined the start bot function which will start or bot application
def start_bot():
    # while loop in  python is used to repeatedly execute a set a target statements as listed below
    while True:
        print '\n'
        # C print is used for colored printing of a string
        cprint('Hello! Welcome to instaBot!', 'blue')
        cprint('you have following options :', 'red')
        print "a.Get your own details.\n"
        print "b.Get details of a user by username.\n"
        print "c.Get your own post.\n"
        print "d.Get users recent post.\n"
        print "e.Like user recent post.\n"
        print "f.get list of likes on post\n"
        print "g.Comment on user recent post.\n "
        print "h.get list of comments on post\n"
        print "i.get the recent media liked by the user.\n "
        print "j.Delete negative comment.\n "
        print "k.get post of yor choice.\n"
        print "l.Exit.\n "
        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        # elif keyword is used while handling with cases having multiple choices
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
            print get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == 'e':
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == 'f':
            insta_username = raw_input('enter username : ')
            list_of_likes(insta_username)
        elif choice == 'g':
            insta_username = raw_input("Enter the username of the user: ")
            comment_on_post(insta_username)
        elif choice == 'h':
            insta_username = raw_input('enter username : ')
            list_of_comments(insta_username)
        elif choice == 'i':
            recent_media_liked()
        elif choice == 'j':
            insta_username = raw_input("Enter the username of the user: ")
            delete_negative_comment(insta_username)
        elif choice == 'k':
            insta_username = raw_input("enter username of the user : ")
            get_media_of_your_choice(insta_username)
        elif choice == 'l':
            exit()
        else:
            cprint("wrong choice", 'green')


start_bot()
