import json
from http.server import HTTPServer, BaseHTTPRequestHandler

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    def do_GET(self):
        path_parsed = self.path.split("/")

        if self.path == "/users":
            self._set_response(200, USERS_LIST)

        elif self.path == f"/user/{path_parsed[-1]}":
            users = list(filter(lambda x: x.get("username", False) == path_parsed[-1], USERS_LIST))
            if users:
                self._set_response(200, users[0])
            else:
                self._set_response(400, {"error": "User not found"})
        else:
            self._set_response(418)

    def do_POST(self):
        keys_valid = ['id', 'username', 'firstName', 'lastName', 'email', 'password']
        body = list(USERS_LIST)

        content_length = int(self.headers['Content-Length'])
        req = json.loads(self.rfile.read(content_length).decode('utf-8'))

        id_list = [data["id"] for data in body]

        if self.path == "/user":
            if list(req.keys()) == keys_valid and req["id"] not in id_list:
                body.append(req)
                self._set_response(201, body[-1])
            else:
                self._set_response(400, {})
        elif self.path == "/user/createWithList":
            body = list(USERS_LIST)
            for user_req in req:
                if list(user_req.keys()) != keys_valid or user_req.get("id", False) in id_list:
                    return self._set_response(400, {})
            body.append(req)
            self._set_response(201, req)
        else:
            self._set_response(418)

    def do_PUT(self):

        body = list(USERS_LIST)
        path_parsed = self.path.split("/")
        content_length = int(self.headers['Content-Length'])
        req = json.loads(self.rfile.read(content_length).decode('utf-8'))
        if self.path == "/user/user_not_found":
            self._set_response(404, {"error": "User not found"})

        elif self.path == f"/user/{path_parsed[-1]}":
            for user_data in body:
                if user_data.get("username", False) == path_parsed[-1]:
                    user_data.update(req)
                    return self._set_response(200, body[0])
                else:
                    return self._set_response(400, {"error": "not valid request data"})

        else:
            self._set_response(418)

    def do_DELETE(self):
        body = list(USERS_LIST)
        path_parsed = self.path.split("/")
        if self.path == f"/user/{path_parsed[-1]}":
            for data_user in body:
                if data_user.get("id", False) == int(path_parsed[-1]):
                    body.remove(data_user)
                    return self._set_response(200, {})
            self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(418)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
