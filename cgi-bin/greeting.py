#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
username = form.getvalue('name')

greeting = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
  </head>  
  <body>
    <h1>Hello {username}!</h1>
    <p>This took f*cking 10 hours of my very limited lifetime...</p>
  </body>
</html>
""".format(username=username)

print (greeting)