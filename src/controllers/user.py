from src.main import app


@app.route('/')
def home():
    return 'App running is app-flask';