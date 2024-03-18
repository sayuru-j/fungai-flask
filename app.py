from flask import Flask
from src.routes.growth_stage_prediction_routes import growth_prediction_routes

app = Flask(__name__)


@app.route("/")
def server_running():
    return "Server running"


# Route Registry
app.register_blueprint(growth_prediction_routes)

# if __name__ == "__main__":
#     # Run the server
#     # src.run(host="0.0.0.0", port=5000)
#     app.run()
