from flask import Flask
from routes.user_routes import main_bp
from routes.main_routes import usuario_bp

app = Flask(__name__)
app.secret_key = 'yahoo'

# registrar os blueprints
app.register_blueprint(main_bp)
app.register_blueprint(usuario_bp, url_prefix='/usuario')

if __name__ =='__main__':
    app.run(debug=True)
