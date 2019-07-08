class Employee:
    def setNumberofWorkingHours(self):
        self.NumberofWorkingHours = "40"

    def displayWorkingHours(self):
        print(self.NumberofWorkingHours)


class Trainee(Employee):
    def setNumberofWorkingHours(self):
        self.NumberofWorkingHours = "45"

    def resetNumberofWorkingHours(self):
        super().setNumberofWorkingHours()


employee = Employee()
employee.setNumberofWorkingHours()
print("Number of Working Hours", end=' ')
employee.displayWorkingHours()

trainee = Trainee()
trainee.setNumberofWorkingHours()
print("Number of Trainee Working Hours", end=' ')
trainee.displayWorkingHours()
trainee.resetNumberofWorkingHours()
print("Number of  Reset Trainee Working Hours", end=' ')
trainee.displayWorkingHours()
