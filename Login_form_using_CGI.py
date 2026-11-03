#We create two Python files:
#1. login.py – Displays the login form.
#2. display.py – Receives input and displays it on another page.
#print("Content-Type: text/html\n")

print("""
<html>
<head>
    <title>Login Form</title>
</head>
<body>

<h2>Login Form</h2>

<form action="display.py" method="GET">

    Username:
    <input type="text" name="username" required>
    <br><br>

    Password:
    <input type="password" name="password" required>
    <br><br>

    <input type="submit" value="Login">

</form>

</body>
</html>
""")






import os
import urllib.parse
import html

# Get form data
data = urllib.parse.parse_qs(
    os.environ.get("QUERY_STRING", "")
)

username = data.get("username", [""])[0]
password = data.get("password", [""])[0]

# Display output
print("Content-Type: text/html\n")

print("<html>")
print("<head><title>Login Details</title></head>")
print("<body>")

print("<h2>Login Details</h2>")

print("<p>Username: " + html.escape(username) + "</p>")

print("<p>Password: " + html.escape(password) + "</p>")

print("</body>")
print("</html>")