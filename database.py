from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app):
  db.init_app(app)

# def db_url():
#     db_settings = settings.DATABASES['default']
#     url = URL(drivername=settings.DATABASE_ENGINE,
#         database=db_settings['NAME'],
#         username=db_settings['USER'],
#         password=db_settings['PASSWORD'],
#         host=db_settings['HOST'],
#         port=db_settings['PORT'] or None,
#         query = getattr(db_settings, 'OPTIONS', {})
#     )
#     return url

# def create_engine():
#     try:
#         url = db_url()
#     except:
#         raise
#     options = getattr(settings.DATABASES['default'], 'SQLALCHEMY_OPTIONS', {})
#     engine = sqlalchemy.create_engine(url, **options)
#     return engine

# def make_session():
#     Session = sqlalchemy.orm.sessionmaker(bind=create_engine())
#     session = Session()
#     return session
