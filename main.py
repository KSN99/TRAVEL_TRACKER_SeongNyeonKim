"""
Name: SeongNyeon Kim
Date: 17/09/2019
Brief Project Description: In this Assignment2, I will create both a console program and a Graphical User
Interface (GUI) program similar as my first assignment by using Python3 and the Kivy toolkit,
I will use techniques like selection,repetition, exceptions, lists, dictionaries, and function.
GitHub URL: https://github.com/KSN99/jcus-cp1404-assg2-KSN99
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from placecollection import PlaceList
class TravelTracker(App):
    """ Main program - Kivy app for displaying places list"""
# import csv for opening the csv field
# import the copy for me to control the data in the csvkjkl

    def __init__(self, **kwargs):
        """Constructor - set up the data model"""
        #this is the text will shown on the GUI with the app.kv field.
        super().__init__(**kwargs)
        self.place_list = PlaceList()
        self.sort_label = Label(text="Sort by:")
        self.spinner = Spinner(text='Country', values=('Country', 'Title', 'Priority', 'Visited'))
        self.append_Places_label = Label(text="Add Place...")
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")
        self.country_label = Label(text="Country:")
        self.country_text_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority:")
        self.priority_text_input = TextInput(write_tab=False, multiline=False)
        self.append_Places_button = Button(text='Add Place')
        self.clear_button = Button(text='Clear')


    def build_left_widgets(self):
        """Build the kivy GUI"""
        #show the widget in the kivy also inlcuding the sorting part by sorting thre conuntry and priority and those botton on the kivy
        """Button for the kivy"""
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.append_Places_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.country_label)
        self.root.ids.leftLayout.add_widget(self.country_text_input)
        self.root.ids.leftLayout.add_widget(self.priority_label)
        self.root.ids.leftLayout.add_widget(self.priority_text_input)
        self.root.ids.leftLayout.add_widget(self.append_Places_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)
        self.spinner.bind(text=self.sorting_places)
        self.append_Places_button.bind(on_release=self.append_Places_handler)
        self.clear_button.bind(on_release=self.fields_text_clearer)


    def append_Places_handler(self, *args):
        """Error handler when user input wrong value"""
        #this is the requirment of the input.
        if str(self.title_text_input.text).strip() == '' or str(self.country_text_input.text).strip() == '' or str(
                self.priority_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        #every blank must be put in
        else:
            try:

                if int(self.priority_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Priority must be >= 0"
        #the number in this input must bigger than 0
                else:
                    self.place_list.append_Places(self.title_text_input.text, self.country_text_input.text,
                                            int(self.priority_text_input.text))
                    self.place_list.sorting(self.spinner.text)
                    self.fields_text_clearer()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_widgets()

            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"
             # the number in this input must be the interager


        if str(self.title_text_input.text).strip() == '' or str(self.country_text_input.text).strip() == '' or str(
                self.priority_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be filled"
        else:
            try:

                if int(self.priority_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Priority must be >= 0"
                # the number in this input must bigger than 0
                else:
                    self.place_list.append_Places(self.title_text_input.text, self.country_text_input.text,
                                            int(self.priority_text_input.text))
                    self.place_list.sorting(self.spinner.text)
                    self.fields_text_clearer()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_widgets()
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"
            # the number in this input must be the interager

    def build(self):
#The travel tracker will apper on the top of the kivy system.
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.place_list.load_places()
        self.place_list.sorting('Country')
        self.build_left_widgets()
        self.build_right_widgets()
        return self.root




    def visit_Places(self, button):
        """To distinguish whether the visited place or not"""
        #determint what should be display below the GUI
        if self.place_list.place_get(button.id).status == 'n':
            self.place_list.place_get(button.id).status = 'y'
            self.root.ids.bottomLayout.text = "You need to visit " + str(self.place_list.place_get(button.id).title)

        else:
        #if the lastest button is visited one new place, this will be trigger
            self.place_list.place_get(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You have visited " + str(self.place_list.place_get(button.id).title) + ". Great travelling!"

        self.sorting_places()
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()

    def build_right_widgets(self):
        # display the top column shown how many place left for visit.

            self.top_label.text = "To Visit: " + str(self.place_list.tovisit_places_count())

            for place in self.place_list.places:
            #the text change by the status of the buttom.
                if place[0].status == 'n':
                    place_button = Button( text= place[0].title + " in " + place[0].country + ", priority " + str(place[0].priority) + " (Visited)",
                                           id=place[0].title)
                    #this is the place already been visited


                else:
                    place_button = Button(
                        text= place[0].title + " in " + place[0].country + ", priority " + str(place[0].priority) + " ",
                        id=place[0].title)
                    #this is the place have not been visited

                    place_button.background_color = [0, 80, 88, 0.3]

                place_button.bind(on_release=self.visit_Places)
                self.root.ids.rightLayout.add_widget(place_button)

    def fields_text_clearer(self, *args):
        #to clear all the input
        self.title_text_input.text = ""
        self.country_text_input.text = ""
        self.priority_text_input.text = ""
        self.root.ids.bottomLayout.text = ""





    def sorting_places(self, *args):
        """sort places"""
        #sorting the place by the Country, Title, Priority and Visited
        self.place_list.sorting(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()

    def on_stop(self):
        #save to data to the place csv field
        self.place_list.load_to_csv()


if __name__ == '__main__':
    # For installing kivy program
    app = TravelTracker()
    app.run()























