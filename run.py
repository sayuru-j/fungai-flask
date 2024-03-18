from flask import Flask
from app.routes.growth_stage_prediction_routes import growth_prediction_routes

app = Flask(__name__)


# Route Registry
app.register_blueprint(growth_prediction_routes)


if __name__ == "__main__":
    # Run the server
    app.run(host="0.0.0.0", port=5000)
