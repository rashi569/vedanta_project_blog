import pyrebase
import os
from flask import Flask, render_template,request,redirect

config = {
    "apiKey": os.environ.get("FIREBASE_API_KEY"),
    "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
    "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.environ.get("FIREBASE_APP_ID"),
    "databaseURL": os.environ.get("FIREBASE_DATABASE_URL")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()
storage=firebase.storage()

app = Flask(__name__)

@app.route('/')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/signin',methods=["GET","POST"])
def signin():
    if request.method=='POST':
        username=request.form["username"]
        password=request.form["password"]
        try:
            auth.sign_in_with_email_and_password(username,password)
            return redirect('postedit')
        except:
            return render_template("signin.html")
    if auth.current_user:
        return redirect('postedit')
     
    return render_template("signin.html")

@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method=='POST':
        username=request.form["email"]
        password=request.form["password"]
        auth.create_user_with_email_and_password(username,password)
        return redirect('signin')
    return render_template("signup.html")

# @app.route('/reset_password',methods=['GET','POST'])
# def forgot_password():
#     if request.method == 'POST' :
#         email=request.form['user_email']
#         auth.send_password_reset_email(email)
#         return render_template('index.html')
#     return render_template('reset_password.html')

@app.route('/logout')
def logout():
    auth.current_user=None
    return redirect('/')

@app.route('/blog',methods=["GET","POST"])
def blog():
    blog=db.child("Blogs").get()
    blogs=[item.val() for item in blog.each()]
    return render_template("blog.html",blogs=blogs)

@app.route('/postedit',methods=["GET","POST"])
def postedit():
    user=auth.current_user
    if request.method=='POST':
        title=request.form["title"]
        body=request.form["body"]
        data={"title":title,"body":body}
        db.child("Blogs").child(title).set(data)
        return redirect('blog')
    return render_template("postedit.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
