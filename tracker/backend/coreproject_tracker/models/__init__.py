"""Module for handling all database models.

Notes:
    The models created with the inherited `Base` constant
    must be imported below the declaration for `Alembic`
    autogenerate to work.
"""

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass
