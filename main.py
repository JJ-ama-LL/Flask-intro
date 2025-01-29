from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response


@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied


@app.route('/stats')
def get_stats():
    chicken = veg = fish = 0
    comp_spe = comp_maj = info_spe = info_maj = 0

    for student in data:
        if student['pref'] == 'Chicken':
            chicken+=1
        elif student['pref'] == 'Fish':
            fish+=1
        elif student['pref'] == 'Vegetable':
            veg+=1

        if student['programme'] == 'Computer Science (Major)':
            comp_maj+=1
        elif student['programme'] == 'Computer Science (Special)':
            comp_spe+=1
        elif student['programme'] == 'Information Technology (Major)':
            info_maj+=1
        elif student['programme'] == 'Information Technology (Special)':
            info_spe+=1

    result = {
        "Chicken" : chicken,
        "Computer Science (Major)" : comp_maj,
        "Computer Science (Special)" : comp_spe,
        "Fish" : fish,
        "Information Technology (Major)" : info_maj,
        "Information Technology (Special)" : info_spe,
        "Vegetable" : veg
    }

    return jsonify(result)


@app.route('/add/<int:a>/<int:b>')
def addition(a,b):
    x = a + b

    return jsonify(x) 


@app.route('/subtract/<int:a>/<int:b>')
def sub(a,b):
    x = a - b

    return jsonify(x) 


@app.route('/multiply/<int:a>/<int:b>')
def mult(a,b):
    x = a * b

    return jsonify(x) 


@app.route('/divide/<int:a>/<int:b>')
def div(a,b):
    x = a / b

    return jsonify(x) 


# route variables
@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

app.run(host='0.0.0.0', port=8080)