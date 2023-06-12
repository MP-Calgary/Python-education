# Prompt the color group.
print("")
color_group = input("Do you own all the green properties? (y/n) ")
if color_group == 'y':

    # If yes, ask what is on Pacific Avenue.
    pacific = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    if pacific == 0 or pacific == 1 or pacific == 2 or pacific == 3 or pacific == 4:

        # If there are no hotels on Pacific Avenue go to North Carolina.
        north_carolina = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if north_carolina == 0 or north_carolina == 1 or north_carolina == 2 or north_carolina == 3 or north_carolina == 4:

            # If there are no hotels on North Carolina, go to Pennsylvania.
            pennsylvania = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
            if pennsylvania == 0 or pennsylvania == 1 or pennsylvania == 2 or pennsylvania == 3 or pennsylvania == 4:

                # Ask how many hotels are avalible to purchase.
                num_hotels = int(input("How many hotels are there to purchase? "))
                if num_hotels > 0:

                    # Do all the calculations for amount of money needed.
                    num_house_PA_need = 4 - pacific
                    num_house_NC_need = 4 - north_carolina
                    num_house_PN_need = 4 - pennsylvania
                    num_house_total_need = num_house_PA_need + num_house_NC_need + num_house_PN_need
                    total_money_need = (num_house_total_need * 200) + 200
                    
                    # Prompt the amount of cash the player has.
                    total_cash = int(input("How much cash do you have to spend? "))
                    if total_cash > total_money_need:

                        # If player has enough money, prompt houses.
                        num_houses = int(input("How many houses are there to purchase? "))
                        if num_houses >= num_house_total_need:
                            
                            # Show the user how much money they owe, along with how many houses they need to purchase
                            # one hotel on Pennsylvania.
                            print("")
                            print(f"This will cost ${total_money_need}.")
                            print(f"    Purchase 1 hotel and {num_house_total_need} house(s).")
                            print(f"    Put 1 hotel on Pennsylvania and return any houses to the bank.")

                            # Determine if any houses need to be built on North Carolina or Pacific.
                            if num_house_NC_need > 0:
                                print(f"    Put {num_house_NC_need} house(s) on North Carolina.")

                                if num_house_PA_need > 0:
                                    print(f"    Put {num_house_PA_need} house(s) on Pacific.")

                                elif num_house_PA_need == 0:
                                    print("")

                            elif num_house_NC_need == 0:

                                if num_house_PA_need > 0:
                                    print(f"    Put {num_house_PA_need} house(s) on Pacific.")

                                elif num_house_PA_need == 0:
                                    print("")                                
                                

                        # If there are not enough houses, terminate the program.
                        elif num_houses < num_house_total_need:
                            print("\nThere are not enough houses available for purchase at this time.")

                    elif total_cash < total_money_need:
                        print("\nYou do not have sufficient funds to purchase a hotel at this time.")

                # If there are not enough hotels, terminate the program.
                elif num_hotels == 0:
                    print("\nThere are not enough hotels available for purchase at this time.")

            # If there is a hotel on Pennsylvania, terminate the program.
            elif pennsylvania == 5:
                print("\nYou cannot purchase a hotel if the property already has one.")

        # If there is a hotel on North Carolina, terminate the program.
        elif north_carolina == 5:
            print("\nSwap North Carolina's hotel with Pennsylvania's 4 houses.")

    # If there is a hotel on Pacific, terminate the program.
    elif pacific == 5:
        print("\nSwap Pacific's hotel with Pennsylvania's 4 houses.")

# If no, then terminate the program.
elif color_group == 'n':
    print("\nYou cannot purchase a hotel until you own all the properites of a given color group.")
