"""Class example."""

class Person:
    """Person superclass."""

    def __init__(self, fname, lname):
        """Initialize Person.

        Args:
            fname (str): First name
            lname (str): Last name
        """
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        """Print the person's first and last name."""
        print(self.firstname, self.lastname)

class Student(Person):
    """Student subclass.

    Args:
        Person (Person): A person.
    """

    def __init__(self, fname, lname, year):
        """Initilalize Student.

        Args:
            fname (str): First name
            lname (str): Last name
            year (int): Graduation year
        """
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        """Print a welcome statement for the student."""
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
