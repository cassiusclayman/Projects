'''
    Mohammad Ali Bokhari
    Take-home assessment for Evive
'''

class Orders:
    # 1 is main, 2 is side, 3 is a drink, 4 is dessert
    breakfast = {}
    lunch = {}
    dinner = {}

    def __init__(self):
        """
        Constructor
        """
        self.breakfast = {1: "Eggs", 2: "Toast", 3: "Coffee"}
        self.lunch = {1: "Salad", 2: "Chips", 3: "Soda"}
        self.dinner = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}

    def count(self, lst):
        """
        find the number of occurrence of each item id in the order, return a dictionary with number of occurrences
        """
        counts = {1: 0, 2: 0, 3: 0, 4: 0}

        for itemID in lst:      # count occurrences of item id's
            itemID = eval(itemID)
            if itemID == 1:
                counts[1] += 1
            elif itemID == 2:
                counts[2] += 1
            elif itemID == 3:
                counts[3] += 1
            elif itemID == 4:
                counts[4] += 1
        return counts

    def validOrder(self, meal, counts):
        """
        Check whether an order is valid; return a message if the order is invalid
        """
        out = ""

        if counts[1] == 0:
            out += "Unable to process: Main is missing"
        if counts[2] == 0:
            if out == "":
                out += "Unable to process: Side is missing"
            else:
                out += ", side is missing"

        if meal == "Breakfast":
            if counts[1] > 1:
                out += "Unable to process: {} cannot be ordered more than once".format(self.breakfast[1])
            if counts[2] > 1:
                if out == "":
                    out += "Unable to process: {} cannot be ordered more than once".format(self.breakfast[2])
                else:
                    out += ", {} cannot be ordered more than once".format(self.breakfast[2])

        elif meal == "Lunch":
            if counts[1] > 1:
                out += "Unable to process: {} cannot be ordered more than once".format(self.lunch[1])
            if counts[3] > 1:
                if out == "":
                    out += "Unable to process: {} cannot be ordered more than once".format(self.lunch[3])
                else:
                    out += ", {} cannot be ordered more than once".format(self.lunch[3])

        elif meal == "Dinner":
            if counts[1] > 1:
                out += "Unable to process: {} cannot be ordered more than once".format(self.dinner[1])
            if counts[2] > 1:
                if out == "":
                    out += "Unable to process: {} cannot be ordered more than once".format(self.dinner[2])
                else:
                    out += ", {} cannot be ordered more than once".format(self.dinner[3])
            if counts[3] > 1:
                if out == "":
                    out += "Unable to process: {} cannot be ordered more than once".format(self.dinner[3])
                else:
                    out += ", {} cannot be ordered more than once".format(self.dinner[3])
            if counts[4] == 0:
                if out == "":
                    out += "Unable to process: Dessert is missing"
                else:
                    out += ", dessert is missing"
            if counts[4] > 1:
                if out == "":
                    out += "Unable to process: {} cannot be ordered more than once".format(self.dinner[4])
                else:
                    out += ", {} cannot be ordered more than once".format(self.dinner[4])

        return out

    def driver(self, line):
        """
        Builds output after counting occurrences of itemID's with count() and checking validity of the order using valid()
        """
        while True:
            line = line.replace(",", "")
            line = line.split()
            out = ""
            sortedLst = line[1:]
            sortedLst.sort()

            if line[0] == "":
                # no meal given
                return "Unable to process: Meal is missing"

            meal = line[0][0].upper() + line[0][1:]  # code to ensure first letter of meal is capitalized to match cases
            counts = self.count(sortedLst)

            if meal == "Breakfast":
                valid = self.validOrder("Breakfast", counts)  # check order validity
                if valid != "":
                    return valid

                for key in counts:
                    if key == 3:
                        if counts[key] == 0:
                            out += "Water"
                        if(counts[key]) > 0:
                            if counts[key] < 2:
                                out += "Coffee"
                            else:
                                out += "Coffee({})".format(counts[key])
                    else:
                        if counts[key] > 0:
                            out += self.breakfast[key] + ", "

            elif meal == "Lunch":

                valid = self.validOrder("Lunch", counts)
                if valid != "":
                    return valid

                for key in counts:

                    if key == 3:
                        if counts[key] > 0:
                            out += self.lunch[key]
                        else:
                            out += "Water"
                    elif key == 2:
                        if(counts[key]) > 0:
                            if counts[key] < 2:
                                out += "Chips, "
                            else:
                                out += "Chips({}), ".format(counts[key])
                    else:
                        if counts[key] > 0:
                            out += self.lunch[key] + ", "
            elif meal == "Dinner":
                valid = self.validOrder("Dinner", counts)
                if valid != "":
                    return valid

                for key in counts:
                    if key == 3:
                        if counts[key] > 0:
                            out += self.dinner[key] + ", Water, "
                        else:
                            out += "Water, "
                    elif key == 4:
                        out += self.dinner[key]
                    else:
                        if counts[key] > 0:
                            out += self.dinner[key] + ", "
            else:
                out = "Unable to process: Valid meal was not entered."
            return out

    def test(self):
        done = False
        print("\nIf you want to test using the provided file, please enter the string \"file\".\nIf you wish to provide"
              " your own text file, please enter the filename.\nLastly, if you wish to enter custom input, please enter"
              " the string \"custom\".")

        while not done:
            mode = input("Please enter the corresponding string: ")

            if mode == "file" or mode == "\"file\"":
                file = open("OrdersTest.txt", "r")
                lines = file.readlines()
                for line in lines:
                    if(line == ""):
                        pass
                    else:
                        print(self.driver(line))
                input("Exiting testing. Enter any key to end.")
                return

            elif mode == "custom" or mode == "\"custom\"":
                print("\nBeginning custom testing. Please enter the string \"quit\" when you want to end testing.")
                while not done:
                    try:
                        line = input("Please enter your meal and item IDs: ")
                        if line == "quit" or line == "\"quit\"":
                            print("Exiting testing.")
                            return
                        else:
                            print(self.driver(line))
                    except:
                        print("Sorry, that wasn't a valid string. Please try again.")
                input("Exiting testing. Enter any key to end.")
                return

            else:
                try:
                    file = open(mode, "r")
                    lines = file.readlines()
                    for line in lines:
                        print(self.driver(line))
                    input("Exiting testing. Enter any key to end.")
                    return
                except:
                    print("Sorry, that wasn't a valid file name. Please try again.")

def main():
    testObj = Orders()
    testObj.test()


if __name__ == "__main__":
    main()