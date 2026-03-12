from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    wallet_address = Column(String, unique=True, index=True, nullable=False)
    x_username = Column(String, unique=True, index=True, nullable=False)
    nonce = Column(String, nullable=True)