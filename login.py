#!/usr/bin/env python3
import cgi, cgitb, secret, templates, json, os

form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

json_object = json.dumps(dict(os.environ), indent=4)
obj = json.loads(json_object)

if secret.username == username and secret.password == password:
    cookies = obj["HTTP_COOKIE"].split(";")
    alreadyLoggedIn = False
    for cookie in cookies:
        if cookie.split("=")[0] == "LoginStatus" and cookie.split("=")[1] == "loggedIn":
            alreadyLoggedIn = True
    print('Set-Cookie:LoginStatus = loggedIn;\r\n')
    print("Content-type: text/html\r\n")
    if alreadyLoggedIn:
            print("Already logged in! <br>")
    print(templates.secret_page(username, password))
else:
    print("Content-type: text/html\r\n")
    print(templates.after_login_incorrect())