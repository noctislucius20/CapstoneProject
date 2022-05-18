from exceptions.ClientError import ClientError

class InvariantError(ClientError):
    def __init__(self, message):
        self.message = message
        self.name = "InvariantError"
        super().__init__(self.message)