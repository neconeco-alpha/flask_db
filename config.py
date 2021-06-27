class SystemConfig:
  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'sqlite:///./mydb/test.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = True

Config = SystemConfig
