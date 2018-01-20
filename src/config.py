class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Test!234@localhost/abcd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}