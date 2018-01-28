import os
basedir = os.path.abspath(os.path.dirname(__file__))

# autoenv using directory based environments, when you cd out of own the environment changes as well

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'change this'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    
class ProductionConfig(Config):
    DEBUG = False
    
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    
class TestingConfig(Config):
    TESTING = True
    
