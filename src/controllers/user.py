from src.main import app


@app.route('/')
def home():
    return {'status': 500, 'message': 'Internal error'};