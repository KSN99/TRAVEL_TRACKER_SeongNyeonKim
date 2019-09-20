"""Place Collection for program"""

from place import Place

# Create your PlaceCollection class in this file


class PlaceCollection:
    """This class will contain a single attribute: A List of Place objects
    1.load places 2. save places 3. add place 4. get number of unvisited places 5.sort"""

    def __init__(self,):
        """For Empty place list"""
        self.list_place = []
        self.load_place()

    def __str__(self):
        return str([str(place) for place in self.list_place])

    def load_place(self):
        """Load place.csv file for place list"""
        readfile = open('place.csv','r')
        for place in readfile:
            place_string = place.split(",")
            self.list_place.append(
                [Place(place_string[0], place_string[1], int(place_string[2], place_string[3].strip()))])
        readfile.close()

    pass
