from app import app

@app.route('/')
@app.route('/index')
def index():
    return("Hello GumGum! version 1.0.0")

@app.route('/health')
def health():
    return("OK")
