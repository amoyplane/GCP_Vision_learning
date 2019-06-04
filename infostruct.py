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
        for vet in self.vertexs:
            print('(' + str(vet[0]) + ',' + str(vet[1]) + ')')
        print(self.direct)
        print(self.text)
        print(self.trans)
