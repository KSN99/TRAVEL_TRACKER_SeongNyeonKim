"""
Name: SeongNyeon Kim
Date: 19.09.2019
Brief Project Description: This project is for creating both a console and a GUI program by using python and Kivy.
GitHub URL: https://github.com/JCUS-CP1404/jcus-cp1404-assg2-KSN99
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App


class TravelTrackerApp(App):
    """For installing Kivy application """
    total_text =StringProperty()
    status_text=StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_list = PlaceList()

    def build(self):
        """Build the Kivy Gui"""
        self.name = "Travel Tracker 2.0"
        self.root = Builder.load_file('app.kv')
        self.place_list.sort('name')
        self.building_widgets()
        self.place_buttons()
        return  self.root


    pass


if __name__ == '__main__':
    TravelTrackerApp().run()
