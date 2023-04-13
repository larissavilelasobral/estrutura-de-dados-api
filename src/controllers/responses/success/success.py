class SuccessResponse:
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'success': {'message': self.message, 'status_code': self.status_code}}
