"""TODO Docstring"""
import os
import sys

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from alembic import context
import domain.models

from config.database import Base
from config.database import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

print("-----")
print(DB_HOST)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

config = context.config

connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


print(connection_string)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
config.set_main_option("sqlalchemy.url", connection_string)

fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """TODO Docstring"""

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """TODO Docstring"""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection,
                          target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
