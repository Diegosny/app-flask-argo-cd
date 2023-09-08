from src.main import app


@app.route('/')
def home():
    return {'status': 422, 'message': 'Nao processado'};