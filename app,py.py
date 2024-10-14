from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World!</h1>"

@app.route('/vikas', methods = ['GET', 'POST'])
def vikas():
    if request.method == 'GET':
        return "You made GET request\n"
    elif request.method == 'POST':
        return "You made POST request\n"
    else:
        return "You will never see this message\n"

@app.route('/hello')
def helloo():                    #to see status response open cmd and type "curl -I http://localhost:portno/hello"
    #return 'hello\n' , 200       #change the number according to the response you want
    response = make_response()
    response.status_code = 404
    response.headers['content-type'] = 'Abhishek/abhi'
    return response

#200 - status OK
#201 - status created
#202 - status Accepted
#404 - status not found


@app.route('/greet/<name>')          #passing variable in browser "http://127.0.0.1:portno/greet/your name"
def greet(name):
    return f"vanakam {name}"

#adding 2 numbers using its datatypes
@app.route('/add/<int:num1>/<int:num2>')              #http://127.0.0.1:portno/add/2000000/1 in browser
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return f"some parameters are missing"



if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port = 6789)