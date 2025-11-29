import json
from core.responses import send_json, send_404
from core.request import parse_json_body
from services.student_services import (
    service_get_all
    , service_get_one
    , service_create
)
def get_all_students(handler):
    return send_json(handler, 200, service_get_all())
def get_student(handler, student_id):
    student = service_get_one(student_id)
    return send_json(handler, 200, student) if student else send_404(handler)

def create_student(handler):
    data = parse_json_body(handler)
    new_student = service_create(data)
    return send_json(handler, 201, new_student)