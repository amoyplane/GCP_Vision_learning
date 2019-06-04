class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Info:
    def __init__(self, points=[], direction=1, text='', trans=''):
        self.vertexs = points
        self.direct = direction
        self.text = text
        self.trans = trans

    def showInfo(self):
        print(self.vertexs + '\n')
        print(self.direct + '\n')
        print(self.text + '\n')
        print(self.trans + '\n')
