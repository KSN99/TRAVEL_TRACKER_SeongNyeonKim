# Create your Place class in this file


class Place:
    """Simple class with the required attributes for a place and the methods"""
    pass
    def __init__(self, name, country, priority, status):
        """The __init__() function is called automatically every time the class is being used to create a new object."""
        self.name=name
        self.country=country
        self.priority=priority
        self.status=status

    def __str__(self):
        """Two methods to mark the place as unvisited and visited"""
        if self.status == "v":
            return "Unvisited place {} in {} ({})".format(self.name, self.country, self.status)
        else:
            return "Visited place {} in {} ({})".format(self.name, self.country, self.status)

    def m_visited(self, *args):
        """visited place"""
        if self.status == "v":
            self.status == "n"
            return self.status
