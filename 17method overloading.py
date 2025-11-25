#Method overriding occurs when a child class provides a new implementation of a method that is already defined in its parent class.
#It allows a subclass to customize or replace the behavior of a method inherited from the superclass.

class Bank:
    def interest_rate(self):
        print("General interest rate is 5%")

class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate is 6.5%")

class ICICI(Bank):
    def interest_rate(self):
        print("ICICI interest rate is 7%")

# Create objects
b = Bank()
s = SBI()
i = ICICI()

# Call the method
b.interest_rate()   # Output: General interest rate is 5%
s.interest_rate()   # Output: SBI interest rate is 6.5%
i.interest_rate()   # Output: ICICI interest rate is 7%
