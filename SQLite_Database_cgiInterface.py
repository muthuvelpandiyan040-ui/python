import sqlite3
import os
import urllib.parse
import html

# Connect to SQLite database
db = os.path.join(os.path.dirname(__file__), "student.db")
con = sqlite3.connect(db)
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# Get form data from CGI request
params = urllib.parse.parse_qs(os.environ.get("QUERY_STRING", ""))

action = params.get("action", [""])[0]

# Read form values
sid = params.get("id", [""])[0]
name = params.get("name", [""])[0]
age = params.get("age", [""])[0]
course = params.get("course", [""])[0]

# CGI response header
print("Content-Type: text/html\n")

print("<html><body>")
print("<h2>Student Database Management</h2>")

# INSERT operation
if action == "insert":
    cur.execute(
        "INSERT INTO student (id, name, age, course) VALUES (?, ?, ?, ?)",
        (sid, name, age, course)
    )
    con.commit()
    print("<p>Record Inserted Successfully!</p>")

# UPDATE operation
elif action == "update":
    cur.execute(
        "UPDATE student SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, sid)
    )
    con.commit()
    print("<p>Record Updated Successfully!</p>")

# DESTROY / DELETE operation
elif action == "delete":
    cur.execute("DELETE FROM student WHERE id=?", (sid,))
    con.commit()
    print("<p>Record Deleted Successfully!</p>")

# SELECT operation
elif action == "select":
    print("<h3>Student Records</h3>")
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()

    print("<table border='1'>")
    print("<tr><th>ID</th><th>Name</th><th>Age</th><th>Course</th></tr>")

    for row in rows:
        print("<tr>")
        for value in row:
            print("<td>" + html.escape(str(value)) + "</td>")
        print("</tr>")

    print("</table>")

# Display HTML forms
print("""
<h3>Insert Student</h3>
<form>
<input type="hidden" name="action" value="insert">
ID: <input name="id" required><br>
Name: <input name="name" required><br>
Age: <input name="age" type="number" required><br>
Course: <input name="course" required><br>
<input type="submit" value="Insert">
</form>

<h3>Update Student</h3>
<form>
<input type="hidden" name="action" value="update">
Student ID: <input name="id" required><br>
New Name: <input name="name" required><br>
New Age: <input name="age" type="number" required><br>
New Course: <input name="course" required><br>
<input type="submit" value="Update">
</form>

<h3>Delete Student</h3>
<form>
<input type="hidden" name="action" value="delete">
Student ID: <input name="id" required><br>
<input type="submit" value="Delete">
</form>

<h3>Display Students</h3>
<form>
<input type="hidden" name="action" value="select">
<input type="submit" value="Display Records">
</form>
""")

con.close()

print("</body></html>")