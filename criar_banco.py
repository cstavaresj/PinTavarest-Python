from PinTavarest import database, app
from PinTavarest.models import Usuario, Foto

with app.app_context():
    database.create_all()