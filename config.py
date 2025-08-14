import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://event_db_95sh_user:ohQgnQTy1NsO5nYyIVuFf4psihb2wu0G@dpg-d2epdt3ipnbc73a94rk0-a:5432/event_db_95sh"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'event.db')}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = "supersecretkey"

