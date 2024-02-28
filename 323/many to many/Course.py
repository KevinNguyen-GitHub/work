from orm_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from Department import Department

class Course(Base):
    """A catalog entry. Each course proposes to offer students who enroll in
    a section of the course an organized sequence of lessons and assignments
    aimed at teaching them specified skills.
    """
    __tablename__ = "courses"

    # Columns
    department_abbreviation = Column(String(10), ForeignKey("departments.abbreviation"), primary_key=True)  # Renamed to match the attribute name
    course_number = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    units = Column(Integer, nullable=False)

    # Relationships
    department = relationship("Department", back_populates="courses")
    sections = relationship("Section", back_populates="course")

    # __table_args__ can best be viewed as directives that we ask SQLAlchemy to
    # send to the database. In this case, that we want two separate uniqueness
    # constraints (candidate keys).
    __table_args__ = (
        UniqueConstraint("department_abbreviation", "name", name="courses_uk_01"),
        ForeignKeyConstraint([department_abbreviation], [Department.abbreviation])
    )

    def __init__(self, department: Department, course_number: int, name: str, description: str, units: int):
        self.department = department
        self.course_number = course_number
        self.name = name
        self.description = description
        self.units = units

    def set_department(self, department: Department):
        """
        Accept a new department without checking for any uniqueness.
        I'm going to assume that either a) the caller checked that first
        and/or b) the database will raise its own exception.
        :param department:  The new department for the course.
        :return: None
        """
        self.department = department
        self.department_abbreviation = department.abbreviation  # Renamed to match the column name

    def __str__(self):
        return f"Department abbrev: {self.department_abbreviation} number: {self.course_number} name: {self.name} units: {self.units}"
