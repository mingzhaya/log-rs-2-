from app import app, db
from app.models import User, MapDrop

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'MapDrop': MapDrop}
