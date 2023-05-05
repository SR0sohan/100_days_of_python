class person:
    def __init__(self, n, o):
        self.name = n
        self.occ  = o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("sohan", "developer")
b = person("silota", "life")
a.info()
b.info()