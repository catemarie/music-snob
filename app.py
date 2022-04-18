from flask import Flask, render_template
import sys
import logging


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    event1 = {}
    event1['title'] = 'Event 1'
    event1['content'] = 'First event'
    event2 = {}
    event2['title'] = 'Event 2'
    event2['content'] = 'Second event'
    events = [event1, event2]
    return render_template('index.html', events=events)
