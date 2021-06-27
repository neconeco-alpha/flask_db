from flask import Flask
from database import init_db
from api import user_router
from bin.my_batch import job

import logging

app = Flask(__name__)
app.register_blueprint(user_router, url_prefix='/api')

app.logger.setLevel(logging.DEBUG)
handle = logging.FileHandler('./log/DEBUG.log')
handle.setLevel(logging.INFO)
app.logger.addHandler(handle)


app.config.from_object('config.Config')
init_db(app)
app.cli.add_command(job)

if __name__ == '__main__':
  app.run()
