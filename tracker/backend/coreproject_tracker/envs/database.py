import os

__all__ = ["DATABASE_URI"]


DATABASE_URI = os.environ.get(
    "DATABASE_URL", "postgresql+asyncpg://postgres:supersecretpassword@localhost/seeder"
)
