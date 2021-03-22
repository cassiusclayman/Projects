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

        for id in lst:      # count occurrences of item id's
            id = eval(id)
            if(id == 1):
                counts[1] += 1
            elif(id == 2):
                counts[2] += 1
            elif(id == 3):
                counts[3] += 1
            elif(id == 4):
                counts[4] += 1
        return counts

    def validOrder(self, meal, counts):
        """
        Check whether an order is valid; return a message if the order is invalid
        """
        out = ""


        if(meal == "Breakfast"):
            if(counts[1] == 0):
                out += "Unable to process: Main is missing"
            if(counts[1] > 1):
                out += "Unable to process: {} cannot be ordered more than once".format(self.breakfast[1])
            if(counts[2] == 0):
                if(out == ""):
                    out += "Unable to process: Side is missing"
                else:
                    out += ", side is missing"
            if(counts[2] > 1):
                if(out == ""):
                    out += "Unable to process: {} cannot be ordered more than once".format(self.breakfast[2])
                else:
                    out += ", {} cannot be ordered more than once".format(self.breakfast[2])

        elif(meal == "Lunch"):
            if(counts[1] == 0):
                out += "Unable to process: Main is missing"
            if(counts[1] > 1):
                out += "Unable to process: {} cannot be ordered more than once".format(self.lunch[1])
            if(counts[2] == 0):
                if(out == ""):
                    out += "Unable to process: Side is missing"
                else:
                    out += ", side is missing"
            if(counts[3] > 1):
                if(out == ""):
                    out += "Unable to process: {} cannot be ordered more than once".format(self.lunch[3])
                else:
                    out += ", {} cannot be ordered more than once".format(self.lunch[3])

        # elif(meal == "Dinner"):
        return out
    
    def driver(self, line):

        while(True):
            line = line.replace(",", "")
            line = line.split()
            out = ""
            sortedLst = line[1:]
            sortedLst.sort()

            if line[0] == "":
                # no meal given
                return "Unable to process: Meal is missing"

            counts = self.count(sortedLst)
            if line[0] == "Breakfast":

                valid = self.validOrder("Breakfast", counts)  # check order validity
                if(valid != ""):
                    return valid

                for key in counts:
                    if(key == 3):
                        if(counts[key] == 0):
                            out += "Water"
                        if(counts[key]) > 0:
                            if(counts[key] < 2):
                                out += "Coffee"
                            else:
                                out += "Coffee({})".format(counts[key])
                    else:
                        if(counts[key] > 0):
                            out += self.breakfast[key] + ", "

            elif line[0] == "Lunch":

                valid = self.validOrder("Lunch", counts)
                if(valid != ""):
                    return valid

                for key in counts:

                    if(key == 3):
                        if counts[key] > 0:
                            out += self.lunch[key]
                        else:
                            out += "Water"
                    elif(key == 2):
                        if(counts[key]) > 0:
                            if(counts[key] < 2):
                                out += "Chips, "
                            else:
                                out += "Chips({}), ".format(counts[key])
                    else:
                        if(counts[key] > 0):
                            out += self.lunch[key] + ", "
            return out




            # elif line[0] == "Dinner":

def main():
    test = Orders()
    print(test.driver("Lunch 1, 2, 2"))


if __name__ == "__main__":
    main()