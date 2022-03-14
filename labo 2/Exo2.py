class Person :
    def __init__(self, name, home, properties = None):
        self.name = name
        self.home = home
        self.properties = properties or []

    @property
    def is_owner(self):
        return len(self.properties) > 0
    @property
    def address(self):
        #retourner l'address en fonction du home => numéro de property et @ du building
        pass
        

class Property :
    def __init__(self, building, owner = None, garage = False, number = None, occupiers = None):
        self.building = building
        self.owner = owner
        self.garage = garage
        self.number = number
        self.occupiers = occupiers or []
class Building :
    def __init__(self, address, properties = None):
        self.address = address
        self.properties = properties or []
    @property
    def nb_properties(self):
        #retourn le npmbre de propriété
        pass
