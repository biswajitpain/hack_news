#!usr/bin/env python
# Hacker news portal  using flsak pyton
import os
import requests
from flask import Flask
from flask import render_template
import MySQLdb
from contextlib import closing
from datetime import datetime

app = Flask(__name__)
url=u'https://hacker-news.firebaseio.com/v0/'
@app.route("/")
def populate_news():
    articles = []
    comments_count={}
    url=u'https://hacker-news.firebaseio.com/v0/'
    dictionary = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
    for i in xrange(0,30):
        p=requests.get(url+'item/'+str(dictionary[i])+'.json').json()
        articles.append(p)
        #comments_count[p["id"]]=len(p["kids"])

    return render_template('index.html', articles=articles,c=comments_count)

@app.route('/user/<username>')
def show_user_profile(username):
	
    u=username
    users=[]
    url_user=u'https://hacker-news.firebaseio.com/v0/user/'
    user=requests.get(url_user+u+'.json').json()
    users.append(user)
    #for k,v in users.items():
   # return  users[0]["id"]
    return render_template('users.html',user=user)

@app.route('/comments/<id>')
def show_comments(id):
	
	comments=[]
	idd=str(id)
	p=requests.get(url+'item/'+idd+'.json').json()
	k=len(p["kids"])
	if k>10:
		for i in range(10):
			j=str(p["kids"][i])
			s=requests.get(url+'item/'+j+'.json').json()
			comments.append(s)
	else:
		for i in range(k):
                        j=str(p["kids"][i])
                        s=requests.get(url+'item/'+j+'.json').json()
                        comments.append(s)

	
	return render_template('comments.html',comments=comments)
    
    
   # return 'User %s' % username


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5555))
        app.run(host='0.0.0.0', port=port, debug=True)
        

