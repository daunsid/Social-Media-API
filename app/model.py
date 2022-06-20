from cgitb import text
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP, Column, ForeignKey, ForeignKeyConstraint, Integer, String, Boolean
from sqlalchemy.sql.expression import null, text


class Post(Base):
    __tablename__ = "post_table"

    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users_table.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User")


class User(Base):
    __tablename__ = "users_table"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String)

class Votes(Base):
    __tablename__ = "votes_table"
    post_id = Column(Integer, ForeignKey("post_table.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True)




#user = User()