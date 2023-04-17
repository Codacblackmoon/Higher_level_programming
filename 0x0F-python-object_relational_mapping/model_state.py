#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(0

class City(Base):
    """
    State class that inherits from  Base

    Attributes:
        id: Id state
        name: NAME of state
    """
    __tablename__ = "states"
    id = Column(Integer, primay_Key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False
