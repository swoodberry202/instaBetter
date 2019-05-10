#Name: sloan woodberry
#Name: quickstart.py
#Purpose: to run all of my python simoltaniously
#Date: 5/9/19
#Collaborators: None
from instapy import InstaPy
from instapy import smart_run
import os
import zipfile
import datetime
import threading
import hideMe
import requests
import random 
from multiprocessing import Pool 
#this right here manifests my rotating proxy 
hideMe.manifest_json
import time 
#this is what I call to pause every now and then
def rest():
	time.sleep(random.randint(60*30,6*60*60))
def main():
    driver = get_chromedriver(use_proxy=True)

    driver.get('https://httpbin.org/ip')

insta_username = 'queenofnothing666'
insta_password = 'dogs4evr'
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  )

with smart_run(session):
	#while True:
	#this threading allows me to run for a random period of time and then pause
	timer = threading.Timer(random.randint(60*30,5*60*60),rest)
	timer.start()
		#this puts a delay between actions (instaPy randomizes the length of time between actions for me)
	session.set_action_delays(enabled=True, like=.3, comment= 6, follow=1, unfollow=2, randomize=True, random_range=(30, 110))
		#these are hashtags that will be purposefully excluded from all following and liking
	session.set_dont_like(['suicidal','suicide','trump', 'crack', 'heroin', 'daddy','mommy', 'michaeljackson','sex', 'bdsm','nsfw','ddlg', 'submissive','rkelly', 'fetish','latex','kink','bondage','nudity'])

		#this sets up the threading/ all of the programs that will be running at the same time and runs them
	processes = ('like.py','like.py', 'unfollow.py', 'unfollow.py', 'follow.py')
		
	def run_process(process):
		os.system('python {}'.format(process))
		
	pool = Pool(processes=5)                                                        
	pool.map(run_process, processes)                                                     


if __name__ == '__main__':
    main()

