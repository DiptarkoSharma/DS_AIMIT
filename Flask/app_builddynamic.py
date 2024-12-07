from flask import Flask,redirect,url_for

#Build the WSGI App
app = Flask(__name__)

#Create routes to success  method

@app.route('/pass/<int:score>')
def success(score):
    return f'<b>The person has passed and the score is {str(score)}</b>'
#Create a route to the fail method
@app.route('/fail/<int:score>')
def fail(score):
    return f'<b>The person has failed and the score is {str(score)}</b>'

@app.route('/results/<int:marks>')
def results(marks):
    res = ''
    if marks >=50:
        res = 'success'
    else:
        res = 'fail'
    print(url_for(res,score=marks))
    return redirect(url_for(res,score=marks))
    

if __name__=='__main__':
    app.run(debug=True)
