from orm_base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from Enrollment import Enrollment
class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    department_abbreviation = Column(String(10), nullable=False)
    course_number = Column(Integer, nullable=False)
    room = Column(String(50), nullable=False)
    course = relationship("Course", back_populates="sections")

    enrollments = relationship('Enrollment', back_populates='section')

    __table_args__ = (
        UniqueConstraint('number', 'department_abbreviation', 'course_number', name='sections_uk_01'),
        ForeignKeyConstraint(["department_abbreviation", "course_number"], ["courses.department_abbreviation", "courses.course_number"])
    )

    def __init__(self, number: int, department_abbreviation: str, course_number: int, room: str = None):
        self.number = number
        self.department_abbreviation = department_abbreviation
        self.course_number = course_number
        self.room = room

    def set_course(self, course):
        self.course = course
        self.department_abbreviation = course.department_abbreviation
        self.course_number = course.course_number

    def __str__(self):
        return f"Section number: {self.number}, Department Abbreviation: {self.department_abbreviation}, Course Number: {self.course_number}, Room: {self.room}"
