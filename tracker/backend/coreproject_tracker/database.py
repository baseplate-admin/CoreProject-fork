from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

from coreproject_tracker.envs import DATABASE_URI

engine = create_async_engine(DATABASE_URI, echo=True)

# Session to be used throughout app.
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_session():
    """
    Async contextmanager that yields a Session,
    commits if all goes well, rolls back on error.
    """
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
