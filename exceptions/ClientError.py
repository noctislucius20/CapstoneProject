class ClientError(Exception):
    def __init__(self, statusCode = 400, message = any):
        self.statusCode = statusCode
        self.message = message
        self.name = "ClientError"
        super().__init__(self.message)