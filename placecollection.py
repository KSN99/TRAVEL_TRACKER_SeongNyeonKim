from place import Place


class PlaceList:
    """PlaceList class for reading list program"""
    def __init__(self, ):
        """Constructor - create empty place list  """
        # To empty the list
        self.places = []



    def sorting(self, sort_method):
        """Sort places list based on Title. country. and priority"""
        #to sort data by the key passed, then by priority
        if sort_method == "Country":
            self.places.sort(key=lambda i: (i[0].country, i[0].title))
        elif sort_method == "Title":
            self.places.sort(key=lambda i: i[0].title)
        elif sort_method == "Priority":
            self.places.sort(key=lambda i: (i[0].priority, i[0].title))
        else:
            self.places.sort(key=lambda i: (i[0].status, i[0].title))
        # append te place title country and priority
    def append_Places(self, title, country, priority):
        """Add a single place to main place list"""
        # To adding place
        self.places.append([Place(title, country, priority, 'y')])

    def place_get(self, title):
        """Get a single place based on its title"""
        # Method to let user selected single place object.
        for place in self.places:
            if place[0].title == title:
                return place[0]

    def tovisit_places_count(self):
        """Get the number of unvisited places need to visit"""
        #to detect wether this place already been to or not
        place_tovisit = 0
        for place in self.places:
            if place[0].status == 'y':
                place_tovisit += 1
        return place_tovisit

    def visited_places_count(self):
        """Get the number of visited places need to visit"""
        #to detect wether this place already been to or not
        visited_places = 0
        for place in self.places:
            if place[0].status == 'n':
                visited_places += 1
        return visited_places


    def load_places(self):
        #To laod the csv field from the place.csv
        filereader = open('place.csv', 'r')
        for place in filereader:
            place_string = place.split(",")
            self.places.append(
                [Place(place_string[0], place_string[1], int(place_string[2]), place_string[3].strip())])

        filereader.close()

    def load_to_csv(self):
        """load places in the csv file in a format"""
        #Write the new data to the place.csv field
        filewriter = open('place.csv', 'w')
        for place in self.places:
            filewriter.write(
                place[0].title + "," + place[0].country + "," + str(place[0].priority) + "," + place[
                    0].status + "\n")

        filewriter.close()




