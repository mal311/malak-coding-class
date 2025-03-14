class Employee :
    #Initialising (constructor)
    def __init__(self):
        print('emplyoee created.')

    #deleting (destructor)
    def __del__(self):
        print('Destructor called, Employee deleted')

obj= Employee()
del obj