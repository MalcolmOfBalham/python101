class Animal(object):
    pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

# this is from ex44


class Parent(object):
    def implicit(self):
        print("PARENT: explicit")

    def override(self):
        print("PARENT: override")

    def altered(self):
        print("PARENT: altered")


class Child(Parent):
    pass

    def override(self):
        print("CHILD: override")

    def altered(self):
        print("CHILD: BEFORE PARENT altered")
        super(Child, self).altered()
        # note that this does exactly the same thing
        super().altered()
        print("CHILD: AFTER PARENT altered")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

pytdad.altered()
son.altered()


# now using composition
class Other(object):

    def override(self):
        print("OTHER override")

    def implicit(self):
        print("OTHER implicit")

    def altered(self):
        print("OTHER altered")


class OtherChild(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD before OTHER altered")
        self.other.altered()
        print("CHILD after OTHER altered")

    # son2 = Other() 
    son2 = OtherChild()
    son2.implicit()
    son2.override()
    son2.altered()
