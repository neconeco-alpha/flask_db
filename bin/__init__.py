from flask.cli import AppGroup
from bin.my_batch import cmd

job = AppGroup('job')

job.add_command(cmd)
