from marshmallow.fields import Nested
from marshmallow.schema import BaseSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Student, Grade


class GradeSchema(SQLAlchemyAutoSchema):
    class Meta(BaseSchema.Meta):
        model = Grade


class StudentSchema(SQLAlchemyAutoSchema):
    grades = Nested(GradeSchema, many=True, only=["id", "value"])

    class Meta(BaseSchema.Meta):
        model = Student
