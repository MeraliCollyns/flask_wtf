import os

# class Config:
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False