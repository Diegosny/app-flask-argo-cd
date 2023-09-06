from src.main import app


@app.route('/')
def home():
    return 'App running is port 5000 - app-python';