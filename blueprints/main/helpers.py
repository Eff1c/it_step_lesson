from flask import abort, make_response, jsonify


def validate_change_payload(payload: dict, required_keys: set) -> dict:
    payload_valid_keys = required_keys.intersection(payload.keys())

    if not payload_valid_keys:
        response_data = jsonify(
            success=False,
            message="Невалідний payload"
        )
        abort(make_response(response_data, 422))

    valid_payload = {key: payload[key] for key in payload_valid_keys}

    return valid_payload


def validate_change_student_payload(payload: dict) -> dict:
    required_keys = {"name", "surname", "middle_name"}
    valid_payload = validate_change_payload(payload, required_keys)

    return valid_payload


def validate_change_grade_payload(payload: dict) -> dict:
    required_keys = {"value"}
    valid_payload = validate_change_payload(payload, required_keys)

    return valid_payload
