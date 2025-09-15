from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Store student details in memory
students = []

# HTML template inside Python
html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Student Details</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background: #f9f9f9;
    }
    h1, h2 { color: #2c3e50; }
    form {
      background: #fff;
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
      margin-bottom: 20px;
      max-width: 400px;
    }
    label { display: inline-block; width: 120px; }
    input { padding: 5px; width: 200px; }
    button {
      margin-top: 10px;
      padding: 8px 14px;
      background: #2980b9;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover { background: #1f6391; }
    table {
      width: 100%;
      border-collapse: collapse;
      background: #fff;
    }
    th, td {
      padding: 10px;
      border: 1px solid #ddd;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Student Details Form</h1>

  <form action="/add" method="POST">
    <label>Name:</label>
    <input type="text" name="name" required><br><br>

    <label>Address:</label>
    <input type="text" name="address" required><br><br>

    <label>Phone:</label>
    <input type="text" name="phno" required><br><br>

    <label>Email:</label>
    <input type="email" name="email" required><br><br>

    <button type="submit">Add Student</button>
  </form>

  <h2>Student List</h2>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Address</th>
        <th>Phone</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      {% for student in students %}
      <tr>
        <td>{{ student.name }}</td>
        <td>{{ student.address }}</td>
        <td>{{ student.phno }}</td>
        <td>{{ student.email }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_page, students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    address = request.form["address"]
    phno = request.form["phno"]
    email = request.form["email"]

    students.append({"name": name, "address": address, "phno": phno, "email": email})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
