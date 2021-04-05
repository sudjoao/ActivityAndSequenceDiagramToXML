class Error(Exception):
    pass

class OrderError(Error):
    def __init__(self, message):
        self.message = message

class MissMergeError(Error):
    def __init__(self, message):
        self.message = message

class MessageFormatException(Error):
    def __init__(self, message):
        self.message = message

class EmptyOptionalFragment(Error):
    def __init__(self, message):
        self.message = message
