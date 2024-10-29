from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)

# Set a secret key for securely signing the session data
app.secret_key = 'your_secret_key'

# Route to set session data
@app.route('/login', methods=['POST'])
def login():
    # Set user-specific session data
    session['username'] = request.form['username']
    return redirect(url_for('welcome'))

# Route to access session data
@app.route('/welcome')
def welcome():
    # Check if 'username' is in session
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    else:
        return "You are not logged in!"

# Route to clear session data
@app.route('/logout')
def logout():
    # Clear the session
    session.pop('username', None)
    return "You have been logged out."

if __name__ == '__main__':
    app.run(debug=True)