class ApiException(Exception):
    def __init__(self, message, status_code):
        super().__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'error': {'message': self.message, 'status_code': self.status_code}}


class ErrorResponse(Exception):
    def __init__(self, message, status_code):
        super().__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'error': {'message': self.message, 'status_code': self.status_code}}

