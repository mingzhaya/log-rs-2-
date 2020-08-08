from app import app, db
from app.models import User, MapDrop, ItemDrop, Quest, TreasureDrop

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'MapDrop': MapDrop, 'ItemDrop': ItemDrop, 'Quest': Quest, 
            'TreasureDrop': TreasureDrop}
