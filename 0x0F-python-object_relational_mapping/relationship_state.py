#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from splalchemy.ext.declarative import declarative_base
"""
    Module that performs creates a states class based off of Base
"""

Base = declarative_base()

class City(Base):
    """
        the ``State`` class which inherits from ``Base`` class.
    """
    __tablename__ = "states"
    id = Column(Integer, primay_Key=True)
    name = Column(String(128), nullable=False)
