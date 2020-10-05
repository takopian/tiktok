
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    points = [{'name': "point1", 'xcoord': 55.15, 'ycoord': 33.15, 'header': "Some text1", 'body': "Some body1"},
              {'name': "point2", 'xcoord': 53.15, 'ycoord': 31.15, 'header': "Some text2", 'body': "Some body2"},
              {'name': "point3", 'xcoord': 57.15, 'ycoord': 35.15, 'header': "Some text3", 'body': "Some body3"}]

    return render_template('index.html', points=points)