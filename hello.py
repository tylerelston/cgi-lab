#!/usr/bin/env python3
import os, json, templates

print("Content-type: text/html\r\n")
print("<br>")
print("<title>Test</title>")


#Q1
#print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)
obj = json.loads(json_object)
print("Browser info:")
print("<br>")
print(obj["HTTP_USER_AGENT"])
print("<br>")
print("<br>")

print("Query:")
print("<br>")
print(obj["QUERY_STRING"])


print(templates.login_page())