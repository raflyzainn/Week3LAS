from flask import Flask
from Controllers.about import about_bp
from Controllers.home import home_bp
from Controllers.maps import maps_bp

app = Flask(__name__, template_folder='Templates')

app.register_blueprint(about_bp)
app.register_blueprint(home_bp)
app.register_blueprint(maps_bp)

if __name__ == '__main__':
    app.run(debug=True)