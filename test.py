class String:
    
    def __init__(self):
        self.uppercase = 0
        self.lowercase = 0
        self.vowels = 0
        self.consonants = 0
        self.spaces = 0
        self.string = ""  

    def getstr(self):
        self.string = input("Enter a string: ") 

    def countupper(self):
        for i in self.string:
            if i.isupper():
                self.uppercase += 1

    def countlower(self):
        for i in self.string:
            if i.islower():
                self.lowercase += 1

    def countvowels(self):
        for i in self.string:
            if i in ('A','a','E','e','I','i','O','o','U','u'):
                self.vowels += 1

    def countconsonants(self):
        for i in self.string:
            if i not in ('A','a','E','e','I','i','O','o','U','u'):
                self.consonants += 1

    def countspaces(self):
        for i in self.string:
            if i == " ":
                self.spaces += 1

    def execute(self):
        self.countupper()
        self.countlower()
        self.countvowels()
        self.countconsonants()
        self.countspaces()

    def display(self):
        print("The given string contains....")
        print("%d Upper case letters"%self.uppercase)
        print("%d Lower case letters" %self.lowercase)
        print("%d Wowels"%self.vowels)
        print("%d Consonants"%(self.consonants))
        print("%d Spaces"%self.spaces)

s = String()
s . getstr()
s . execute()
s . display()
