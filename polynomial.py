class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
    
        p1_str = "(" + repr(self.p1) + ")" if isinstance(self.p1, Add) or isinstance(self.p1, Sub) else repr(self.p1)
        p2_str = "(" + repr(self.p2) + ")" if isinstance(self.p2, Add) or isinstance(self.p2, Sub) else repr(self.p2)

        return p1_str + " * " + p2_str


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        p1_str = "(" + repr(self.p1) + ")" if isinstance(self.p1, Add) or isinstance(self.p1, Sub) else repr(self.p1)
        p2_str = "(" + repr(self.p2) + ")" if isinstance(self.p2, Add) or isinstance(self.p2, Sub) else repr(self.p2)

        return p1_str + " / " + p2_str
    


poly = Add( Add( Int(4), Int(3)), Add( X(), Div( Int(1), Sub( Mul(X(), X()), Int(1)))))
print(poly)

poly_2 = Add(Div(Mul(X(), X()), Add(Int(25), X())), Mul(Sub(X(), Int(26)), Add(X(), Int(27))))
print(poly_2)

poly_3 = Mul(Add(Sub(Div(Mul(Int(39), Int(40)), Add(Int(41), Int(42))), Int(43)), Int(44)), X())
print(poly_3)
