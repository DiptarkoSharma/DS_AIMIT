from flask import Flask,redirect,url_for,request,render_template

#Build the WSGI App
app = Flask(__name__)

#Home page - Form page
@app.route('/')
def welcome():
    return render_template('forms.html')



@app.route('/submit',methods=['POST','GET'])
def submit():
    avg_score = 0
    res = ''
    if request.method == "POST":
        science = float(request.form['science'])
        maths  = float(request.form['maths'])
        english = float(request.form['english'])
        avg_score = round((science+maths+english)/3,2)
        print(f'Average score is {avg_score}')
    return render_template('results.html',results=avg_score)

   

if __name__=='__main__':
    app.run(debug=True)
