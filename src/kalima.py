class Kalima():
    def __init__(self, kalima_id):
        self.token=str() # 'alh' or 'ilaa'
        self.connot=list()
        """
        [
            ['fruit', 'produce'],
            ['fruit', 'become'],
            ['produce', 'pleasure]',
            ]
        """
        # connotations order is prime
        self.adds=list()
        """
        [
            '\d{3}\.\d{3}\.\d{3}',
            '\d{3}\.\d{3}\.\d{3}',
            ]
        """
        
class Part(Kalima):
    def __init__(self):.
        pass

class Word(Kalima):
    def __init__(self):
        self.root=list() # ['a', 'l', 'h']
        # letter order is the Arabic order: [a,l,h]
        """
        store root as a matrix? but loses letter order:
            
            headers: kalima_id, a, b, t, l, h
                             1, 1, 0, 0, 1, 1
                             2, 1, 1, 0, 0, 0

            headers: kalima_id, p0, p1, p2, p3
                             1,  a,  l,  h
                             2,  i,  l,  m
        """

