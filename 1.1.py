class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

sm = StringManipulator()
sm.getString()
sm.printString()