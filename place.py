
class Place:
    """Place class for represent place objects."""
    def __init__(self, title, country, priority, status):
        """initialize each attributes in places list"""
        #This simple class attributes for a place (name, country, priority, visited status).
        self.title = title
        self.country = country
        self.priority = priority
        self.status = status

    def mark_place(self, status):
        """Mark as visited for places"""
        #marking place as visited or not
        self.status = status
