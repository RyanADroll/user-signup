from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("sign-up.html")

def no_space(value):
    whitespace = " "
    if whitespace not in value:
        return True
    else:
        return False

def is_filled(value):
    if value != "":
        return True
    else:
        return False

def valid_email_at(value):
    if value.count('@') == 1:
        return True
    else:
        return False

def valid_email_period(value):
    if value.count('.') == 1:
        return True
    else:
        return False


@app.route("/validate-form", methods=['POST'])
def validate():
    
    username_input = request.form['username']
    password_input = request.form['password']
    verify_input = request.form['verify']
    email_input = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if not is_filled(username_input):
        username_error = "Please enter a username"
        username_input = ""
    else:
        username_len = len(username_input)
        if  username_len > 20 or username_len < 3:
            username_error = "Username must be between 3 and 20 characters"
            username_input = ""
        else:
            if not no_space(username_input):
                username_error = "Spaces are not allowed"
                username_input = ""

    if not is_filled(password_input):
        password_error = "Please enter a password"
        password_input = ""
    else:
        password_len = len(password_input)
        if  password_len > 20 or password_len < 3:
            password_error = "Password must be between 3 and 20 characters"
            password_input = ""
        else:
            if not no_space(username_input):
                password_error = "Spaces are not allowed"
                password_input = ""

    if not is_filled(verify_input):
        verify_error = "Please enter a password"
        verify_input = ""
    else:
        if verify_input != password_input:
            verify_error = "Passwords must match"
            verify_input = ""

    if is_filled(email_input):
        email_len = len(email_input)
        if  email_len > 20 or email_len < 3:
            email_error = "Email must be between 3 and 20 characters"
            email_input = ""
        else:
            if not valid_email_at(email_input):
                email_error = "Not a valid email"
                email_input = ""
            elif not valid_email_period(email_input):
                email_error = "Not a valid email"
                email_input = ""


    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", username=username_input)
    else:
        return render_template ("sign-up.html", username_input=username_input,
        email_input=email_input, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()