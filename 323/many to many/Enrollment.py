from orm_base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Enrollment(Base):
    __tablename__ = 'enrollments'
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id'), primary_key=True)
    student = relationship('Student', back_populates='enrollments')
    section = relationship('Section', back_populates='enrollments')

    def __init__(self, student, section):
        self.student = student
        self.section = section

    def enroll_student_in_section(self, student, section):
        if student not in self.student and section not in self.section:
            self.student.append(student)
            self.section.append(section)

    def unenroll_student_from_section(self, student, section):
        if student in self.student and section in self.section:
            self.student.remove(student)
            self.section.remove(section)

    def list_students_in_section(self, section):
        students_in_section = [student for student, sec in zip(self.student, self.section) if sec == section]
        return students_in_section

    def list_sections_for_student(self, student):
        sections_for_student = [sec for stu, sec in zip(self.student, self.section) if stu == student]
        return sections_for_student

    def __str__(self):
        return f"Enrollment: Student ID - {self.student_id}, Section Number - {self.section_id}"
