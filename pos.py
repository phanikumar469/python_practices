class Tree:
    colour = "green"
    def __init__ (self,name,height):
        self.name = name
        self.height = height
    def Tree_type(self):
        print("Tree name", self.name, "Tree height", self.height)

tree1 = Tree(name="Mango", height="5cm")
tree2 = Tree(name = "lemon",  height = "6.5")
tree1.Tree_type()
tree2.Tree_type()

mystring = "Hello World"
rev = ""
for ch in mystring:
    rev = ch + rev
print(rev)

mystring = "inahp olleh"
rev = mystring[::-1]
print(rev)

num = int(input("Enter a multiplication table "))
for i in range(1,11):
    result = num * i
    print(f"{num} * {i} = {result}")

n = 5
for i in range(0,11):
    result = n * i
    print(f"{n} * {i} = {result}")