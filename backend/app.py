from flask import Flask
from flask_cors import CORS
from utils import db

app = Flask(__name__)
cors = CORS(
        app,
        supports_credentials=True,
        origins="*",
        allow_headers=["Cookie", "content-type"],
    )


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{db_user}:{db_password}@{db_url}/{db_name}"
app.config["SECRET_KEY"] = "MLJGMFHGFLINGFMINDM986497408£**dslfihsjdf-66"
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_PATH"] = "/"
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.config["development"] = True
    app.run("0.0.0.0", 5000, debug=True)
