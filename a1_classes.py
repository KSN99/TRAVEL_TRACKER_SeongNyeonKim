"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place

#TravelTracker

#Main

print("Welcome to Tavel Tracker")
places = []
place_file = "place.csv"

def load_place():
    #place_file = "place.csv"
    # places = []
    with open(place_file, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')

            place = [parts[0], parts[1], parts[2], parts[3]]
            places.append(place)

    return places


def main():

    print("Travel Tracker 1.0 -by SeongNyeon Kim ")
    places = load_place()
    print("{} places loaded".format(len(places)))
    number_of_places = count_places()
    while True:
        print("Menu:")
        print("L-List places")
        print("A-Add new place")
        print("M-Marked a place as visited")
        print("Q-Quit")
        choice = input(">>>").upper()
        if choice == "L":
            l_place(places)
        elif choice == "A":
            a_place(places)
        elif choice == "M":
            l_place(places)
            m_place(places)
        elif choice == "Q":
            save_places(places)
            print("{} places saved to place.csv :)".format(len(places)))
            break
        else:
            print("invalid menu choice")

def count_places():
    places_data = 0
    for place in range(len(places)):
        places_data += 1

        return places_data

def l_place(places):

    visitedplace = 0
    unvisitedplace = 0
    #for each in places:
    for i, each in enumerate(places):
        if each[3] == "n":
            print("{:2}. {} {:32}- {:29}({:3})".format(i, "*",  each[0], each[1], each[2]))
            unvisitedplace += 1
        elif each[3] == "v":
            print("{:2}.  {:32}- {:29}({:3})".format(i,  each[0], each[1], each[2]))
            visitedplace += 1
    print("{} places, You still want to visit {} places ".format(count_places(), unvisitedplace))
    return places


def a_place(places):

    while True:
         name= input("Name:")
         if name=="":
             print("Input cannot be blank")
         else:
             break
    while True:
         country = input("Country:")
         if country == "":
             print("Input cannot be blank")
         else:
             break
    while True:
         try:
             priority = int(input("Priority:"))
             if priority < 0:
                 print("Number must be >= 0")
             else:
                 break
         except:
             print("Invalid input; enter a valid number")
    print("{} by {} ({}) added to place list".format(name, country, priority))
    new_place = [name, country, priority, "n"]
    places.append(new_place)
    return places


def m_place(places):

    required=0
    for each in places:
        if each[3] == "v":
            required = 1

    if required ==0:
        print("No more places to visit!")
        return places

    while True:
        print("Enter the number of a place mark as visited")
        try:
            place_num = int(input(""))

            if place_num <0:
                print("Number must be >=0")
            elif place_num >= len(places):
                print("Invalid place number")
            elif places[place_num][3] == "n":
                places[place_num][3] = "v"
                print("You have visited {}".format(places[place_num][0]))
                break
            else:
                places[place_num][3] = "v"
                print("{} by {} visited".format(places[place_num][0],places[place_num][1]))
                break
        except:
            print("Invalid input; enter a valid number")
    return places

def save_places(places):
    print("{} places saved to CSV file".format(len(places)))
    write_file = open(place_file, 'w')
    for line in places:
        # out_file.write("{},{},{},{}\n".format(str(line[0]), str(line[1]), str(line[2])),str(line[3], File=out_file))
        new_file = '{}{}{}{}'.format(line[0], line[1], line[2], line[3]) + '\n'
        write_file.write(new_file)
    write_file.close()


main()
