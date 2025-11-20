'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''



from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length



class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired( message="Please, enter a valid email!."), Length(min=13,max=30), ])
    password = PasswordField(label='Password', validators=[DataRequired(message="Please, enter a valid password!"), Length(min=8, max=20)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)

app.secret_key = "manman"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login_page():
    login_form = LoginForm()
    #login_form.validate_on_submit()
    if login_form.validate_on_submit():
        entered_email = login_form.email.data
        entered_password = login_form.password.data
        print(f"Entered email: {entered_email}\nEntered password: {entered_password}")

        if entered_email == "admin@email.com" and entered_password == "12345678":
            print(f"Right Email: {entered_email}\nRight Password: {entered_password}")
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
