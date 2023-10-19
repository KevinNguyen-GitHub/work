from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from your_module import Base  # Import your models

class Enrollment(Base):
    __tablename__ = 'enrollments'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id'), primary_key=True)

    # Define a reference to the Student and Section models
    student = relationship('Student', back_populates='enrollments')
    section = relationship('Section', back_populates='enrollments')

# In the Student and Section models, add the back_populates attribute for the enrollments relationship
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    # Other student attributes

    # Define the relationship with Enrollment
    enrollments = relationship('Enrollment', back_populates='student')

class Section(Base):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True)
    # Other section attributes

    # Define the relationship with Enrollment
    enrollments = relationship('Enrollment', back_populates='section')
