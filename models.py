from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=False)


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    fk_student = Column(
        Integer,
        ForeignKey(
            Student.id,
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
    )
    student = relationship(Student, backref="grades")
