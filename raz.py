class person:

    def __init__(self,year,name):
       self.year = year
       self.name = name

    def printInfo(self):
          print(f"year: {self.year} , name: {self.name}")

    def add_to_year(self,number):
        print(f"the year before adding number {self.year} and after adding is {self.year + number}")

p1 = person(2001,"raz")

p1.printInfo()

p1.add_to_year(9)

print("at lllllllllllll5656")