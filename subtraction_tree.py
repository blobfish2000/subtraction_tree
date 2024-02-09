import random
import re


    

class ParenNode:
    child = None
    scalar = None
    depth = None
    
    def calculate(self):
        return (self.scalar * self.child.calculate()[0], self.scalar * self.child.calculate()[1])

    def populate(self, max_depth = 7):
        if random.random() < 0.8:
            self.scalar = 1
        else:
            self.scalar = random.randint(-5,5)
            if self.scalar == 0:
                self.scalar = 1
        if self.depth >= max_depth:
            self.child = ValueNode(random.randint(-10,-1))
            return
        if random.random() < 0.9:
            self.child = InfixNode(None, None, depth=self.depth+1)
            self.child.populate( max_depth)
        else:
            self.child = ValueNode(random.randint(-10,-1))
    def __init__(self, child, scalar,
                 depth=0):
        self.child = child
        self.depth = depth
        self.scalar = scalar
    def __str__(self):
        if self.scalar == 1:
            return "(" + str(self.child) + ")"
        else:
            return str(self.scalar) + "(" + str(self.child) + ")"

class InfixNode:
    a = None
    b = None
    op = None
    depth = None

    def calculate(self):
        if self.op == "-":
            return (self.a.calculate()[0] - self.b.calculate()[0],
                    self.a.calculate()[1] - self.b.calculate()[1])
        else:
            return (self.a.calculate()[0] + self.b.calculate()[0],
                    self.a.calculate()[1] + self.b.calculate()[1])


    def populate(self, max_depth = 7):
        
        if random.random() < 0.8:
            self.op = "-"
        else:
            self.op = "+"

        if self.depth >= max_depth:
            self.a = ValueNode(random.randint(-10,10))
            self.b = ValueNode(random.randint(0,10))
            return

        if random.random() < 0.8:
            self.a = ParenNode(None, None, self.depth+1)
            self.a.populate(max_depth)
        else:
            self.a = ValueNode(random.randint(-10,10))

        if random.random() < 0.8:
            self.b = ParenNode(None, None, self.depth+1)
            self.b.populate(max_depth)
        else:
            self.b = ValueNode(random.randint(0,10))

    def __init__(self, a, b, op = "-", depth=0):
        self.a = a
        self.b = b
        self.depth = depth
        self.op = op

    def __str__(self):
        return str(self.a) + " " + self.op + " " + str(self.b)

class ValueNode:
    value = None
    depth = None

    def calculate(self):
        if self.variable:
            return (0,self.value)
        else:
            return (self.value,0)

    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.variable = False
        if random.random() < 0.2:
            self.variable = True
            if self.value == 0:
                self.value = 1

    def __str__(self):
        if self.variable:
            if self.value == -1:
                return "-k"
            elif self.value == 1:
                return "k"
            else:
               return str(self.value)+"k"
        else:
            return str(self.value)

sample = "(((((((-1 - 7x) + (((-7 - 7x) + (4 + 4x)) - 3)) - (((-4x - 2x) + 4x) - (-4x + (9 - 1x)))) + (((((-5 - 3x) - 5x) + 6x) - ((-5x + 10) - 8x)) - ((-2x - (-7x - (-10x + 8x))) - (((((-8x + 8) - 5x) - (8x + 10)) + 10x) + 9)))) + ((9x + 6x) + (((((-2x - (4x - 10)) - 5) - 5) + ((((1 - (-6 + 10x)) - ((8x - 3x) - (8x + 3))) + ((-4 - 2x) + 3x)) - ((((5 + 7x) + 3) - (-4 - 9x)) + ((((-3x + (-5x - (3x + 7))) + 5x) - (-9 - (4 + (-10x + 8x)))) + 10)))) + ((6x + 10) + (((((5 + 1) + 4) - (-6x + 10)) - ((-3 - 8) + ((-8 - 8x) - 8x))) + (((2 + 8x) + ((-10x + 1x) + (-6x + 10))) - ((-9x + 4x) - 1))))))) + ((((-8x + (9x + 3x)) + ((1 - ((10 - (-8 + 6x)) - 3x)) - ((-1x + (-10 - (-3x + 7x))) + 1))) - (-6x + (-1x + (-4x + 5x)))) + ((-6x + 7) - (6x - (((3x + (3 + 10x)) - 10) - (((((-8x + 1x) - (((-7x + 5x) - 1) + 3x)) + 2) - 5) + (5 + ((-6x - 8) + 5)))))))) + ((3x - 3) - 1)) + ((((((-5 + (((-8x - 4) + 10x) + 2)) - (-10 - 8x)) + (((-9x + 6x) - (8 - 7x)) - (10 - (-2x + 5)))) + (-6x + (9 - (7x + 8x)))) + ((((5x - (2x + 5x)) - (((-2x + 3x) + ((3x - 10) - (3 + (-7 - (-2 - 3x))))) + (-10x - ((3 + (-5x + ((-9 + 2) - 2x))) + (-2x + 7))))) - (-1x + (-7x - 5x))) - ((-3 - (1x + (4 + ((2 - 5) - 9x)))) - (-8x - 10)))) + (((((2 + ((7 + 8) - ((-10x + (9x - (-8x - 9))) - 8x))) + (((1 - 10) - ((-6x + 9x) - (6 + 1))) - ((((-3x + 10) - (-1 - 9x)) - (((-7 + (-4x + (-7x + 4x))) + (5 - (4 - 4x))) - ((-8 + 6x) + (((-10 + 3x) + (3 - 7)) - 3x)))) + (((-1x + 10x) - 2) + 10))))) + ((10x - (7 + 6)) - ((-9x - 7x) + (-4 + (-4 - (-3x + 1x)))))) + (((((((-9 - 10) - (5x + 2)) - (8x - 3)) - 8x) - ((-8 - 8x) - 3)) - ((((((2 + ((-10x - (7x - 1)) + (-3 + 9))) + (-3 + ((-7x + 5) - (-6x + 8x)))) - (8 - 6)) + (((8x - 4x) - 8) - (((8 - 4) + 9x) - 6x))) + (-7x - (-9 + (4 + 4)))) - (10 - (-1x + 9x)))) - ((5 - 4) + (9x + (((((9 + 7x) - ((-10x - 10x) + (6 + 2))) + (-6x + (-1 + (-5x - (-1 - 4x))))) + (-8 + 3)) - (-10 - 10)))))) - ((((7 + ((10x + (1 - 7x)) - 9)) - ((((-2 + 5x) + 4x) - (-7 + ((9 + (-4 + 8x)) - ((7 + 7) - 7x)))) + ((-7 - 9x) + (((-2 - 5) + (9x + 8)) + 3)))) - 1) + (8x + ((-4x - 1x) + 1x)) + 5)))"

def lex(code_string):
    re_dict={"coef" : "([0-9]+)\(",\
             "lparen" : "\(",\
             "rparen" : "\)",\
             "variable" : "-?[0-9]+x",\
             "integer" : "-?[0-9]+",\
             "plus" : " \+ ",\
             "minus" : " - "}
    for lexeme_class in re_dict:
        re_dict[lexeme_class] = re.compile(re_dict[lexeme_class])

    lexeme_list = []
    index = 0
    while index < len(code_string):
        matched = False
        for lexeme_class in re_dict:
            pattern = re_dict[lexeme_class]
            match = pattern.match(code_string, index)
            if match:
                matched = True
                group = match[0]
                print(f"head was: {code_string[index:min(index+5,len(code_string))]}...")
                index += len(group)
                if len(match.groups())>0:
                    group = match[1]
                
                if lexeme_class == "integer":
                    group = int(group)
                if lexeme_class == "variable":
                    group = int(group[:-1])

                lexeme_list.append((lexeme_class, group))
                print(f"lexed {lexeme_list[-1]} and head is now: {code_string[index:min(index+5,len(code_string))]}...")
                break
        if matched == False:
            print("no match at:", code_string[index:min(index+5,len(code_string))])
            return lexeme_list

    return lexeme_list

def parse(lexeme_list):
    #
    head = lexeme_list[0]
    match head:
        case 


n = InfixNode(None, None)
n.populate(10)
print(str(n))
s, v = n.calculate()
print(str(s) + " + " + str(v) + "k")
