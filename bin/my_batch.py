import click
from flask.cli import AppGroup
from models.user import User
from flask import current_app
# from app import app

from faker import Factory
fake = Factory.create('ja_JP')


job = AppGroup('job')
# @click.command('task1', help="Hello World.")

@job.command('hello')
def cmd():
  # app.logger.info('test')
  # print('hello world')
  current_app.logger.info('test')


  user = User.registUser({
    'name': fake.name(),
    'address': fake.address(),
    'tel': fake.phone_number(),
    'mail': fake.email()
  })
