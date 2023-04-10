from flask import Flask, render_template, request, redirect, session, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'Secret'



# The "@" decorator associates this route with the function immediately following
# @app.route('/process', methods=['post'])
# def process():
#     session['times'] = request.form['times']
#     return redirect('/')

@app.route('/')
def table():
    session['times'] = request.form['times']
    if 'Secret' in session:
        request.form['times'].innerHTML += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    return render_template('index.html')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

