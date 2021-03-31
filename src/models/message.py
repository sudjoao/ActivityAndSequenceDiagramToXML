class Message():
    def __init__(self, name, orig, dest, prob, _type):
        self.name = name
        self.orig = orig
        self.dest = dest
        self.prob = prob
        self.type = _type

    def set_name(self, name):
        self.name = name
    
    def set_orig(self, orig):
        self.orig = orig
    
    def set_dest(self, dest):
        self.dest = dest
    
    def set_prob(self, prob):
        self.prob = prob

    def set_type(self, _type):
        self.set_type = _type
