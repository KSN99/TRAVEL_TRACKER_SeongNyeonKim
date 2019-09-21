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

    def save_places(self):
        """Save places in CSV file"""
        writefile = open('place.csv','w')
        for place in self.list_place:
            writefile.write(place[0].name + "," +place[0].country +","
                            + str(place[0].priority)+"," + place[0].status + "\n")
        writefile.close()

    def add_place(self, name, country, priority):
        """Add a new place in csv file"""
        self.list_place.append([Place(name,country,priority, 'y')])

    def get_num_unvisited_place(self):
        """Get number of unvisited places """
        visited_places =0
        for place in self.list_place:
            if place[0].status == 'v':
                visited_places += 1
        return visited_places

    def sort(self, sort_list):
        """Sort by the key passed in, then by priority"""
        if sort_list == "name":
            self.list_place.sort(key=lambda i: i[0].name)
        elif sort_list == "country":
            self.list_place.sort(key=lambda i: (i[0].country, i[0].name))
        else:
            self.list_place.sort(key=lambda i: (i[0].priority, i[0].name))

    pass
