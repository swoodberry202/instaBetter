#Name: sloan woodberry
#Name: MyPost.py
#Purpose: to manage, generate, and make posts
#Date: 5/9/19
#Collaborators: None

from instapy import InstaPy
from instapy import smart_run
import os
import datetime
import threading
import random
import markovify
import nltk
import urllib.request  as urllib2 
import hideMe
import time 


insta_username = 'queenofnothing666'
insta_password = 'dogs4evr'
# insta_username = 'testymctesterson87'
# insta_password = 'mytest'



def post(postCaption):
    Mypics = os.listdir('posts')

#this picks a random image out of the posts folder to post
    myPostIndex= random.randint(0, len(Mypics)-1)
    MyPost=Mypics[myPostIndex]
    print(MyPost)
#this is the line that actually makes the official post
    os.system("instapy -u {} -p {} -f ../posts/{} -t '{}'".format(insta_username,insta_password,MyPost,postCaption))
def addTags():
    #this calls a java program that properly formats the tags for the post
    os.system("javac moreTags.java")
    os.system("java moreTags")
    myPostTags= open("cleanPostTags.txt","r").read()

    open("cleanPostTags.txt", "w").close()
    return myPostTags


allText=open("capLibrary.txt", "a")
#this reads in my list of approved tags 
myTags= open("tags.txt","r").read()
myTags=myTags.split()

#the following lines pick 8 random tags, print them in terminal, open up the instagram page associated with said tag,
#
tag1=myTags[random.randint(0,len(myTags)-1)]
tag2=myTags[random.randint(0,len(myTags)-1)]
tag3=myTags[random.randint(0,len(myTags)-1)]
tag4=myTags[random.randint(0,len(myTags)-1)]
tag5=myTags[random.randint(0,len(myTags)-1)]
tag6=myTags[random.randint(0,len(myTags)-1)]
tag7=myTags[random.randint(0,len(myTags)-1)]
tag8=myTags[random.randint(0,len(myTags)-1)]
print(tag1)
print(tag2)
print(tag3)
print(tag4)
print(tag5)
print(tag6)
print(tag7)
print(tag8)
content=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag1) 
content2=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag2) 
content3=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag3) 
content4=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag4) 
content5=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag5) 
content6=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag6) 
content7=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag7) 
content8=urllib2.urlopen("https://www.instagram.com/explore/tags/%s/?__a=1"%tag8) 
for line in content: 
    allText.write(line.decode())
for line in content2: 
    allText.write(line.decode())
for line in content3: 
    allText.write(line.decode())
for line in content4: 
    allText.write(line.decode())
for line in content5: 
    allText.write(line.decode())
for line in content6: 
    allText.write(line.decode())
for line in content7: 
    allText.write(line.decode())
for line in content8: 
    allText.write(line.decode())

#this calls my java programs that clean all the html out and isolate just the catptions from the posts under a given tag
os.system("javac formatter.java")
os.system("java formatter")

with open("cleanCaption.txt") as f:
    text = f.read()



#the following line use markovify to make a text model and generate a caption
text_model = markovify.Text(text)

caption=text_model.make_sentence()
while caption== "None":
	caption=text_model.make_sentence()

#here I add the 8 randomly picked tags from before to my post caption
caption+=str("\n")
caption+=str("#"+tag1+" ")
caption+=str("#"+tag2+" ")
caption+=str("#"+tag3+" ")
caption+=str("#"+tag4+" ")
caption+=str("#"+tag5+" ")
caption+=str("#"+tag6+" ")
caption+=str("#"+tag7+" ")
caption+=str("#"+tag8+" ")
caption+=str(addTags())
#lastly I print the caption with the tags, post the caption, and clear the files I was writing to so they are
#ready to be used again
print(caption)
post(caption)
open("cleanCaption.txt", "w").close()
open("capLibrary.txt", "w").close()

#JJJJJJJJ


