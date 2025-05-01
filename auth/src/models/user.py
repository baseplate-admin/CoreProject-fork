import uuid
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    name: str = Field(index=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
