from flask import Flask,render_template,flash, redirect,url_for,session,logging,request


app = Flask(__name__)


u={}

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        print(uname)
        print(passw)
        print(u)
        try:
                if u[uname]==passw:
                        return '{} is succesfully  login'.format(uname)
                else:
                        return 'worng password'
        except:
                
                return 'worng password'
        
        
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        passw = request.form['passw']
        u[uname]=passw
        return '{} is succesfully  registered'.format(uname)
        
         
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
