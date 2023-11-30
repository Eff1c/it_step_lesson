from flask import Blueprint, jsonify, request
from sqlalchemy import and_
from sqlalchemy.orm import joinedload

from app import db
from blueprints.main.forms import StudentForm, GradeForm
from blueprints.main.helpers import validate_change_student_payload, validate_change_grade_payload
from blueprints.main.schemes import StudentSchema
from models import Student, Grade

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/student_grades")
def get_student_grades():
    query = db.session.query(
        Student
    ).options(
        joinedload(Student.grades)
    )

    converter = StudentSchema(many=True)
    response = converter.dump(query)

    return jsonify(response)


@main_blueprint.route("/student", methods=["POST"])
def create_student():
    form = StudentForm()

    if form.validate_on_submit():
        new_record = Student(
            name=form.name.data,
            surname=form.surname.data,
            middle_name=form.middle_name.data
        )

        db.session.add(new_record)
        db.session.commit()

        return jsonify(success=True, id=new_record.id), 201

    return jsonify(success=False, errors=form.errors), 422


@main_blueprint.route("/student/<int:student_id>", methods=["PUT"])
def change_student(student_id):
    payload = request.get_json(force=True) or {}

    payload = validate_change_student_payload(payload)

    result = db.session.query(
        Student
    ).filter(
        Student.id == student_id
    ).update(
        payload
    )

    if not result:
        return jsonify(success=False), 404

    db.session.commit()

    return jsonify(success=True), 200


@main_blueprint.route("/grade/<int:student_id>", methods=["POST"])
def create_grade(student_id):
    form = GradeForm()
    form.fk_student.data = student_id

    if form.validate_on_submit():
        new_record = Grade(
            value=form.value.data,
            fk_student=form.fk_student.data
        )

        db.session.add(new_record)
        db.session.commit()

        return jsonify(success=True, id=new_record.id), 201

    return jsonify(success=False, errors=form.errors), 422


@main_blueprint.route("/grade/<int:student_id>/<int:grade_id>", methods=["PUT"])
def change_grade(student_id, grade_id):
    payload = request.get_json(force=True) or {}

    payload = validate_change_grade_payload(payload)

    result = db.session.query(
        Grade
    ).filter(
        and_(
            Grade.id == grade_id,
            Grade.fk_student == student_id
        )
    ).update(
        payload
    )

    if not result:
        return jsonify(success=False), 404

    db.session.commit()

    return jsonify(success=True), 200


@main_blueprint.route("/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    result = db.session.query(
        Student
    ).filter(
        Student.id == student_id
    ).delete()

    if not result:
        return jsonify(success=False), 404

    db.session.commit()

    return jsonify(success=True), 200
