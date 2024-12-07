from flask import Flask,redirect,url_for,request,render_template

#Build the WSGI App
app = Flask(__name__)

#Home page - Form page
@app.route('/')
def welcome():
    return render_template('forms.html')

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

@app.route('/submit',methods=['POST','GET'])
def submit():
    avg_score = 0
    res = ''
    if request.method == "POST":
        science = float(request.form['science'])
        maths  = float(request.form['maths'])
        english = float(request.form['english'])
        avg_score = round((science+maths+english)/3,2)
    if avg_score >= 50.0:
        res = 'success'
    else:
        res = 'fail'
    return redirect(url_for(res,score=avg_score))

   

if __name__=='__main__':
    app.run(debug=True)
