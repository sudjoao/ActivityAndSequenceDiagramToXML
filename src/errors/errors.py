class Error(Exception):
    pass

class OrderError(Error):
    def __init__(self, message):
        self.message = message

class MissMergeError(Error):
    def __init__(self, message):
        self.message = message
