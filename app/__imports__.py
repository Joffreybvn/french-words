"""Following imports are used by the sub-dependencies of this application,
but are not included by default by pyinstaller. To solve the issue, they are
imported explicitly here."""

# Imports for config.py
import os
from slugify import slugify
from appdata import AppDataPaths


# Imports for migrations
import logging
from logging.config import fileConfig
from datetime import date
from flask import current_app
from alembic import context, op
from sqlalchemy import Column, Integer, String, Date, Identity
