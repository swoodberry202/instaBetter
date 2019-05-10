#Name: sloan woodberry
#Name: like.py
#Purpose:to like posts based on a series of tags in tags.txt
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
	#this opens tags.txt picks a series of random tags and likes those tags
	myTags= open("tags.txt","r").read()
	myTags=myTags.split()
	usingTags=[]
	likesPerTag= random.randint(2,90)
	for q in range(1,4):
		usingTags.append(myTags[random.randint(0,len(myTags)-1)])

	session.set_action_delays(enabled=True, like=.3, comment= 6, follow=1, unfollow=2, randomize=True, random_range=(30, 110))
	#this right here tags that if included in a post make it so that post wont be liked
	session.set_dont_like(['suicidal','suicide','trump', 'crack', 'heroin', 'daddy','mommy', 'michaeljackson','sex', 'bdsm','nsfw','ddlg', 'submissive','rkelly', 'fetish','latex','kink','nymphette','bondage','nudity'])
		
	session.set_user_interact(amount=19, randomize=True, percentage=100, media='Photo')
	session.like_by_tags(usingTags, amount=10, interact=True)
	rest()

	


if __name__ == '__main__':
    main()
