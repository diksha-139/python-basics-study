class Bird:
    def __init__(self):
        print("bird is ready")
    def whoIsThis(self):
        print("bird")
    def swim(self):
        print("bird is swimming")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whoIsThis(self):
        print("penguin")
    def Run(self):
        print("penguin can run faster")
peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.Run()