class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Info:
    def __init__(self, points=[], direction=1, text='', trans='', id=0):
        self.vertexs = points
        self.direct = direction
        self.text = text
        self.trans = trans
        self.id = id

    def showInfo(self):
        print('Info id = ', end=' ')
        print(self.id)
        for vet in self.vertexs:
            print('(' + str(vet[0]) + ',' + str(vet[1]) + ')', end=' ')
        print()
        print('Direction = ', end=' ')
        print(self.direct)
        print(self.text)
        print(self.trans)


if __name__ == '__main__':
    a = Info([(11, 222), (33, 455), (15, 326), (237, 1348)], 1, 'abc', 'def', 2)
    a.showInfo()
