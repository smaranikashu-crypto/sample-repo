class StudentRouter(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        add_cors_headers(self)
        self.end_headers()
    def do_GET(self):
        path = urlparse(self.path).path


        if path in ("/", "/index.html"):
            return serve_html(self)

        if path.startswith("/static/"):
            return serve_static(self)

        if path == "/api/students":
            return get_all_students(self)

        if path.startswith("/api/students/"):
            student_id = int(path.split("/")[-1])
            return get_student(self, student_id)

        return send_404(self)
    def do_POST(self):
        if self.path == "/api/students":
            return create_student(self)

        return send_404(self)
     def do_PUT(self):
        if self.path.startswith("/api/students/"):
            student_id = int(self.path.split("/")[-1])
            return update_student(self, student_id)

        return send_404(self)
     def do_DELETE(self):
        if self.path.startswith("/api/students/"):
            student_id = int(self.path.split("/")[-1])
            return delete_student(self, student_id)

        return send_404(self)

    def log_message(self, format, *args):
        print(f"[Server] {format % args}"
    