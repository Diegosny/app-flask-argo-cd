from src.main import app


@app.route('/')
def home():
    return {'status': 200, 'message': 'ok'};