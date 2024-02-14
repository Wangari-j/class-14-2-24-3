class fruits:
    shape = " "
    colour = " "

    def fruit_desc(self):
        print("Oranges have many seeds.")

    def fruitType(self):
        print("Most citrus fruits originate from the Mediterranean.")

fruits1 = fruits()
fruits2 = fruits()

fruits1.shape = "round"
fruits2.colour = "orange"

print(fruits1.shape)
print(fruits2.colour)

fruits2.fruit_desc()
fruits1.fruitType()

#the above is a good examples of classes, attributes, functions and objects basic concepts.
