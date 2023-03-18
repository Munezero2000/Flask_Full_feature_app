from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '9e0057005a3f4ef5b9065b0074212c85'

# Two routes can be handled by the same function

posts = [
    {
        'author': 'Munezero Ange',
        'title': 'The Software Engineer',
        'content': 'The Introduction of AI',
        'date_posted': 'April 20, 2018',
    },
    {
        'author': 'Orlie Von Shillo',
        'title': 'The Little Baby',
        'content': 'The song of Her',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template('register.html', title='Login', form=form)


# if you don't want to use Environmental variable we can use
if __name__ == '__main__':
    app.run(debug=True)
