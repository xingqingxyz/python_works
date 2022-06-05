


class people:
    def __init__(self, vae: object, var1: object) -> object:
        """

        :rtype: object
        """
        self.vae = vae
        self.__private_var1 = var1

    def get(self) -> object:
        print(self.__private_var1)

    def set(self, var):
        self.__private_var1 = var
        print(self.__private_var1)

print("hello")
adc.get()
adc = people(2, 3)
adc.set(45)