from flask import Flask, render_template, redirect, url_for, request, session, jsonify, json, make_response

app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods=['GET','POST'])
def login(text=''):    
    #if current_user.is_authenticated:
    #    return redirect('dashboard')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        '''
        user = find_user(username, password)
        if user is not None:
            login_user(User(username),remember=request.form.get('remember_me'))
            session['username'] = username
            return redirect('dashboard')
        else:
            text = 'Wrong username or password'
        '''
        return redirect('dashboard')
    return render_template('login.html', text=text)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/automaticmeasurement')
def automaticmeasurement():
    return render_template('automaticmeasurement.html')

@app.route('/meters')
def meters():
    return render_template('meters.html')

@app.route('/concentrators')
def concentrators():
    return render_template('concentrators.html')

@app.route('/pointofdelievery')
def pointofdelievery():
    return render_template('pointofdelievery.html')

@app.route('/systemnotification')
def systemnotification():
    return render_template('systemnotification.html')

@app.route('/alarms')
def alarms():
    return render_template('alarms.html')

@app.route('/meterauto')
def meterauto():
    return render_template('meterauto.html')

@app.route('/statuslog')
def statuslog():
    return render_template('statuslog.html')

@app.route('/automaticmeter')
def automaticmeter():
    return render_template('automaticmeter.html')

@app.route('/singlemeter')
def singlemeter():
    return render_template('singlemeter.html')

@app.route('/concentratormeterreading')
def concentratormeterreading():
    return render_template('concentratormeterreading.html')

@app.route('/schedulereading')
def schedulereading():
    return render_template('schedulereading.html')

@app.route('/readingondemand')
def readingondemand():
    return render_template('readingondemand.html')

@app.route('/manualmeter')
def manualmeter():
    return render_template('manualmeter.html')

@app.route('/readingpersonal')
def readingpersonal():
    return render_template('readingpersonal.html')

@app.route('/readingequipment')
def readingequipment():
    return render_template('readingequipment.html')

@app.route('/historyofchanges')
def historyofchanges():
    return render_template('historyofchanges.html')

@app.route('/pointofdelieverymeter')
def pointofdelieverymeter():
    return render_template('pointofdelieverymeter.html')

@app.route('/consumermeter')
def consumermeter():
    return render_template('consumermeter.html')

@app.route('/concentratormeter')
def concentratormeter():
    return render_template('concentratormeter.html')

@app.route('/hierarchiesorganization')
def hierarchiesorganization():
    return render_template('hierarchiesorganization.html')

@app.route('/definitionstructures')
def definitionstructures():
    return render_template('definitionstructures.html')

@app.route('/overviewstructure')
def overviewstructure():
    return render_template('overviewstructure.html')

@app.route('/assignmentelements')
def assignmentelements():
    return render_template('assignmentelements.html')

@app.route('/meterassignment')
def meterassignment():
    return render_template('meterassignment.html')

@app.route('/concentratorassignment')
def concentratorassignment():
    return render_template('concentratorassignment.html')

@app.route('/pointofdelieveryassignment')
def pointofdelieveryassignment():
    return render_template('pointofdelieveryassignment.html')

@app.route('/energyconsumers')
def energyconsumers():
    return render_template('energyconsumers.html')

@app.route('/listconsumers')
def listconsumers():
    return render_template('listconsumers.html')

@app.route('/modifyconsumers')
def modifyconsumers():
    return render_template('modifyconsumers.html')

@app.route('/addconsumer')
def addconsumer():
    return render_template('addconsumer.html')

@app.route('/editconsumer')
def editconsumer():
    return render_template('editconsumer.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    app.debug = True
    app.run()