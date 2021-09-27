from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/avaleht')
def hello_world():
    return 'Jou nibba!'
    
if __name__ == '__main__':
    app.run()