#Name: sloan woodberry
#Name: follow.py
#Purpose:to follow users that are following me back as well as other users
#Date: 5/9/19
#Collaborators: None
from instapy import InstaPy
from instapy import smart_run
import os
import zipfile
import datetime
import threading
import hideMe

import random 

insta_username = 'queenofnothing666'
insta_password = 'dogs4evr'
hideMe.manifest_json
def rest():
  time.sleep(16200)
def main():
    driver = get_chromedriver(use_proxy=True)

    driver.get('https://httpbin.org/ip')
# insta_username = 'testymctesterson87'
# insta_password = 'mytest'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True
                  #headless_browser=False,
                  #bypass_suspicious_attempt=True
                  )

with smart_run(session):
  session.set_action_delays(enabled=True, like=.3, comment= 6, follow=1, unfollow=2, randomize=True, random_range=(30, 110))
  #this compiles a list of people who follow me and I dont follow back and then follows new people
  myFans= session.pick_fans(username="queenofnothing666", live_match=True, store_locally=True)
  session.follow_by_list(myFans, times=1, sleep_delay=10, interact=False)
  #this follows people who are following my followers
  follows = session.grab_followers(username=insta_username, amount="full", live_match=True, store_locally=False)
  session.follow_user_followers(follows, amount=10, randomize=True)
  rest()
  x=0
  x+=1
  x=666

if __name__ == '__main__':
    main()