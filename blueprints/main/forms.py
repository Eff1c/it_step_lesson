from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from app import db
from models import Student


def validate_student_is_exist(form, field):
    student = db.session.query(
        Student.id
    ).filter(
        Student.id == field.data
    ).limit(1).scalar()

    if not student:
        raise ValidationError(
            'Студента за таким id не знайдено'
        )


class StudentForm(FlaskForm):
    name = StringField(
        "Ім'я",
        validators=[
            DataRequired("Поле обов'язкове для заповнення"),
        ]
    )
    surname = StringField(
        "Прізвище",
        validators=[
            DataRequired("Поле обов'язкове для заповнення"),
        ]
    )
    middle_name = StringField(
        "По батькові",
        validators=[
            DataRequired("Поле обов'язкове для заповнення"),
        ]
    )


class GradeForm(FlaskForm):
    value = IntegerField(
        "Оцінка",
        validators=[
            DataRequired("Поле обов'язкове для заповнення"),
        ]
    )
    fk_student = IntegerField(
        "Ідентифікатор студента",
        validators=[
            DataRequired("Поле обов'язкове для заповнення"),
            validate_student_is_exist
        ]
    )
