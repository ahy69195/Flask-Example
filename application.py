# Need to call this application.py for AWS default easy connectability

from flask import Flask
application = Flask(__name__) # all aplications have this, convention thing with aws

# Simply endpoint, and pass in the path endquotes
@application.route('/') # when we visit this, we pass in a function
def hello_world():
        return 'Hello World'

if __name__ == '__main__':
    application.run(host="localhost", port=8000, debug=True)



