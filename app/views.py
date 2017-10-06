from app import app

@app.route('/')
@app.route('/index')
def index():
    F = open("app/static/version", "r")
    version = F.read()
    return("Hello GumGum! NEW Version:" + version)

@app.route('/health')
def health():
    return("OK")
