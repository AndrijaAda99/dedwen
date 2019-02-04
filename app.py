from flask import Flask, render_template, redirect, url_for, request, session, jsonify, json, make_response
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from database import Database

app = Flask(__name__)
app.secret_key = 'thisissecret'

db = Database()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, username):
        self.username = username
    @property
    def id(self):
        return self.username

@login_manager.user_loader
def load_user(id):
    return User(id)

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods=['GET','POST'])
def login(text=''):    
    if current_user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.find_user(username, password)
        if user is not None:
            login_user(User(username),remember=request.form.get('remember_me'))
            session['username'] = username
            return redirect('dashboard')
        else:
            text = 'Wrong username or password'        
    return render_template('login.html', text=text)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    resp = make_response(render_template('login.html', 
    user=session['username']))
    resp.set_cookie('endpoint', '', expires=0)
    return resp

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/meters')
@login_required
def meters():
    return render_template('meters.html')

@app.route('/concentrators')
@login_required
def concentrators():
    return render_template('concentrators.html')

@app.route('/pointofdelievery')
@login_required
def pointofdelievery():
    return render_template('pointofdelievery.html')

@app.route('/alarms')
@login_required
def alarms():
    return render_template('alarms.html')

@app.route('/meterauto')
@login_required
def meterauto():
    return render_template('meterauto.html')

@app.route('/statuslog')
@login_required
def statuslog():
    return render_template('statuslog.html')

@app.route('/singlemeter')
@login_required
def singlemeter():
    return render_template('singlemeter.html')

@app.route('/concentratormeterreading')
@login_required
def concentratormeterreading():
    return render_template('concentratormeterreading.html')

@app.route('/schedulereading')
@login_required
def schedulereading():
    return render_template('schedulereading.html')

@app.route('/readingondemand')
@login_required
def readingondemand():
    return render_template('readingondemand.html')

@app.route('/singlemeterman')
@login_required
def singlemeterman():
    return render_template('singlemeterman.html')

@app.route('/readingpersonal')
@login_required
def readingpersonal():
    return render_template('readingpersonal.html')

@app.route('/readingequipment')
@login_required
def readingequipment():
    return render_template('readingequipment.html')

@app.route('/pointofdelieverymeter')
@login_required
def pointofdelieverymeter():
    return render_template('pointofdelieverymeter.html')

@app.route('/consumermeter')
@login_required
def consumermeter():
    return render_template('consumermeter.html')

@app.route('/concentratormeter')
@login_required
def concentratormeter():
    return render_template('concentratormeter.html')

@app.route('/definitionstructures')
@login_required
def definitionstructures():
    return render_template('definitionstructures.html')

@app.route('/overviewstructure')
@login_required
def overviewstructure():
    return render_template('overviewstructure.html')

@app.route('/meterassignment')
@login_required
def meterassignment():
    return render_template('meterassignment.html')

@app.route('/concentratorassignment')
@login_required
def concentratorassignment():
    return render_template('concentratorassignment.html')

@app.route('/pointofdelieveryassignment')
@login_required
def pointofdelieveryassignment():
    return render_template('pointofdelieveryassignment.html')

@app.route('/listconsumers')
@login_required
def listconsumers():
    return render_template('listconsumers.html')

@app.route('/addconsumer')
@login_required
def addconsumer():
    return render_template('addconsumer.html')

@app.route('/editconsumer')
@login_required
def editconsumer():
    return render_template('editconsumer.html')

@app.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    app.debug = True
    app.run()