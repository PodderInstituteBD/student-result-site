from flask import Flask, request, render_template
import sqlite3

app = Flask(_name_)

# হোমপেজ - যেখানে রোল ইনপুট ফর্ম আছে
@app.route('/')
def index():
    return render_template('index.html')

# রেজাল্ট পেইজ - ইউজারের রোল নিয়ে রেজাল্ট দেখাবে
@app.route('/result', methods=['GET'])
def result():
    roll = request.args.get('roll')

    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students WHERE roll=?", (roll,))
    data = cursor.fetchone()
    conn.close()

    if data:
        name, grade = data
        return f"<h2>Result for Roll: {roll}</h2><p>Name: {name}</p><p>Grade: {grade}</p>"
    else:
        return f"<h2>No result found for Roll: {roll}</h2>"

if _name_ == '_main_':
    app.run(debug=True)
