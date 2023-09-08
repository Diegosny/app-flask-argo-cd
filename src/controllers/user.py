from src.main import app


@app.route('/')
def home():
    return {'status': 404, 'message': 'Not found'};