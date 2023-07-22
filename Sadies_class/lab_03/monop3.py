def main():
    #create hotel and end_turn variable.
    hotel = 0
    end_turn = 0

    #loop through the prompts until we get a hotel.
    while hotel != 1 or end_turn == 0:
        
        #prompts user to see if they own all the proptery.
        property = str(input("Do you own all the green properties? (y/n)\n: "))

        #Checks response for output.
        if property == "n":
            print("You cannot purcahse a hotel until you own all the properties of a given color group.")
            end_turn = 1
            return end_turn
        
        #prompts user for what is on Pennsylvania.
        penn = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel)\n: "))

        #check response for PA output.
        if penn == 5:
            print("You cannot purcahse a hotel if the property already has one.")
            hotel = 1
            return hotel

        #prompts user for what is on North Carolina.
        carolina = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel)\n: "))

        #checks response for NC output.
        if carolina == 5:
            print("Swap North Carolina's hotel for Pennsylvania's 4 houses.")
            end_turn = 1
            return end_turn
            
        #prompts user for what is on Pacific.
        pacific = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel)\n: "))

        #checks response for PC output.
        if pacific == 5:
            print("Swap Pacific's hotel for Pennsylvania's 4 houses.")
            end_turn = 1
            return end_turn
        
        #prompts user for available hotels.
        buy_hotels = int(input("How many hotels are there to purchase?\n: "))

        #checks response for No Hotels output.
        if buy_hotels == 0:
            print("There are not enough hotels available for purchase at this time.")
            end_turn = 1
            return end_turn
        
        #Math for calculated houses need for each property.
        PA_need = 4 - penn
        NC_need = 4 - carolina
        PC_need = 4 - pacific

        #money needed per property.
        NC_money_need = NC_need * 200
        PC_money_need = PC_need * 200

        #Math for total houses needed for a hotel.
        total_need = PA_need + NC_need + PC_need

        #Math for money needed to build all the houses. The extra 200 at the end is for buying one hotel.
        total_money_need = (200 * total_need) + 200

        #prompts user for total cash available.
        cash = int(input("How much money do you have to spend?\n: "))

        #checks response for cash output.
        if cash < total_money_need:
            print("You do not have suffiecient funds to purchase a hotel at this time")
            end_turn = 1
            return end_turn

        #prompts user for available Houses.
        buy_houses = int(input("How many house are there to purchase?\n: "))

        #check response for cash houses output.
        if buy_houses < total_need:
            print("There are not enough houses available for purchase this time.")
            end_turn = 1
            return end_turn

        #Display the amount of houses need to build a hotel.
        print("The total amount of houses needed is",total_need,".")

        #Logic for purchasing houses and a hotel.
        if NC_need > 0:
            if PC_need > 0:
                print("This will cost $",total_money_need,".")
                print("\tPurchase 1 hotel and ",total_need," house(s).")
                print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
                print("\tPut ",NC_need," house(s) on North Carolina.")
                print("\tPut ",PC_need," house(s) on Pacific.")
                hotel = 1
                return hotel
            else:
                print("This will cost $",(NC_money_need + 200),".")
                print("\tPurchase 1 hotel and ",NC_need," house(s).")
                print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
                print("\tPut ",NC_need," house(s) on North Carolina.")
                hotel = 1
                return hotel
        else:
            if PC_need > 0:
                print("This will cost $",(PC_money_need + 200),".")
                print("\tPurchase 1 hotel and ",PC_need," house(s).")
                print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
                print("\tPut ",PC_need," house(s) on Pacific.")
                hotel = 1
                return hotel       


if __name__ == "__main__":
    main()
