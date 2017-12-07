class Venue:
    id = None
    name = ""
    capcity= -1
    limited_availability = False
    partition = 1
    in_door = True
    def __init__(self,id,name, capcity, limited_availability=False, partition =1, in_door =True):
        self.id = id
        self.name = name
        self.capcity = capcity,
        self.limited_availability = limited_availability
        self.partition
        self.in_door = in_door

    def __eq__(self,other):
        return self.id == other.id and self.name == other.name and self.capcity == other.capcity
    def __ne__ (self, other):
        return not self.__eq__(other)
