import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SITE_NAME = "YJ Space"
    SITE_AUTHOR = "Your Name"
    SITE_DESCRIPTION = "A showcase of my projects and skills"