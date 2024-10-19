from sqlalchemy import Column, Integer, String, Text
from database.db import Base

class ProblemCategory(Base):
    __tablename__ = 'problem_categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class BugReport(Base):
    __tablename__ = 'bug_reports'
    
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    description = Column(Text)

