from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy import String, Integer, Time, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Section(Base):
    __tablename__ = 'sections'
    department_abbreviation: Mapped[str] = mapped_column('department_abbreviation', String(10), nullable=False, primary_key=True)
    course_number: Mapped[int] = mapped_column('course_number', Integer, nullable=False, primary_key=True)
    section_number: Mapped[int] = mapped_column('section_number', Integer, nullable=False, primary_key=True)
    semester: Mapped[str] = mapped_column('semester', String(10), nullable=False, primary_key=True)
    section_year: Mapped[int] = mapped_column('section_year', Integer, nullable=False, primary_key=True)
    building: Mapped[str] = mapped_column('building', String(6), nullable=False)
    room: Mapped[int] = mapped_column('room', Integer, nullable=False)
    schedule: Mapped[str] = mapped_column('schedule', String(6), nullable=False)
    start_time: Mapped[Time] = mapped_column('start_time', Time, nullable=False)
    instructor: Mapped[str] = mapped_column('instructor', String(80), nullable=False)

    # Define the relationship to Course
    course: Mapped["Course"] = relationship('Course', back_populates='sections')

    # Uniqueness constraints
    __table_args__ = (
        PrimaryKeyConstraint('department_abbreviation', 'course_number', 'section_number', 'semester', 'section_year', name='pk_01'),
        UniqueConstraint('semester', 'section_year', 'schedule', 'start_time', 'building', 'room', name='uk_01'),
        UniqueConstraint('semester', 'schedule', 'start_time', 'instructor', name='uk_02'),
    )

    def __init__(self, department_abbreviation, course_number, section_number, semester, section_year, building, room, schedule, start_time, instructor):
        self.department_abbreviation = department_abbreviation
        self.course_number = course_number
        self.section_number = section_number
        self.semester = semester
        self.section_year = section_year
        self.building = building
        self.room = room
        self.schedule = schedule
        self.start_time = start_time
        self.instructor = instructor

    def __str__(self):
        return f"Section {self.department_abbreviation} {self.course_number}-{self.section_number}, Semester: {self.semester} {self.section_year}, Location: {self.building} Room {self.room}, Schedule: {self.schedule} {self.start_time}, Instructor: {self.instructor}"