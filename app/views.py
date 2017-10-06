from app import app

@app.route('/')
@app.route('/index')
def index():
    return("Hello GumGum!")

@app.route('/health')
def health():
    return("OK")
