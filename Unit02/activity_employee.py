class Employee:

    def __init__(self, name, salary, role):
        self.name = name                # public
        self._salary = salary           # protected
        self.role = role                # public
        self.__annual_days = 22  # private

    def __str__(self):
        return f'Employee {self.name}, salary {self._salary}, role {self.role}'

    def book_day(self):
        """Attempts to book a day off.
        Returns True if successful, False if no days left."""
        if self.__annual_days > 0:
            self.__annual_days -= 1
            print(f"Day booked. {self.__annual_days} days remaining.")
            return True
        else:
            print('You have no annual days left')
            return False

    def days_off(self):
        """Returns the remaining paid days off."""
        return f"Paid days off for the year: {self.__annual_days}"


# --- Program ---
employee1 = Employee("John", 20000, "Technical Lead")
print(employee1.days_off())

while True:
    ask = input("Do you want to book a day off? (Y/N) ").lower().strip()
    if ask == "y":
        if not employee1.book_day():  # If booking fails, stop loop
            break
    elif ask == "n":
        break
    else:
        print("Please enter Y or N.")

print(employee1.days_off())
