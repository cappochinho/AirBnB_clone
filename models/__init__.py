#!/usr/bin/python3
# init file for the models module

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()