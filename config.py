import os

class Config:
    # Security: Secret key for session encryption
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bhumij-plants-super-secret-key-2026'
    
    # Database: Using SQLite for development
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security: HTTPOnly cookies to prevent XSS cookie theft
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True