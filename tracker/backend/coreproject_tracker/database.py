from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from coreproject_tracker.envs import DATABASE_URI

engine = create_async_engine(DATABASE_URI, echo=True)

# Session to be used throughout app.
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
