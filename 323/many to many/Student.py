from orm_base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from StudentMajor import StudentMajor
from Enrollment import Enrollment

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)

    majors = relationship('StudentMajor', back_populates='student', cascade='all, save-update, delete-orphan')

    sections = relationship('Section', secondary='enrollments', back_populates='students')
    enrollments = relationship('Enrollment', back_populates='student')

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', name='students_uk_01'),
        UniqueConstraint('email', name='students_uk_02')
    )

    def __init__(self, last_name, first_name, email):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email

    def add_major(self, major):
        # Check if the major is already associated with the student
        if major not in self.majors:
            student_major = StudentMajor(self, major, datetime.now())
            self.majors.append(student_major)

    def remove_major(self, major):
        # Remove the major from the student's list of majors
        for student_major in self.majors:
            if student_major.major == major:
                self.majors.remove(student_major)
