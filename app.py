
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sfjgknkgj85jmkfd7039krmtgtou'

points = [{'id': 1, 'name': "point1", 'xcoord': 55.15, 'ycoord': 33.15, 'header': "Some text1", 'body': "Some body1"},
              {'id': 2,'name': "point2", 'xcoord': 53.15, 'ycoord': 31.15, 'header': "Some text2", 'body': "Some body2"},
              {'id': 3,'name': "point3", 'xcoord': 57.15, 'ycoord': 35.15, 'header': "Some text3", 'body': "Some body3"}]

@app.route('/')
def index():
    ppoints = points
    return render_template('index.html', points=ppoints)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        header = request.form['header']
        body = request.form['body']
        xcoord = float(request.form['xcoord'])
        ycoord = float(request.form['ycoord'])

        points.append({'id':len(points) + 1, 'xcoord': xcoord, 'ycoord': ycoord, 'header': header, 'body': body})
        print(xcoord, ycoord, header, body)
        return redirect(url_for('index'))

    return render_template('create.html')