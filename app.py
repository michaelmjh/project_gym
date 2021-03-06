from flask import Flask, render_template

from controllers.booking_controller import booking_blueprint
from controllers.fitness_classes_controller import fitness_class_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(booking_blueprint)
app.register_blueprint(fitness_class_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)