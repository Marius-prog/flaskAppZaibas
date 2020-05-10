import os


class BaseConfig(object):
    DEBUG = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/db.sqlite'


class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://bhwooehxgexjmd:df2eed7c2cda1b6cd34de62444d73dc5b8c7e6e5f67b4b6adf69609166d80d02@ec2-176-34-97-213.eu-west-1.compute.amazonaws.com:5432/ddlol2pkc7t5ns'

class HerokuConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
