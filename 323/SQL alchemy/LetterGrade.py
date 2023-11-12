from sqlalchemy import Date, ForeignKey, CheckConstraint, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from Enrollment import Enrollment


class LetterGrade(Enrollment):
    __tablename__ = "letter_grade"
    # I HAD put Integer after the table name, but apparently it picks that up from the parent PK.
    letterGradeId: Mapped[int] = mapped_column('letter_grade_id',
                                               ForeignKey("enrollments.enrollment_id",
                                                          ondelete="CASCADE"), primary_key=True)
    minAcceptable: Mapped[str] = mapped_column('min_acceptable', String(1),
                                               CheckConstraint("min_acceptable IN('A', 'B', 'C', 'D', 'F')",
                                                               name="grade_constraint"),
                                               nullable=False)
    # Add relationship with back_populates
    enrollment = relationship("Enrollment", back_populates="letter_grade")

    __mapper_args__ = {"polymorphic_identity": "letter_grade"}

    def __init__(self, section, student, min_acceptable: str):
        super().__init__(section, student)
        self.minAcceptable = min_acceptable

    def __str__(self):
        return f"LetterGrade Enrollment: {super().__str__()}"
