from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        number = request.form['number']
        

        with open('submissions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message, number])

        return render_template('success.html', name=name)
    

if __name__ == '__main__':
    app.run(debug=True)
