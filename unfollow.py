#Name: sloan woodberry
#Name: unfollow.py
#Purpose:to unfollow users that aren't following me back
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
import time 

hideMe.manifest_json
def rest():
  time.sleep(16200)

def main():
    driver = get_chromedriver(use_proxy=True)

    driver.get('https://httpbin.org/ip')
# insta_username = 'testymctesterson87'
# insta_password = 'mytest'
insta_username = 'queenofnothing666'
insta_password = 'dogs4evr'
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  )

with smart_run(session):
    #Here I unfollow 70 people and then take a break so instagram doesn't block me
  session.unfollow_users(amount=70, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=12*60*60, sleep_delay=random.randint(0, 60))
  rest()
  





