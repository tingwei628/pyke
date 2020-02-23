class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRRT_KEY= ''
    DB_HOST = ''
    JSON_AS_ASCII = False



class ProdConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    DB_HOST = '[production_db_host_url]'
"""
class DevConfig(Config):
    pass

"""
