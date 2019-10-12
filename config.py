import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# To supress this warning  
# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead 
SQLALCHEMY_TRACK_MODIFICATIONS = False

# The database uri is of type '<service>://<user>:<password>@<host:port>/<dbname>'
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/fyuurdb'