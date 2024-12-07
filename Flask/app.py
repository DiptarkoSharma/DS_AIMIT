from flask import Flask

#Create a WSGI App
app = Flask(__name__)

@app.route('/')
def main():
    return f'<h1>Welcome to my world</h1>'

@app.route('/students')

def students():
    return f'<h2>Welcome to my world, dear Students</h2>'

if __name__ =='__main__':
    app.run(debug= True)