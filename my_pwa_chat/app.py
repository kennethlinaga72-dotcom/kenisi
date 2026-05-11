from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

# Essential for PWA: serving the service worker from the root scope
@app.route('/sw.js')
def serve_sw():
    return app.send_static_file('sw.js')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)