import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
class Database:
    def __init__(self):
        host = '127.0.0.1'
        user = 'root'
        password = 'thisispassword'
        db = 'dedwen'
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def add_admin(self):
        username = 'admin'
        hashed_password = generate_password_hash('password')
        self.cur.execute("INSERT INTO admin (user_name, user_password) values ('%s', '%s');"%(username, hashed_password))
        self.con.commit()        

    def find_user(self,username,password):       
        self.cur.execute('SELECT * FROM admin WHERE user_name = "%s";'%(username))
        user = self.cur.fetchone()
        if user is not None:
            if check_password_hash(user['user_password'], password):
                return user
        return None