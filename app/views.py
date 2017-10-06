from app import app

@app.route('/')
@app.route('/index')
def index():
    F = open("static/version", "r")
    version = F.read()
    return("Hello GumGum! Version:" + version)

@app.route('/health')
def health():
    return("OK")
