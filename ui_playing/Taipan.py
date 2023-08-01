#Based on the game Taipan, written by Art Canfil in 1978
import os
import math
import random
import platform
from datetime import datetime

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   REVERSE = '\033[7m'
   END = '\033[0m'

# -------[ END class color ]---------

class gameDate:
    monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self):
        self.DOM = 1
        self.MOY = 1
        self.YEAR = 1860
        self.orig_DOM = self.DOM
        self.orig_MOY = self.MOY
        self.orig_YEAR = self.YEAR

    def GetDate(self):
        return str(self.DOM).rjust(2, "0") + " " + self.monthName[(self.MOY - 1)] + " " + str(self.YEAR)

    def GetDay(self):
        return self.DOM

    def GetYear(self):
        return self.YEAR

    def GetMonth(self):
        return self.MOY

    def IncrementDate(self, Days2Add):
        self.DOM = self.DOM + Days2Add

        if self.MOY in [1, 3, 5, 7, 8, 10, 12]:
            if self.DOM > 31:
                self.DOM -= 31
                self.MOY += 1
        elif self.MOY in [4, 6, 9, 11]:
            if self.DOM > 30:
                self.DOM -= 30
                self.MOY += 1
        elif self.MOY == 2:
            if self.DOM > 28:
                self.DOM -= 28
                self.MOY += 1

        if self.MOY > 12:
            self.YEAR += 1
            self.MOY = 1

    def days_between_dates(self, curr_DOM, curr_MOY,curr_YEAR):
        original_day = self.orig_DOM
        original_month = self.orig_MOY
        original_year = self.orig_YEAR

        days = 0
        while (original_year, original_month, original_day) < (curr_YEAR, curr_MOY, curr_DOM):
            days_in_current_month = self.days_in_month(original_month, original_year)
            days_to_add = days_in_current_month - original_day + 1
            original_day = 1
            original_month += 1

            if original_month > 12:
                original_month = 1
                original_year += 1

            # Check if the next month exceeds the other_date
            if (original_year, original_month, original_day) > (curr_YEAR, curr_MOY, curr_DOM):
                days_to_add = curr_DOM - 1

            days += days_to_add

        return days

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and gameDate.is_leap_year(year):
            return 29
        return days_per_month[month]
    
# -------[ END class gameDate ]---------

class gameItems:
# lists = index 0 - 3
    itemName = ["Opium", "Silk", "Arms", "General"]
    itemPrice = [0, 0, 0, 0]

    def __init__(self):
        self.SetPrices(0)

    def SetPrices(self, port_number):
        price_range = {
            'Opium': (300, 999),
            'Silk': (50, 250),
            'Arms': (5, 150),
            'General': (1, 99)
            }
        min_price = 0
        max_price = 1
        small_step = 1
        large_step = 5
        # portNames = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
        port_variance = {
            'Opium':   [-10,  15,  10, -15,   5, -5,   0,  20],
            'Silk':    [-10,   5,  10,  15, -15,  0,  -5, -10],
            'Arms':    [-5,   15, -15, -10,   0,  5,  10, 0],
            'General': [-15, -10,  -5,   0,   5,  10, 15, 10]
        } # the above are percentages to change price based on the port

        opium_var = 1 + (port_variance['Opium'][port_number] / 100.0)
        silk_var = 1 + (port_variance['Silk'][port_number] / 100.0)
        arms_var = 1 + (port_variance['Arms'][port_number] / 100.0)
        general_var = 1 + (port_variance['General'][port_number] / 100.0)

        self.itemPrice = [
            max(int(round(random.randrange(price_range['Opium'][min_price], price_range['Opium'][max_price], large_step) * opium_var / 5.0)) * 5, 1),
            max(int(round(random.randrange(price_range['Silk'][min_price], price_range['Silk'][max_price], large_step) * silk_var / 5.0)) * 5, 1),
            max(int(round(random.randrange(price_range['Arms'][min_price], price_range['Arms'][max_price], small_step) * arms_var / 5.0)) * 5, 1),
            max(int(random.randrange(price_range['General'][min_price], price_range['General'][max_price], small_step) * general_var), 1)
        ] # rounding the bigger numbers to 5's, and the max ensures that the number will be at least 1

    def GetItemPrice(self,index):
        return(self.itemPrice[index])

    def GetItemName(self,index):
        return(self.itemName[index])

# -------[ END class gameItems ]---------

class gamePort:
    portNames = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
    portIndex = 0

    def __init__(self):
        self.portIndex = 0
        
    def SetPort(self, newIndex):
        if (self.portIndex != newIndex):
            self.portIndex = newIndex
    
    def GetPort(self):
        return(self.portIndex)

    def GetPortName(self):
        return(self.portNames[self.portIndex])
        
    def GetPortNameList(self):
        pNames = ""
        portList = []
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                portList.append(self.portNames[i])
        pNames = ",".join(portList)
        return(pNames)

    def GetPortCharList(self):
        pChars = ""
        portList = []
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                portList.append(self.portNames[i][0])
        pChars = ",".join(portList)
        return(pChars)

    def PrintPortList(self,currentport):
        formatted_string = ""
        numb_names = len(self.portNames)
        for i in range(len(self.portNames)):
            if i == currentport:
                formatted_string = formatted_string + " " * len(self.portNames[i]) + ", "
            else:
                formatted_string = formatted_string + self.portNames[i] + ", "
        formatted_string = formatted_string[:len(formatted_string)-2] # strip off last comma
        print("-------------------------------------------------------------------")
        print(formatted_string)
        print("-------------------------------------------------------------------")    


# -------[ END class gamePort ]---------

class playerGold:
    onHand = 0
    inBank = 0
    inDebt = 0

    def __init__(self, onHand):
        self.onHand = onHand
    
    def SpendGold(self,gold2spend):
        retVal = False
        if (gold2spend > self.onHand):
            print("You do not have that much gold.")
        else : 
            self.onHand = (self.onHand - gold2spend)
            retVal = True
        return(retVal)

    def AddGold(self,gold2add):
        self.onHand = (self.onHand + gold2add)

    def GetGoldOnHand(self):
        return (self.onHand)

    def GetGoldInBank(self):
        return (self.inBank)

    def GetGoldInDebt(self):
        return (self.inDebt)

    def DepositGold(self,gold2dep):
        retVal = False
        if (int(gold2dep) > int(self.onHand)):
            print("You do not have that much gold.")
        else : 
            self.onHand = (self.onHand - gold2dep)
            self.inBank = (self.inBank + gold2dep)
            retVal = True
        return(retVal)

    def WithdrawGold(self,gold2wd):
        retVal = False
        if (int(gold2wd) > int(self.inBank)):
            print("You do not have that much gold.")
        else : 
            self.onHand = (self.onHand + gold2wd)
            self.inBank = (self.inBank - gold2wd)
            retVal = True
        return(retVal)

    def BorrowGold(self,gold2borrow):
        retVal = False
        if ((self.inDebt + gold2borrow) > 1000):
            print("You cannot borrow that much! 1000 Max")
        else : 
            self.onHand = (self.onHand + gold2borrow)
            self.inDebt = (self.inDebt + gold2borrow)
            retVal = True
        return(retVal)

    def CompoundDebt(self):
        self.inDebt = (self.inDebt + (self.inDebt *.01))

    def RepayGold(self,gold2repay):
        retVal = False
        if (self.onHand < gold2repay):
            print("You do not have that much gold.")
        elif (round(self.inDebt) < gold2repay):
            print("Too much! Overpayment!")
        else : 
            self.inDebt = round(self.inDebt)
            self.onHand = (self.onHand - gold2repay)
            self.inDebt = (self.inDebt - gold2repay)
            retVal = True
        return(retVal)

# -------[ END class playerGold ]---------

class playerWarehouse:
    itemQty = [0, 0, 0, 0]

    def __init__(self):
        self.maxCapacity = 10000

    def GetCurrentCapacity(self):
        return (self.maxCapacity - self.itemQty[0] - self.itemQty[1] - self.itemQty[2] - self.itemQty[3])

    def GetMaxCapacity(self):
        return(self.maxCapacity)

    def GetItemQty(self, index):
        return(self.itemQty[index])

    def StoreItem(self, index, qty):
        retVal = False
        if (qty <= self.GetCurrentCapacity()) :
            self.itemQty[index] = (self.itemQty[index] + qty)
            retVal = True
        return (retVal)

    def RetrieveItem(self, index, qty):
        retVal = False
        if (qty <= self.itemQty[index]) :
            self.itemQty[index] = (self.itemQty[index] - qty)
            retVal = True
        return retVal

# -------[ END class playerWarehouse ]---------

class playerShip:
    itemQty = [0, 0, 0, 0]
    maxDefense = 500        # original number
    shipDefense = 500       # original number
    shipGuns = 5            # MP changed to 500 from default of 5 or 0 if there isn't a loan
    maxCapacity = 60      # MP changed to 5000 from default of 10 or if not guns, 60, Python version started at 50
    
    def __init__(self, name):
        self.name = name
    
    def GetName(self):
        return (self.name)
        
    def GetDefense(self):
        return (self.shipDefense)

    def GetGuns(self):
        return (self.shipGuns)

    def GetDamage(self):
        return (self.maxDefense-self.shipDefense)

    def GetStatus(self):
        return (round((self.shipDefense/self.maxDefense) * 100))

    def GetItemQty(self, index):
        return (self.itemQty[index])
        
    def GetTotalWeight(self):
        return(self.itemQty[0] + self.itemQty[1] + self.itemQty[2] + self.itemQty[3])

    def GetMaxCapacity(self):
        return(self.maxCapacity)
        
    def GetCapacity(self):
        return(round(self.maxCapacity * (self.shipDefense / self.maxDefense)))

    def GetCurrentCapacity(self):
        return(self.GetCapacity() - self.GetTotalWeight())
    
    def SetCapacity(self,newCap):
        self.maxCapacity = newCap

    def SetGuns(self,newGuns):
        self.shipGuns = newGuns
    
    def AddItem(self, index, amount2add):
        retVal = False
        if (amount2add > self.GetCurrentCapacity()) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] + amount2add)
            retVal = True
        return retVal
    
    def RemoveItem(self, index, amount2rem):
        retVal = False
        if (amount2rem > self.itemQty[index]) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] - amount2rem)
            retVal = True
        return retVal

    def DamageShip(self,Damage):
        self.shipDefense = (self.shipDefense - Damage)
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(3) > 0):
                self.RemoveItem(3,1);
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(2) > 0):
                self.RemoveItem(2,1);
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(1) > 0):
                self.RemoveItem(1,1);
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(0) > 0):
                self.RemoveItem(0,1);

    def RepairShip(self,Repair):
        self.shipDefense = (self.shipDefense + Repair)
        if (self.shipDefense > self.maxDefense):
            self.shipDefense = self.maxDefense

    def Attack(self):
        return(int(self.shipGuns * random.randrange(5, 50, 5)))
    
    def SetName(self, NewName):
        self.name = NewName
        
# -------[ END class playerShip ]---------
    
global Game_Items
global Game_Port
global Game_Date
global Player_Ship
global Player_Gold
global Player_WHouse

def Clear_Screen():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    
def Config_Game():
    global Game_Items
    global Game_Port
    global Game_Date
    global Player_Ship
    global Player_Gold
    global Player_WHouse

    companyName = ""
    Clear_Screen()
    print("")
    print("         _____  _    ___ ____   _    _   _               ")
    print("        |_   _|/ \\  |_ _|  _ \\ / \\  | \\ | |          ")
    print("          | | / _ \\  | || |_) / _ \\  |  \\| |          ")
    print("          | |/ ___ \\ | ||  __/ ___ \\ | |\\  |")
    print("          |_/_/   \\_\\___|_| /_/   \\_\\_| \\_|         ")
    print("                                                         Programmed by:")
    print("   A game based on the China trade of the 1800's         Michael Parker")
    print("")
    print("                      ~~|     ,                          ")
    print("                       ,|`-._/|")
    print("                     .' |   /||\\                        ")
    print("                   .'   | ./ ||`\\                       ")
    print("                  / `-. |/._ ||  \\                      ")
    print("                 /     `||  `|-._\\                      ")
    print("                 |      ||   ||   \\")
    print("~^~_-~^~=~^~~^= /       ||   ||__  \\~^=~^~-~^~_~^~=     ")
    print(" ~=~^~ _~^~ =~ `--------|`---||  `\"-`___~~^~ =_~^=      ")
    print("~ ~^~=~^_~^~ =~ \\~~~~~~~'~~~~'~~~~/~~`` ~=~^~ ~^=       ")
    print(" ~^=~^~_~-=~^~ ^ `--------------'~^~=~^~_~^=~^~=~")
    print("")
    
    Game_Items = gameItems()
    Game_Port = gamePort()
    Game_Date = gameDate()
    
    temp_name = 'test'
    Player_Ship = playerShip(temp_name)
    Player_Gold = playerGold(400)  # MP changed to 5000 from default of 400, if have no guns, or 0 if have guns
    Player_WHouse = playerWarehouse()

    print("Options:")
    print("0: Just quit")
    print("1: Load saved game")
    print("Any other key: Start new game")
    user_input = input("Enter your choice: ")

    if user_input == "0":
        exit()
    elif user_input == "1":
        Load_User_Data()
    else:
        #decide what the user wants to do
        companyName = input("What will you name your firm?: ")
        # Validate the input
        while companyName.strip() == "":
            print("Invalid input. The firm name cannot be empty.")
            companyName = input("What will you name your firm?: ")
        Player_Ship.SetName(companyName)

def Print_PirateShips(pirateQty):

    if (pirateQty < 1):
        return()

    line01 ="  _  _                  "
    line02 ="   \/      ]▓▓▓         "
    line03 ="       ____|_____       "
    line04 ="     /           /      "
    line05 ="     |           |      "
    line06 ="     \           \      "
    line07 ="      \___________\     "
    line08 ="  \ _______||__________ "
    line09 ="   \|_|_O_|_|_O_|_|_O_| "
    line10 ="^^%%\_,,_.,.  ,, ..,/   "
    line11 ="%^!^^^!!^^^%%%%%!!!!^^^%"


    pline01 = line01 
    pline02 = line02 
    pline03 = line03 
    pline04 = line04 
    pline05 = line05 
    pline06 = line06 
    pline07 = line07 
    pline08 = line08 
    pline09 = line09 
    pline10 = line10 
    pline11 = line11 


    if (pirateQty > 1):
        pline01 = pline01 + line01
        pline02 = pline02 + line02
        pline03 = pline03 + line03
        pline04 = pline04 + line04
        pline05 = pline05 + line05
        pline06 = pline06 + line06
        pline07 = pline07 + line07
        pline08 = pline08 + line08
        pline09 = pline09 + line09
        pline10 = pline10 + line10
        pline11 = pline11 + line11

    if (pirateQty > 2):
        pline01 = pline01 + line01
        pline02 = pline02 + line02
        pline03 = pline03 + line03
        pline04 = pline04 + line04
        pline05 = pline05 + line05
        pline06 = pline06 + line06
        pline07 = pline07 + line07
        pline08 = pline08 + line08
        pline09 = pline09 + line09
        pline10 = pline10 + line10
        pline11 = pline11 + line11
 
    print(pline01)
    print(pline02)
    print(pline03)
    print(pline04)
    print(pline05)
    print(pline06)
    print(pline07)
    print(color.YELLOW +pline08)
    print(color.YELLOW +pline09)
    print(color.BLUE +pline10)
    print(color.BLUE +pline11)

#  end Print_PirateShips


def Select_TradeItem():

    Selection = ""

    while (Selection != "O") and (Selection != "S") and (Selection != "A") and (Selection != "G") and (Selection != "Q"):
        print(f"Sellect item: " + color.GREEN + "O" + color.END + "pium ," + color.GREEN + "S" + color.END + "ilk, " + color.GREEN + "A" + color.END + "rms ,or " + color.GREEN + "G" + color.END + "eneral cargo?")
        Selection = input("[O,S,A,G,Q]")
        if (len(Selection) > 0) :
            Selection = Selection[0].upper()

    match Selection:
        case "O":
            RetVal = 0
        case "S":
            RetVal = 1
        case "A":
            RetVal = 2
        case "G":
            RetVal = 3
        case "Q":
            RetVal = 9

    return(RetVal)
        
#
# ┌──────────────────────────────────────────────────────────────────────┐
# │                 Company Name : The Peace Dividend                    │
# │  Hong Kong                                             99 jan 1860   │
# │ ┌────────────────────────────────────┐ ┌───────────────────────────┐ │
# │ │ Goods    Price   Ship   Warehouse  │ │ Gold On Hand : 1,000,000  │ │
# │ │ ================================== │ │ Gold in Bank : 0          │ │
# │ │ Opium    9999    99     10,000     │ │ Gold in Debt : 0          │ │
# │ │ Silk     999     0      0          │ ├───────────────────────────┤ │
# │ │ Arms     99      0      0          │ │ Ship Capacity : 50 / 50   │ │
# │ │ General  99      0      0          │ │ Ship Guns     : 5         │ │
# │ │                  ================= │ │ Ship Defense  : 500       │ │
# │ │       Available  99     99,999     │ │ Ship Status   : 100%      │ │
# │ └────────────────────────────────────┘ └───────────────────────────┘ │
# │                                                                      │
# └──────────────────────────────────────────────────────────────────────┘

def Print_GameStatus() :
    print("                                 TAIPAN")
    print(f"" + color.GREEN + " ┌────────────────────────────────────────────────────────────────────────┐")
    print(f"" + color.GREEN + " │" + ("Firm: " + color.END + Player_Ship.GetName()).center(76) + color.GREEN + "│")
    print(f"" + color.GREEN + " │ " + color.END + Game_Port.GetPortName().ljust(51),end="")
    print(f"" + color.GREEN + "  Date: " + color.END + Game_Date.GetDate(),end="")
    print(f"" + color.GREEN + " │")
    print(f"" + color.GREEN + " │ ┌────────────────────────────────────┐ ┌─────────────────────────────┐ │")
    print(f"" + color.GREEN + " │ │ Goods    Price   Ship   Warehouse  │ │ Gold On Hand : " + str("{:,}".format(Player_Gold.GetGoldOnHand())).ljust(13) + "│ │")
    print(f"" + color.GREEN + " │ │ ================================== │ │ Gold in Bank : " + str("{:,}".format(Player_Gold.GetGoldInBank())).ljust(13) + "│ │")
    print(f"" + color.GREEN + " │ │ " + str(Game_Items.GetItemName(0)).ljust(9) + str(Game_Items.GetItemPrice(0)).ljust(8) + str(Player_Ship.GetItemQty(0)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(0))).ljust(11) + "│ │ Gold in Debt : " + str("{:,}".format(round(Player_Gold.GetGoldInDebt()))).ljust(13) + "│ │")
    print(f"" + color.GREEN + " │ │ " + str(Game_Items.GetItemName(1)).ljust(9) + str(Game_Items.GetItemPrice(1)).ljust(8) + str(Player_Ship.GetItemQty(1)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(1))).ljust(11) + "│ ├─────────────────────────────┤ │")
    print(f"" + color.GREEN + " │ │ " + str(Game_Items.GetItemName(2)).ljust(9) + str(Game_Items.GetItemPrice(2)).ljust(8) + str(Player_Ship.GetItemQty(2)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(2))).ljust(11) + "│ │ Ship Capacity : " + (str(Player_Ship.GetCapacity()) + " / " + str(Player_Ship.GetMaxCapacity())).ljust(12) + "│ │")
    print(f"" + color.GREEN + " │ │ " + str(Game_Items.GetItemName(3)).ljust(9) + str(Game_Items.GetItemPrice(3)).ljust(8) + str(Player_Ship.GetItemQty(3)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(3))).ljust(11) + "│ │ Ship Guns     : " + str(Player_Ship.GetGuns()).ljust(12) + "│ │")
    print(f"" + color.GREEN + " │ │                  ================= │ │ Ship Defense  : "  + str(Player_Ship.GetDefense()).ljust(12) + "│ │")
    print(f"" + color.GREEN + " │ │       Available  " + str(Player_Ship.GetCurrentCapacity()).ljust(7) + str("{:,}".format(Player_WHouse.GetCurrentCapacity())).ljust(11) + "│ │ Ship Status   : " + str(Player_Ship.GetStatus()).ljust(5) + "%      │ │")
    print(f"" + color.GREEN + " │ └────────────────────────────────────┘ └─────────────────────────────┘ │")
    print(f"" + color.GREEN + " └────────────────────────────────────────────────────────────────────────┘")
    

def Ship_UnderAttack():
    underAttack = True
    playerNumberofGuns = Player_Ship.GetGuns()
    maxPirates = 15
    if playerNumberofGuns < 5:
        maxPirates = 10
    elif playerNumberofGuns == 5:
        maxPirates = 15
    else:
        maxPirates = 10 + (playerNumberofGuns // 10) * 2

    piratesInitial = random.randrange(1, maxPirates, 1)   # Set intitial number of attacking ships 
    piratesDefense = (piratesInitial * 100)       # Each ship takes 100 points of damage to sink it.
    piratesLeft = piratesInitial   # use piratesInitial to calculate the flotsam and jetsam.  more initial ships = greater reward

    while (underAttack):
        Clear_Screen()
        shipDamageTaken = int(random.randrange(1, ((piratesLeft if piratesLeft > 0 else 1)*2), 1))  # damage taken to Player_Ship -  calc on number of pirates left
        Player_Ship.DamageShip(shipDamageTaken)
        curr_status_of_ship = Player_Ship.GetStatus()
        if curr_status_of_ship < 0:
            print("Your ship sustained maximum damage and has sunk")
            print()
            print(color.BLUE)
            print("Y   Y   OOO     U   U")
            print(" Y Y   O   O    U   U")
            print("  Y    O   O    U   U")
            print("  Y    O   O    U   U")
            print("  Y     OOO      UUU")
            print()
            print("L       OOO      SSS    EEEE")
            print("L      O   O    S      E")
            print("L      O   O     SSS   EEEE")
            print("L      O   O        S  E")
            print("LLLLL   OOO     SSSS    EEEE")
            print(color.END)
            exit()
        
        Print_GameStatus()
        Print_PirateShips(piratesLeft)

        print(f"" + color.END + "We are under attack by " + color.YELLOW + str(piratesLeft), end=" ")
        print(f"" + color.END + "ships!")
#        print("Defense: "+str(piratesDefense))
#        print("Start Ships: "+str(piratesInitial))
#        print("Ships Left: "+str(piratesLeft))
        print(f"" + color.END + "We have sustained " + color.YELLOW  + str(shipDamageTaken), end=" ")
        print(f"" + color.END + "damage to our defenses.")

        RunFight = ""
        while (RunFight != "F") and (RunFight != "R"):
            print(f"" + color.END + "We're under attack.  Shall we " + color.GREEN + "F" + color.END + "ight or " + color.GREEN + "R" + color.END + "un?")
            RunFight = input("[F,R]")
            if (len(RunFight)> 0) :
                RunFight = RunFight[0].upper()

        if (RunFight == "F"):
            attackValue = Player_Ship.Attack()               # Ship Attack is based on Guns in ship
            piratesDefense = (piratesDefense - attackValue)
            piratesLeft = (piratesDefense // 100)
            if (piratesLeft <= 0):
                print(f"" + color.END + "Victory!  We have sunk all of the attacking ships!")
                # FlotsamQty = int(random.randrange(1, piratesInitial, 1))
                FlotsamQty = 1 if piratesInitial == 1 else int(random.randrange(1, piratesInitial, 1)) #MP added
                FlotsamItem = int(random.randrange(1, 4, 1))
                print("We have recovered some flotsam and jetsam.",FlotsamQty, "of",Game_Items.GetItemName(FlotsamItem))
                if (FlotsamQty > Player_Ship.GetCurrentCapacity()):
                    FlotsamQty = Player_Ship.GetCurrentCapacity()
                Player_Ship.AddItem(FlotsamItem,FlotsamQty)
                underAttack = False
            else :
                print(f"" + color.END + "We hit them with  ", attackValue, "damage.")
                print(f"" + color.END + "There are still ", piratesLeft, "ships attacking!")
        else :
            outRun = random.randrange(1, 4, 1)
            if (outRun >= piratesLeft):
                underAttack = False
                print(f"" + color.END + "We have escaped!")
            else :
                print("We have outrun", outRun, "ships!")
                piratesLeft = (piratesLeft - outRun)
        
        continueGame = input("Press <ENTER> to continue")
    

def Travel_toPort():
    Port_Desired = ""
    DaysAtSea = random.randrange(2, 7, 1)
    # print(Game_Port.GetPortNameList())
    Game_Port.PrintPortList(Game_Port.GetPort())
    
    
    while (Port_Desired != "H") and (Port_Desired != "B") and (Port_Desired != "C") and (Port_Desired != "J") and (Port_Desired != "M") and (Port_Desired != "P") and (Port_Desired != "R") and (Port_Desired != "S") and (Port_Desired != "Q") :
        Port_Desired = input(color.END + "Where would you like to go? ["+Game_Port.GetPortCharList()+",Q]")
        if (len(Port_Desired) > 0) :
            Port_Desired = Port_Desired[0].upper()

    match Port_Desired:
        case "H":
            newGamePort = 0
        case "B":
            newGamePort = 1
        case "C":
            newGamePort = 2
        case "J":
            newGamePort = 3
        case "M":
            newGamePort = 4
        case "P":
            newGamePort = 5
        case "R":
            newGamePort = 6
        case "S":
            newGamePort = 7
        case "Q":
            newGamePort = Game_Port.GetPort()
            
    if (newGamePort == Game_Port.GetPort()):
        print("We're already there!")
        Port_Desired = input("Press <ENTER> to continue")
    else :
        Game_Date.IncrementDate(DaysAtSea)
        Game_Items.SetPrices(newGamePort)
        Game_Port.SetPort(newGamePort)
        Disaster = random.randrange(1, 10, 1)
        if (Disaster > 6):
            Ship_UnderAttack()
        elif (Disaster < 2):
            Game_Port.SetPort(random.randrange(1, 8, 1))
            print("Storm! We've been blown off course")
            Port_Desired = input("Press <ENTER> to continue")

        

def Buy_Cargo():
    bIndex = Select_TradeItem()
    Can_Buy = (Player_Gold.GetGoldOnHand() // Game_Items.GetItemPrice(bIndex))
    print(f"Buy {Game_Items.GetItemName(bIndex)}!")
    print(f"You can afford {Can_Buy} {Game_Items.GetItemName(bIndex)}.")
    try:
        Want_Buy = int(input("How much do you want to buy?"))
    except ValueError:
        Want_Buy = 0 
    if (Want_Buy > 0) and (Want_Buy <= Can_Buy) :
        if (Player_Ship.AddItem(bIndex, Want_Buy) == False):
            print("Unable to complete the transaction.  Check capacity!")
            Want_Buy = input("Press <ENTER> to continue")
        else :
            Player_Gold.SpendGold(Want_Buy * Game_Items.GetItemPrice(bIndex))
    else:
        print("Invalid Amount Selected")
        Want_Buy = input("Press <ENTER> to continue")
   

def Sell_Cargo():
    sIndex = Select_TradeItem()
    Can_Sell = Player_Ship.GetItemQty(sIndex)
    print(f"Sell {Game_Items.GetItemName(sIndex)}!")
    print(f"You have {Player_Ship.GetItemQty(sIndex)} of {Game_Items.GetItemName(sIndex)} to sell.")
    try:
        Want_Sell = int(input("How much do you want to sell?"))
    except ValueError:
        Want_Sell = 0
   
    if (Want_Sell > 0) and (Want_Sell <= Can_Sell) :
        if (Player_Ship.RemoveItem(sIndex, Want_Sell) == False):
            print("Unable to complete the transaction.  Check capacity!")
            Want_Sell = input("Press <ENTER> to continue")
        else:
            Player_Gold.AddGold(Want_Sell * Game_Items.GetItemPrice(sIndex))
    else:
        print("Invalid Amount Selected")
        Want_Sell = input("Press <ENTER> to continue")


def Visit_Bank():
    Bank_Amount = 0
    Bank_Action = ""

    while (Bank_Action != "D") and (Bank_Action != "W") and (Bank_Action != "B") and (Bank_Action != "R") and (Bank_Action != "Q") :
        print(f"" + color.END + "Would you like to " + color.GREEN + "D" + color.END + "eposit, " + color.GREEN + "W" + color.END + "ithdraw, " + color.GREEN + "B" + color.END + "orrow or " + color.GREEN + "R" + color.END + "epay?")
        Bank_Action = input("[D,W,B,R,Q]")
        if (len(Bank_Action) > 0) :
            Bank_Action = Bank_Action[0].upper()

    match Bank_Action:
        case "D":
            try:
                Bank_Amount = int(input("How much would you like to deposit?"))
            except ValueError:
                Bank_Amount = 0
            if (Player_Gold.DepositGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "W":
            try:
                Bank_Amount = int(input("How much would you like to withdraw?"))
            except ValueError:
                Bank_Amount = 0
            if (Player_Gold.WithdrawGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "B":
            try:
                Bank_Amount = int(input("How much would you like to borrow?"))
            except ValueError:
                Bank_Amount = 0       
            if (Player_Gold.BorrowGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  1000 Max!")
                Bank_Action = input("Press <ENTER> to continue")

        case "R":
            try:
                Bank_Amount = int(input("How much would you like to repay?"))
            except ValueError:
                Bank_Amount = 0  
            if (Player_Gold.RepayGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")


def Store_Cargo():
    sIndex = Select_TradeItem()
    onShip = int(Player_Ship.GetItemQty(sIndex))
    WarehouseSpace = Player_WHouse.GetCurrentCapacity()
    
    if (onShip > WarehouseSpace):
        Can_Store = WarehouseSpace
    else:
        Can_Store = onShip

    print(f"Store {Game_Items.GetItemName(sIndex)}!")
    print("You can store", Can_Store, Game_Items.GetItemName(sIndex),".")

    try:
         qty2Store = int(input("How much do you want to store?"))
    except ValueError:
        qty2Store = 0
    
    while (qty2Store < 0) and (qty2Store > Can_Store):
            try:
                qty2Store = int(input("How much do you want to store?"))
            except ValueError:
                qty2Store = 0

    if (Player_Ship.RemoveItem(sIndex,qty2Store) == False):
        print("Unable to complete the transaction.  Check Ship cargo availability!")
    else:
        if (Player_WHouse.StoreItem(sIndex,qty2Store) == False):
            print("Unable to complete the transaction.  Check Warehouse capacity!")
        else:
            print("Stored", qty2Store,Game_Items.GetItemName(sIndex))

    continueGame = input("Press <ENTER> to continue")


def Retrieve_Cargo():
    rIndex = Select_TradeItem()
    inWhouse = Player_WHouse.GetItemQty(rIndex)
    ShipSpace = Player_Ship.GetCurrentCapacity()
    
    if (inWhouse > ShipSpace):
        Can_Retrieve = ShipSpace
    else: 
        Can_Retrieve = inWhouse

    print(f"Retrieve {Game_Items.GetItemName(rIndex)}!")
    print("You can retrieve", Can_Retrieve, Game_Items.GetItemName(rIndex),".")

    try:
        qty2Retrieve = int(input("How much do you want to retrieve?"))
    except ValueError:
        qty2Retrieve = 0

    while (qty2Retrieve < 0) and (qty2Retrieve > Can_Retrieve):
        print("You can retrieve", Can_Retrieve, Game_Items.GetItemName(rIndex),".")
        try:
            qty2Retrieve = int(input("How much do you want to retrieve?"))
        except ValueError:
            qty2Retrieve = 0

    print(f"Retrieve {Game_Items.GetItemName(rIndex)}!")

    if (Player_WHouse.RetrieveItem(rIndex,qty2Retrieve) == False):
        print("Unable to complete the transaction.  Check Warehouse capacity!")
    else:
        if (Player_Ship.AddItem(rIndex,qty2Retrieve) == False):
            print("Unable to complete the transaction.  Check Ship cargo availability!")
            print("Returning cargo")
            Player_WHouse.StoreItem(rIndex,qty2Retrieve)
        else:
            print("Retrieved", qty2Retrieve,Game_Items.GetItemName(rIndex))

    continueGame = input("Press <ENTER> to continue")


def Use_Warehouse():
    xfer_Amount = 0
    xfer_Item = 0
    Whse_Action = ""

    while (Whse_Action != "S") and (Whse_Action != "R") and (Whse_Action != "Q"):
        print(f"" + color.END + "Would you like to " + color.GREEN + "S" + color.END + "tore or " + color.GREEN + "R" + color.END + "etrieve items from the warehouse?")
        Whse_Action = input("[S,R,Q]")
        if (len(Whse_Action) > 0) :
            Whse_Action = Whse_Action[0].upper()

    match Whse_Action:
        case "S":
            Store_Cargo()
        case "R":
            Retrieve_Cargo()


def Repair_Ship():
    damAmount = Player_Ship.GetDamage()
    repCost = (damAmount * 10)

    print("Repairing a ship costs 10 gold per damage point.")
    print("Your ship has "+str(damAmount)+" damage points.")
    print("It will cost "+str(repCost)+" to fully repair your ship.")

    try:
        Want_Repair = int(input("How much DAMAGE do you want to repair?"))
    except ValueError:
        Want_Repair = 0


    if ((Want_Repair * 10) > Player_Gold.GetGoldOnHand()):
        print("Unable to complete the transaction.  Insufficient Funds!")
        Want_Repair = input("Press <ENTER> to continue")
    else :
        if (Want_Repair > Player_Ship.GetDamage()):
            print("Unable to complete the transaction.  Check damage!")
            Want_Repair = input("Press <ENTER> to continue")
        else :
            Player_Gold.SpendGold(Want_Repair * 10)
            Player_Ship.RepairShip(Want_Repair)
   
def New_Ship():
    choice = 0  # set default value prior to prompt
    time = ((Game_Date.GetYear() - 1860) * 12) + Game_Date.GetMonth()
    amount = random.randint(0, (1000 * (time + 5) // 6)) * (Player_Ship.GetMaxCapacity() // 50) + 1000
    amount = 50 # debug

    if Player_Gold.GetGoldOnHand() < amount:
        return

    fancy_num =  "${:,.0f}".format(amount) 

    print(color.END) 
    print("Comprador's Report")
    print()
    print("Do you wish to trade in your ", end='')
    if Player_Ship.GetDamage() > 0:
        print(color.REVERSE, end='')   # Setting text background color to reverse (highlight)
        print("damaged", end='')
        print(color.END, end='')  # Resetting text formatting to normal
    else:
        print(color.BOLD, end='')
        print("fine", end='')
        print(color.END, end='')
   
    print(" ship for one with 50 more capacity by")
    print(f"paying an additional {fancy_num}, Taipan? Y/N")

    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input().strip().upper()

    if choice in ['Y', 'y']:
        if Player_Gold.SpendGold(amount):
            Player_Ship.SetCapacity(Player_Ship.GetMaxCapacity() + 50)  # add 50 to current state of ship
            Player_Ship.RepairShip(Player_Ship.GetMaxCapacity() + 50) # if bigger than max, will be set to max
    return

def New_Gun():
    choice = 0
    time = ((Game_Date.GetYear() - 1860) * 12) + Game_Date.GetMonth()
    amount = random.randint(500, 1000 * (time + 5) // 6)

    if (Player_Gold.GetGoldOnHand() < amount) or (Player_Ship.GetCapacity() < 10):
        return

    f_amount = "${:,.0f}".format(amount)

    print("Comprador's Report\n\n")
    print(f"Do you wish to buy a ship's gun for {f_amount}, Taipan? ")

    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input().upper()

    if choice in ['Y', 'y']:
        if Player_Gold.SpendGold(amount):
            Player_Ship.SetCapacity(Player_Ship.GetMaxCapacity() + 10)  # add 50 to current state of ship
            Player_Ship.SetGuns(Player_Ship.GetGuns() + 1) 
    return

def Play():

    Clear_Screen()
    Print_GameStatus() 

    print("\n")
    User_Action = ""
    if (Game_Port.GetPort() == 0):  # Hong Kong has more services
        # New_Ship() # MP debug could prompt every time go to Hong Kong
        # New_Gun()  # MP debug could prompt every time go to Hong Kong
        
        # Each time go to Hong Kong, random chance can upgrade ship, or buy a new gun
        if random.randint(0, 3) == 0:
            if random.randint(0, 1) == 0:
                New_Ship() 
            elif Player_Ship.GetGuns() < 1000:
                New_Gun()
            # redraw screen as some stats may have been updated
            Clear_Screen()
            Print_GameStatus() 

        while (User_Action != "B") and (User_Action != "S") and (User_Action != "V") and (User_Action != "W") and (User_Action != "R") and (User_Action != "T") and (User_Action != "Q") and (User_Action != "A"):
            print(f"" + color.END + "Would you like to " + color.GREEN + "B" + color.END + "uy, " + color.GREEN + "S" + color.END + "ell, " + color.GREEN + "V" + color.END + "isit the Bank, use the " + color.GREEN + "W" + color.END + "arehouse, " + color.GREEN + "R" + color.END + "epair your ship, " + color.GREEN + "T" + color.END + "ravel to a new port?, or " + color.GREEN + "Q" + color.END + "uit ")
            User_Action = input("[B,S,V,W,R,T,Q]")
            if (len(User_Action) > 0) :
                User_Action = User_Action[0].upper()
    
        match User_Action:
            case "B":
                Buy_Cargo()
            case "S":
                Sell_Cargo()
            case "V":
                Visit_Bank()
            case "W":
                Use_Warehouse()
            case "R":
                Repair_Ship()
            case "T":
                Travel_toPort()
                Player_Gold.CompoundDebt() # add debt every time you travel
            case "Q":
                my_inhand_money = Player_Gold.GetGoldOnHand()
                f_inhand_money = "${:,.0f}".format(my_inhand_money)
                my_bank_money = Player_Gold.GetGoldInBank()
                f_bank_money = "${:,.0f}".format(my_bank_money)
                total_money = my_inhand_money + my_bank_money
                numb_days_played = Game_Date.days_between_dates(Game_Date.GetDay(),Game_Date.GetMonth(),Game_Date.GetYear())

                if total_money > 999999:
                # if total_money > 100:
                    print()
                    print("|=======================================================|")
                    print("|                   Y o u ' r e    a                    |")
                    print("|                                                       |")
                    print("|" + color.GREEN  + "                M I L L I O N A I R E ! " + color.END + "               |")
                    print("|=======================================================|")
                    print()
                    print("You finished the game with")
                    print()
                    print(f"Gold on hand: {f_inhand_money} and Gold in bank: {f_bank_money}")
                    print()
                    print(f"You played for {numb_days_played:,} days")
                    print()
                else:
                    print("")
                    print("|---------------------------------------------------|")
                    print("|" + color.RED  + "               G A M E       O V E R" +  color.END + "               |")
                    print("|                                                   |")
                    print("| You did not reach the goal of being a millionaire |")
                    print("|---------------------------------------------------|")
                    print("                         ")
                    print("You finished the game with")
                    print()
                    print(f"Gold on hand: {f_inhand_money} and Gold in bank: {f_bank_money}")
                    print()
                    print(f"You played for {numb_days_played:,} days")
                    print()
                exit()
            case "A":
                Save_User_Data()
            case _:
                User_Action = input("Press <ENTER> to continue")
    
    else:
        while (User_Action != "B") and (User_Action != "S") and (User_Action != "T"):
            print(f"" + color.END + "Would you like to " + color.GREEN + "B" + color.END + "uy, " + color.GREEN + "S" + color.END + "ell, or " + color.GREEN + "T" + color.END + "ravel to a new port?")
            User_Action = input("[B,S,T]")
            if (len(User_Action) > 0) :
                User_Action = User_Action[0].upper()
  
        match User_Action:
            case "B":
                Buy_Cargo()
            case "S":
                Sell_Cargo()
            case "T":
                Travel_toPort()
                Player_Gold.CompoundDebt() # add debt every time you travel
    
# End Play()

def Load_User_Data():
    while True:
        filename = input("Enter the filename with the saved data: (enter 0 to abort): ")
        if filename == "0":
            return

        # Open the file for reading
        try:
            with open(filename, "r") as file:
                # Read each line and set the corresponding variable
                general_comment = file.readline().strip()
                save_date = file.readline().strip()
                firm_name = file.readline().strip()
                Player_Ship.SetName(firm_name)

                Game_Date.DOM = int(file.readline().strip())
                Game_Date.MOY = int(file.readline().strip())
                Game_Date.YEAR = int(file.readline().strip())

                Player_Gold.onHand = int(file.readline().strip())
                Player_Gold.inBank = int(file.readline().strip())
                Player_Gold.inDebt = int(file.readline().strip())

                warehouse_string = file.readline().strip()
                Player_Ship.maxDefense = int(file.readline().strip())
                Player_Ship.shipDefense = int(file.readline().strip())
                Player_Ship.shipGuns = int(file.readline().strip())
                Player_Ship.maxCapacity = int(file.readline().strip())
                ship_string = file.readline().strip()

            break  # Exit the loop if the file is successfully read

        except FileNotFoundError:
            print("File not found. Please make sure you entered the correct filename.")

    #need to convert string for Warehouse into the list
    items = warehouse_string[1:-1].split(',')    # Remove the brackets and split the string by commas

    Player_WHouse.itemQty = [int(item.strip()) for item in items]   # Convert each element to an integer and create a list

    #need to convert string for Ship into the list
    items = ship_string[1:-1].split(',')    # Remove the brackets and split the string by commas

    Player_Ship.itemQty = [int(item.strip()) for item in items] # Convert each element to an integer and create a list

    # Game_Date.DOM = 26
    # Game_Date.MOY = 6
    # Game_Date.YEAR = 1862   

    # Player_Gold.onHand = 543210
    # Player_Gold.inBank = 22345
    # Player_Gold.inDebt = 654

    # Player_WHouse.itemQty = [67,125,678,1450]

    # Player_Ship.maxDefense = 5123
    # Player_Ship.shipDefense = 4932
    # Player_Ship.shipGuns = 520
    # Player_Ship.maxCapacity = 6000
    # Player_Ship.itemQty = [2,6,11,18]

    print(f"Data loaded from file '{filename}' succesfully. Data was saved on: {save_date}")
    User_Action = input("Press <ENTER> to continue")

# End Load_Values()    

def Is_Valid_File_Name(file_name):
   if file_name.strip() == '':
      return False
   try:
      # Attempt to create a file with the given name (won't actually create it)
      with open(file_name, 'w'):
         pass
      # If successful, the file name is valid
      return True
   except:
      # If an error occurs, the file name is invalid
      return False
   
# End Is_Valid_File_Name()    

def Get_Valid_File_Name(prompt):
    while True:
        file_name = input(prompt)
        if file_name == "0":
            return file_name
        elif Is_Valid_File_Name(file_name):
            return file_name
        print("Invalid file name. Please try again.")

# End Get_Valid_File_Name()  

def Save_User_Data():
    prompt = "Enter a file name: (enter 0 to abort):"
    file_name = Get_Valid_File_Name(prompt)
    if file_name == "0":
        return

    # Get the current date and time
    now = datetime.now()

    # Format the date and time in the desired format
    formatted_date_time = now.strftime("%d-%m-%Y %I:%M:%S %p")

    datafile = open(file_name, 'w')

    datafile.write(f"This is a data file for the Game Taipan.  Please do not edit.\n")
    datafile.write(f"{formatted_date_time} \n")

    datafile.write(f"{Player_Ship.GetName()} \n")

    datafile.write(str(Game_Date.DOM) + "\n")
    datafile.write(str(Game_Date.MOY) + "\n")
    datafile.write(str(Game_Date.YEAR) + "\n")

    datafile.write(str(Player_Gold.onHand ) + "\n")
    datafile.write(str(Player_Gold.inBank ) + "\n")
    datafile.write(str(Player_Gold.inDebt ) + "\n")


    datafile.write(str(Player_WHouse.itemQty ) + "\n") 

    datafile.write(str(Player_Ship.maxDefense ) + "\n")
    datafile.write(str(Player_Ship.shipDefense ) + "\n")
    datafile.write(str(Player_Ship.shipGuns ) + "\n")
    datafile.write(str(Player_Ship.maxCapacity ) + "\n")
    datafile.write(str(Player_Ship.itemQty ) + "\n") 

    datafile.close() 

    print(f"Successfully saved Taipan user data to '{file_name}'")
    User_Action = input("Press <ENTER> to continue")

# End Save_User_Data()  

def main():
  
    Config_Game()
   
    while (Player_Gold.GetGoldOnHand() < 10000000):
        Play()

if __name__ == "__main__":
    main()