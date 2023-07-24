import os
import math
import random

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
   END = '\033[0m'

class gameDate:
    monthName = ["Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec"]

    def __init__(self):
        self.DOM = 1
        self.MOY = 1
        self.YEAR = 1850

    def GetDate(self):
        return(str(self.DOM).rjust(2,"0") + " " + self.monthName[(self.MOY - 1)] + " " + str(self.YEAR))

    def GetMonth(self):
        return(self.MOY)

    def IncrementDate(self, Days2Add):
        self.DOM = self.DOM + Days2Add

        if (self.MOY == 1) or (self.MOY == 3) or (self.MOY == 5) or (self.MOY == 7) or (self.MOY == 8) or (self.MOY == 10) or (self.MOY == 12):
            if (self.DOM > 31):
                self.DOM -= 31
                self.MOY += 1
        if (self.MOY == 4) or (self.MOY == 6) or (self.MOY == 9) or (self.MOY == 11):
            if (self.DOM > 30):
                self.DOM -= 30
                self.MOY += 1
        if (self.MOY == 2):
            if (self.DOM > 28):
                self.DOM -= 28
                self.MOY += 1
        if (self.MOY > 12) :
            self.YEAR += 1
            self.MOY = 1
    
# -------[ END class gameDate ]---------

class gameItems:
# lists = index 0 - 3
    itemName = ["Opium", "Silk", "Arms", "General"]
    itemPrice = [0, 0, 0, 0]

    def __init__(self):
        self.SetPrices()

    def SetPrices(self):
        self.itemPrice = [random.randrange(300, 999, 5), random.randrange(50, 250, 1), random.randrange(5, 150, 5), random.randrange(1, 99, 1)]

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
    maxDefense = 500        # MP increased
    shipDefense = 500       # MP increased
    shipGuns = 500          # MP increased
    maxCapacity = 5000      # MP increased
    
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
        
# -------[ END class playerShip ]---------
    
global Game_Items
global Game_Port
global Game_Date
global Player_Ship
global Player_Gold
global Player_WHouse


def Clear_Screen():
    os.system('clear')

    
def Config_Game():
    global Game_Items
    global Game_Port
    global Game_Date
    global Player_Ship
    global Player_Gold
    global Player_WHouse

    companyName = ""
    Clear_Screen()
    print("Welcome to the East Empire Trading Simulation!\n")
    companyName = input("What shall we use for a company name?\n")
    
    Game_Items = gameItems()
    Game_Port = gamePort()
    Game_Date = gameDate()
    
    Player_Ship = playerShip(companyName)
    Player_Gold = playerGold(5000)  # MP bumped up
    Player_WHouse = playerWarehouse()


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
    piratesInitial = random.randrange(1, 15, 1)   # Set intitial number of attacking ships 
    piratesDefense = (piratesInitial * 100)       # Each ship takes 100 points of damage to sink it.
    piratesLeft = piratesInitial   # use piratesInitial to calculate the flotsam and jetsam.  more initial ships = greater reward

    while (underAttack):
        Clear_Screen()
        shipDamageTaken = int(random.randrange(1, ((piratesLeft if piratesLeft > 0 else 1)*2), 1))  # damage taken to Player_Ship -  calc on number of pirates left
        Player_Ship.DamageShip(shipDamageTaken)
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
    global Game_Date

    Port_Desired = ""
    DaysAtSea = random.randrange(2, 7, 1)
    print(Game_Port.GetPortNameList())
    
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
        Game_Items.SetPrices()
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
    Want_Buy = int(input("How much do you want to buy?"))
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
    Want_Sell = int(input("How much do you want to sell?"))

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
            Bank_Amount = int(input("How much would you like to deposit?"))
            if (Player_Gold.DepositGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "W":
            Bank_Amount = int(input("How much would you like to withdraw?"))
            if (Player_Gold.WithdrawGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "B":
            Bank_Amount = int(input("How much would you like to borrow?"))
            if (Player_Gold.BorrowGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  1000 Max!")
                Bank_Action = input("Press <ENTER> to continue")

        case "R":
            Bank_Amount = int(input("How much would you like to repay?"))
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

    qty2Store = int(input("How much do you want to store?"))
    while (qty2Store < 0) and (qty2Store > Can_Store):
        qty2Store = int(input("How much do you want to store?"))

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

    qty2Retrieve = int(input("How much do you want to retrieve?"))
    while (qty2Retrieve < 0) and (qty2Retrieve > Can_Retrieve):
        print("You can retrieve", Can_Retrieve, Game_Items.GetItemName(rIndex),".")
        qty2Retrieve = int(input("How much do you want to retrieve?"))

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
    Want_Repair = int(input("How much DAMAGE do you want to repair?"))

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
   

def Play():

    Clear_Screen()
    Print_GameStatus() 

    print("\n")
    User_Action = ""
    if (Game_Port.GetPort() == 0):  # Hong Kong has more services
    
        while (User_Action != "B") and (User_Action != "S") and (User_Action != "V") and (User_Action != "W") and (User_Action != "R") and (User_Action != "T") and (User_Action != "Q"):
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
                my_bank_money = Player_Gold.GetGoldInBank()
                total_money = my_inhand_money + my_bank_money
                if total_money > 1000000:
                    print("")
                    print("YOU ARE A MILLIONARE!!!")
                    print("")
                    print("In hand money", my_inhand_money, ", In bank money",my_bank_money)
                    print("")
                else:
                    print("")
                    print("You finished the game with:")
                    print("In hand money", my_inhand_money, ", In bank money",my_bank_money)
                exit()
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



def main():
  
    Config_Game()
    
    while (Player_Gold.GetGoldOnHand() < 10000000):
        Play()

if __name__ == "__main__":
    main()