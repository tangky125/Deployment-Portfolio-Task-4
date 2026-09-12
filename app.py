from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
visit_count = 0

@app.route('/')
def home():
    global visit_count
    visit_count += 1
    return render_template('index.html', time=datetime.now(), visits=visit_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)