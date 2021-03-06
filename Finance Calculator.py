"""Program that acts as a finance calculator with various functions. Basically to save me time with my obsessive
calculations about my funds. """

import pandas as pd  # import pandas for pandas.eval for safe evaluation of user input


class PersonFinance:
    """
    Constructor for PersonFinance class
    """
    balances = {}
    payInf = {}
    bills = {}

    # TODO implement functions to find investment returns for investment
    #  accounts like a Roth IRA
    def __init__(self):
        self.balances = {"saving": 0.0, "savingInt": 0.0, "checking": 0.0, "total": 0.0}
        self.payInf = {"rate": 0.0, "hours": 0.0, "tax": 0.0, "grossPay": 0.0, "netPay": 0.0}
        self.bills = {"total": 0.0}
        self.four01k = {"start": 0.0, "contrib": 0.0, "compMatch": 0.0, "maxMatch": 0.0, "returnRate": 0.0,
                        "endTotal": 0.0}
        # self.saving = -1    # savings balance
        # self.checking = -1  # checking balance
        # self.rate = -1      # hourly rate
        # self.hours = -1     # average hours worked
        # self.tax = -1       # tax percentage deducted
        # self.pay = -1       # post-tax income
        # self.creditBill = -1   # credit card bill
        # self.genBill = -1  # general bills
        # self.rent = -1     # rent bill

    def __balanceCalc(self):
        """
        Private method used to calculate overall balances of the user
        """
        while True:
            try:
                self.balances["saving"] = float(
                    input("\nLet's calculate your overall balances!\nWe have to start with your"
                          " current savings amount. Please enter your savings (e.g. 20, 30, "
                          "4000): "))
                self.balances["checking"] = float(input("Please enter your checking amount: "))
                self.balances["total"] = self.balances["saving"] + self.balances["checking"]
                print("You've currently got ${:.2f} in your savings account and ${:.2f} in your checking account for a "
                      "total of ${:.2f}.".format(self.balances["saving"], self.balances["checking"],
                                                 self.balances["total"]))
                break
            except:
                print("Sorry, there was an error. "
                      "Please make sure you enter numerical amounts as digits (e.g. 1, 2, 300).")

    def __payCalc(self):
        """
        Private method used to calculate the user's pay
        """
        while True:
            try:
                print("\nLet's calculate your next paycheck!")
                self.payInf["rate"] = float(input("Please enter your hourly pay rate: "))
                self.payInf["hours"] = float(input("Please enter your expected hours worked over this pay period: "))
                inp = input(
                    "Please enter the percentage you usually get taxed on your income (e.g. 15, 25, etc.) : ")
                inp = inp.replace("%", "")  # If user enters the rate with a % symbol, replace it
                self.payInf["tax"] = float(inp) / 100  # presents tax in decimal form (e.g. 15% as .15)

                self.payInf["grossPay"] = self.payInf["rate"] * self.payInf["hours"]
                self.payInf["netPay"] = self.payInf["grossPay"] * (1 - self.payInf["tax"])
                print("\nYour gross pay is ${:.2f} and your net pay is ${:.2f}!\n".format(self.payInf["grossPay"],
                                                                                          self.payInf["netPay"]))
                break

            except:
                print(
                    "Sorry, there was an error. Please make sure you enter numerical amounts as digits (e.g. 1, 2, 300).")

    def __billCalc(self):
        """
        Private method used to calculate the user's bills
        """
        print("\nLet's calculate your bills!")
        print("If at any time you would like to subtract or add an amount from your total bills, please enter a + or -"
              " followed by the amount. (e.g. + 400, - 20, etc.)")
        while True:
            print("\nCurrent total bill amount is: ${:.2f}".format(self.bills["total"]))
            print("Please hit enter when you're done!")

            try:
                line = input("Enter the arithmetic operator along with the corresponding amount: ")
                if line == "":
                    input("All of your bills add up to ${:.2f}. Please enter any key to exit.".format(
                        self.bills["total"]))
                    input("\nPlease enter any key to exit.")
                    break
                elif ((line[0] == '+' and line[1] != " " and eval(line[1:]))
                      or (line[0] == '-' and line[1] != " " and eval(line[1:]))):
                    # if input is entered without a space but is valid (e.g. +500, -20)
                    line = [line[0], line[1:]]
                else:
                    line = line.split()
                if line[0] == "+":
                    self.bills["total"] += pd.eval(line[1])
                elif line[0] == "-":
                    self.bills["total"] -= pd.eval(line[1])
                else:
                    print("Incorrect Input: Please make sure you enter both an arithmetic operator and an amount.")

            except:
                print("Sorry, there was an error. Please make sure you only enter one arithmetic operator and one "
                      "numeric amount. (e.g. + 400, - 20, etc.)")

    def __saveInvestCalc(self):
        print("\nLet's calculate your savings account returns!")
        while True:
            if self.balances["saving"] == 0.0:
                self.balances["saving"] = float(input("Please enter your savings account balance (e.g. 10, 100, 1000, "
                                                      "etc.): "))
            print("Your current savings balance is ${:.2f}.".format(self.balances["saving"]))

            inp = input("Please enter the yearly interest rate on your savings accounts"
                        " (If you are unsure, the yearly rate is currently around 0.40~):")
            inp = inp.replace("%", "")  # If user enters the rate with a % symbol, replace it
            self.balances["savingInt"] = float(inp) / 100

            contrib = float(input("Saving accounts generally pay interest monthly, so any extra contributions to the "
                                  "account will also gain interest. Please enter your monthly contribution to the "
                                  "savings account: "))
            monthlyInt = self.balances["savingInt"] / 12  # calculate and store monthly interest rate
            endTotal = self.balances["saving"]
            for n in range(12):
                endTotal += contrib  # add monthly contribution to the account
                endTotal = endTotal + (endTotal * monthlyInt)  # add earned interest to the account
            print(
                "Starting with a balance of ${:.2f}, an interest rate of {}%, and a monthly "
                "contribution of ${:.2f},".format(self.balances["saving"], self.balances["savingInt"] * 100, contrib))

            totalNoInt = self.balances["saving"] + (contrib * 12)

            print("your savings total after only contributions will be: "
                  "${:.2f}, the interest you'll earn will be ${:.2f}".format(totalNoInt, (endTotal - totalNoInt)),
                  "and your total account balance after including interest earned will be ${:.2f}".format(endTotal))
            break

    def __investCalc(self):
        """
        Private method used to calculate returns on 401k and Roth IRA investments
        """

        print("Let's calculate your returns on your investment accounts! Currently, only 401k's and Roth IRA's are"
              " supported.")
        while True:
            mode = input("Please enter either 401k, Roth IRA, or hit enter to quit: ")
            if mode == "":
                print("Exiting.")
            if mode == "401k":
                '''
                401k's are pre-tax, so we will be using gross income
                '''

                if self.payInf["grossPay"] == 0:  # check if payInf has been populated already
                    self.__payCalc()

                self.four01k["start"] = float(input("Please enter your 401k's current balance: "))
                inp = input("Please enter your company's 401k match percentage: ")
                inp = inp.replace("%", "")  # remove any "%" symbols present
                self.four01k["compMatch"] = float(inp) / 100  # calculate the company match as a percentage
                inp = input(
                    "Please enter your 401k portfolio's average rate of return percentage (e.g. 5%, 6%, etc.): ")
                inp = inp.replace("%", "")
                self.four01k["returnRate"] = float(inp) / 100  # calculate the portfolio's return rate as a percentage
                yearGrossPay = self.payInf["grossPay"] * 26  # calculate year's gross income
                self.four01k["maxMatch"] = yearGrossPay * self.four01k["compMatch"]  # find max employer match
                inp = input("Please enter your contribution percentage: ")
                inp = inp.replace("%", "")
                self.four01k["contrib"] = float(inp) / 100  # calculate user's contribution percentage
                endTotal = self.four01k["start"]

                if self.four01k["compMatch"] > self.four01k["contrib"]:  # if user contributes less than company match
                    totalContrib = ((self.four01k[
                                         "contrib"] * yearGrossPay) / 26) * 2  # times 2 because the company matches our own contributions since they are less than their match cap
                    biweeklyReturn = self.four01k["returnRate"] / 26

                elif self.four01k["compMatch"] <= self.four01k["contrib"]:  # if user contributes as much as, or more than, the company match
                    compMatch = (self.four01k["compMatch"] * yearGrossPay) / 26  # how much the company will contribute over the year
                    ownContrib = (self.four01k["contrib"] * yearGrossPay) / 26
                    biweeklyReturn = self.four01k["returnRate"] / 26
                    totalContrib = compMatch + ownContrib

                for n in range(26):  # calculate 401k contributions and returns for the year
                    endTotal += totalContrib  # add contribution and company match to 401k
                    endTotal += endTotal * biweeklyReturn  # add projected portfolio return to 401k
                self.four01k["endTotal"] = endTotal
                if self.four01k["compMatch"] > self.four01k["contrib"]:
                    print("Starting 401k balance: ${:.2f}\nYearly gross salary: ${:.2f}\nCompany match: {:.2f}%\n"
                          "Company contribution: ${:.2f}\nPersonal percentage: {:.2f}%\nPersonal Contribution: ${:.2f}"
                          "\nPortfolio Return: {}%\nYear's End 401k balance: ${:.2f}\n"
                          "Investment return: ${:.2f}".format(self.four01k["start"], yearGrossPay,
                                                              self.four01k["contrib"] * 100,
                                                              self.four01k["contrib"] * yearGrossPay,
                                                              self.four01k["contrib"] * 100,
                                                              self.four01k["contrib"] * yearGrossPay,
                                                              self.four01k["returnRate"] * 100, self.four01k["endTotal"],
                                                              (self.four01k["endTotal"] -
                                                              (self.four01k["contrib"] * yearGrossPay) -
                                                              (self.four01k["compMatch"] * yearGrossPay))))
                else:
                    print("Starting 401k balance: ${:.2f}\nYearly gross salary: ${:.2f}\nCompany match: {:.2f}%\n"
                          "Company contribution: ${:.2f}\nPersonal percentage: {:.2f}%\nPersonal Contribution: ${:.2f}"
                          "\nPortfolio Return: {}%\nYear's End 401k balance: ${:.2f}\n"
                          "Investment return: ${:.2f}".format(self.four01k["start"], yearGrossPay,
                                                              self.four01k["compMatch"] * 100,
                                                              self.four01k["compMatch"] * yearGrossPay,
                                                              self.four01k["contrib"] * 100,
                                                              self.four01k["contrib"] * yearGrossPay,
                                                              self.four01k["returnRate"] * 100, self.four01k["endTotal"],
                                                              (self.four01k["endTotal"] -
                                                              (self.four01k["contrib"] * yearGrossPay) -
                                                              (self.four01k["compMatch"] * yearGrossPay))))
                break

    def driver(self):
        """
        Driver method
        """
        print("\nWelcome to Finance Calculator!")
        while True:
            print("Please enter the letter option for what you want to calculate today. \nYour options are: "
                  "A)Total Finances (Post Bills), B) Accounts and Total Pay, C) Pay After Taxes, D) Savings Returns, "
                  "E) Investment Returns, Z) Description of Options.\n"
                  "You may also simply hit the enter key to end the program! (Note: If you'd like to see a "
                  "description of the options available, please enter Z)")
            chk = input("\nEnter A, B, C, D, E, Z, or hit enter to quit:\n")

            if chk == "":
                print("Thank you for using Finance Calculator!")
                break

            # User did not exit the program so continue

            elif chk.upper() == 'A':
                '''
                Total Finances (Post Bills)
                '''

                self.__balanceCalc()
                input("Please hit enter to move on to the next step!")
                self.__billCalc()
                input("Please hit enter to move on to the next step!")
                self.__payCalc()
                input("Please hit enter to move on to the next step!")
                # print("\n Your current financial situation looks like this:\n",
                #       "Savings: ${:.2f}\n".format(self.balances["saving"]),
                #       "Checking: ${:.2f}\n".format(self.balances["checking"]),
                #       "Incoming pay: ${:.2f}\n".format(self.payInf["pay"]),
                #       "Pre-bill balances: ${:.2f}\n".format(self.balances["total"]),
                #       "Total bills: ${:.2f}\n".format(self.bills["total"]),
                #       "Post-bill balance: ${:.2f}\n".format(self.balances["total"] - self.bills["total"])
                #       )
                print("\nYour current financial situation looks like this:\n"
                      "Savings: ${:.2f}\nChecking: ${:.2f}\nGross pay: ${:.2f}\nNet pay: ${:.2f}\n"
                      "Pre-bill balances: ${:.2f}\nTotal bills: ${:.2f}"
                      "\nPost-bill balance: ${:.2f}\n".format(self.balances["saving"],
                                                              self.balances["checking"],
                                                              self.payInf["grossPay"],
                                                              self.payInf["netPay"],
                                                              self.balances["total"], self.bills["total"],
                                                              self.balances["total"] - self.bills["total"]))
                inp = input("\nIf you wish to use another function, please enter \"continue\". Otherwise, "
                            "please enter any key to exit: ")
                if inp == "continue":
                    self.driver()
                else:
                    break

            elif chk.upper() == 'B':
                '''
                Accounts and Total Pay
                '''
                self.__balanceCalc()
                self.__payCalc()
                print("You have a Savings balance of ${:.2f}, Checking balance of ${:.2f}, Overall "
                      "account balance (excluding pay) of ${:.2f},"
                      " and you will be getting paid ${:.2f}".format(self.balances["saving"], self.balances["checking"],
                                                                     self.balances["saving"] + self.balances["checking"]
                                                                     , self.payInf["pay"]))
                inp = input("\nIf you wish to use another function, please enter \"continue\". Otherwise, "
                            "please enter any key to exit: ")
                if inp == "continue":
                    self.driver()
                else:
                    break
                # Completed
            elif chk.upper() == 'C':
                '''
                Pay After Taxes
                '''

                self.__balanceCalc()
                self.__payCalc()
                print("Altogether, you'll have ${:.2f}.".format(self.balances["total"] + self.payInf["pay"]))
                inp = input("\nIf you wish to use another function, please enter \"continue\". Otherwise, "
                            "please enter any key to exit: ")
                if inp == "continue":
                    self.driver()
                else:
                    break
                # Completed

            elif chk.upper() == 'D':
                '''
                Savings Return
                '''
                self.__saveInvestCalc()
                inp = input("\nIf you wish to use another function, please enter \"continue\". Otherwise, "
                            "please enter any key to exit: ")
                if inp == "continue":
                    self.driver()
                else:
                    break

            elif chk.upper() == 'E':
                '''
                Investment Returns
                '''
                self.__investCalc()
                inp = input("\nIf you wish to use another function, please enter \"continue\". Otherwise, "
                            "please enter any key to exit: ")
                if inp == "continue":
                    self.driver()
                else:
                    break

            elif chk.upper() == 'Z':
                '''
                Description of Options
                '''

                print("\nOption A will take you through all the steps necessary to provide a complete picture of your "
                      "current financial situation.\nOption B will calculate your current account balances and "
                      "incoming pay.\nOption C will calculate your total pay after taxes.\n ")


def main():
    user = PersonFinance()
    user.driver()
    # user.billCalc()


if __name__ == "__main__":
    main()
