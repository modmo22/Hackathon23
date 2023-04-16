from Abstract.stage import Stage
class Level1(Stage):
    def __init__(self, WIN):
        super().__init__(WIN)
        print(__file__)
        
    def run(self):
        return -1