def gold_silver_calculator() -> float:
    """Calculate the value of gold and silver in pennyweight (dwt), gram (g), 
    or troy ounce (ozt)"""
    metal = input("Select Gold or Silver: ")
    while metal != 'Gold' and metal != 'Silver':
            print("Must be Gold or Silver")
            metal = input("Select Gold or Silver: ")
    if metal == 'Gold':
        while True:
            gold_price_troy_ounce = input("Enter Gold Price: ")
            try:
                gold_price_troy_ounce = float(gold_price_troy_ounce)
                break
            except:
                print("Must be a number")
        unit = input("Select dwt, g, or ozt: ")
        while unit != 'dwt' and unit != 'g' and unit != 'ozt':
            print("Must be dwt, g, or ozt")
            unit = input("Select dwt, g, or ozt: ")
        while True:
            gold_weight = input("Enter Weight: ")
            try:
                gold_weight = float(gold_weight)
                break
            except:
                print("Must be a number")
        while True:
            purity = input("Enter Karats: ")
            while purity != '8' and purity != '9' and purity != '10' \
            and purity != '11' and purity != '12' and purity != '13' \
            and purity != '14' and purity != '15' and purity != '16' \
            and purity != '17' and purity != '18' and purity != '19' \
            and purity != '20' and purity != '21' and purity != '21.6' \
            and purity != '22' and purity != '23' and purity != '24':
                print("Must be 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "
                "20, 21, 21.6, 22, 23, or 24")
                purity = input("Enter Karats: ")
            purity = int(purity)
            break
        if unit == 'ozt':
            if purity == 24:
                return '${:,.2f}'.format((gold_price_troy_ounce * gold_weight))
            elif purity == 23:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.043513749) \
                                         * gold_weight)
            elif purity == 22:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.090866293) \
                                         * gold_weight)
            elif purity == 21.6:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.111111111) \
                                         * gold_weight)
            elif purity == 21:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.142852739) \
                                         * gold_weight)
            elif purity == 20:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.200051789) \
                                         * gold_weight)
            elif purity == 19:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.263105894) \
                                         * gold_weight)
            elif purity == 18:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.333333333) \
                                         * gold_weight)
            elif purity == 17:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.411829666) \
                                         * gold_weight)
            elif purity == 16:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.499919087) \
                                         * gold_weight)
            elif purity == 15:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.599991368) \
                                         * gold_weight)
            elif purity == 14:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.714391408) \
                                         * gold_weight)
            elif purity == 13:
                return '${:,.2f}'.format((gold_price_troy_ounce / 1.846824408) \
                                         * gold_weight)
            elif purity == 12:
                return '${:,.2f}'.format((gold_price_troy_ounce / 2) \
                                         * gold_weight)
            elif purity == 11:
                return '${:,.2f}'.format((gold_price_troy_ounce / 2.181973339) \
                                         * gold_weight)    
            elif purity == 10:
                return '${:,.2f}'.format((gold_price_troy_ounce / 2.39979287) \
                                         * gold_weight)
            elif purity == 9:
                return '${:,.2f}'.format((gold_price_troy_ounce / 2.666642691) \
                                         * gold_weight)
            else:
                return '${:,.2f}'.format((gold_price_troy_ounce / 3.000323703) \
                                         * gold_weight)
        if unit == 'dwt':
            if purity == 24:
                return '${:,.2f}'.format((gold_price_troy_ounce / 20.01995162) \
                                         * gold_weight)
            elif purity == 23:
                return '${:,.2f}'.format((gold_price_troy_ounce / 20.87027498) \
                                         * gold_weight)
            elif purity == 22:
                return '${:,.2f}'.format((gold_price_troy_ounce / 21.81748635) \
                                         * gold_weight)
            elif purity == 21.6:
                return '${:,.2f}'.format((gold_price_troy_ounce / 22.22222222) \
                                         * gold_weight)
            elif purity == 21:
                return '${:,.2f}'.format((gold_price_troy_ounce / 22.85723093) \
                                         * gold_weight)
            elif purity == 20:
                return '${:,.2f}'.format((gold_price_troy_ounce / 24.00103578) \
                                         * gold_weight)
            elif purity == 19:
                return '${:,.2f}'.format((gold_price_troy_ounce / 25.26190273) \
                                         * gold_weight)
            elif purity == 18:
                return '${:,.2f}'.format((gold_price_troy_ounce / 26.66666666) \
                                         * gold_weight)
            elif purity == 17:
                return '${:,.2f}'.format((gold_price_troy_ounce / 28.23686214) \
                                         * gold_weight)
            elif purity == 16:
                return '${:,.2f}'.format((gold_price_troy_ounce / 29.99838174) \
                                         * gold_weight)
            elif purity == 15:
                return '${:,.2f}'.format((gold_price_troy_ounce / 31.99982737) \
                                         * gold_weight)
            elif purity == 14:
                return '${:,.2f}'.format((gold_price_troy_ounce / 34.2831501) \
                                         * gold_weight)
            elif purity == 13:
                return '${:,.2f}'.format((gold_price_troy_ounce / 36.92085542) \
                                         * gold_weight)
            elif purity == 12:
                return '${:,.2f}'.format((gold_price_troy_ounce / 40) \
                                         * gold_weight)
            elif purity == 11:
                return '${:,.2f}'.format((gold_price_troy_ounce / 43.63946679) \
                                         * gold_weight)    
            elif purity == 10:
                return '${:,.2f}'.format((gold_price_troy_ounce / 48.0050267) \
                                         * gold_weight)
            elif purity == 9:
                return '${:,.2f}'.format((gold_price_troy_ounce / 53.33381284) \
                                         * gold_weight)
            else:
                return '${:,.2f}'.format((gold_price_troy_ounce / 60.00647406) \
                                         * gold_weight)
        elif unit == 'g':
            if purity == 24:
                return '${:,.2f}'.format((gold_price_troy_ounce / 31.10116018) \
                                         * gold_weight)
            elif purity == 23:
                return '${:,.2f}'.format((gold_price_troy_ounce / 32.45715786) \
                                         * gold_weight)
            elif purity == 22:
                return '${:,.2f}'.format((gold_price_troy_ounce / 33.92971538) \
                                         * gold_weight)
            elif purity == 21.6:
                return '${:,.2f}'.format((gold_price_troy_ounce / 34.56070845) \
                                         * gold_weight)
            elif purity == 21:
                return '${:,.2f}'.format((gold_price_troy_ounce / 35.54650047) \
                                         * gold_weight)
            elif purity == 20:
                return '${:,.2f}'.format((gold_price_troy_ounce / 37.32601746) \
                                         * gold_weight)
            elif purity == 19:
                return '${:,.2f}'.format((gold_price_troy_ounce / 39.28684963) \
                                         * gold_weight)
            elif purity == 18:
                return '${:,.2f}'.format((gold_price_troy_ounce / 41.4766558) \
                                         * gold_weight)
            elif purity == 17:
                return '${:,.2f}'.format((gold_price_troy_ounce / 43.91341683) \
                                         * gold_weight)
            elif purity == 16:
                return '${:,.2f}'.format((gold_price_troy_ounce / 46.65282496) \
                                         * gold_weight)
            elif purity == 15:
                return '${:,.2f}'.format((gold_price_troy_ounce / 49.76510067) \
                                         * gold_weight)
            elif purity == 14:
                return '${:,.2f}'.format((gold_price_troy_ounce / 53.31472435) \
                                         * gold_weight)
            elif purity == 13:
                return '${:,.2f}'.format((gold_price_troy_ounce / 57.41830571) \
                                         * gold_weight)
            elif purity == 12:
                return '${:,.2f}'.format((gold_price_troy_ounce / 62.20637583) \
                                         * gold_weight)
            elif purity == 11:
                return '${:,.2f}'.format((gold_price_troy_ounce / 67.86564158) \
                                         * gold_weight)    
            elif purity == 10:
                return '${:,.2f}'.format((gold_price_troy_ounce / 74.64582315) \
                                         * gold_weight)
            elif purity == 9:
                return '${:,.2f}'.format((gold_price_troy_ounce / 82.94183445) \
                                         * gold_weight)
            else:
                return '${:,.2f}'.format((gold_price_troy_ounce / 93.31739239) \
                                         * gold_weight)
    else:
        while True:
            silver_price_troy_ounce = input("Enter Silver Price: ")
            try:
                silver_price_troy_ounce = float(silver_price_troy_ounce)
                break
            except:
                print("Must be a number")
        unit = input("Select dwt, g, or ozt: ")
        while unit != 'dwt' and unit != 'g' and unit != 'ozt':
            print("Must be dwt, g, or ozt")
            unit = input("Select dwt, g, or ozt: ")
        while True:
            silver_weight = input("Enter Weight: ")
            try:
                silver_weight = float(silver_weight)
                break
            except:
                print("Must be a number")
        while True:
            purity = input("Enter Purity: ")
            while purity != '750' and purity != '800' and purity != '830' \
            and purity != '850' and purity != '875' and purity != '900' \
            and purity != '910' and purity != '920' and purity != '925' \
            and purity != '930' and purity != '935' and purity != '940' \
            and purity != '950' and purity != '9584' and purity != '960' \
            and purity != '970' and purity != '980' and purity != '999':
                print("Must be 750, 800, 830, 850, 875, 900, 910, 920, 925, "
                "930, 935, 940, 950, 9584, 960, 970, 980, or 999")
                purity = input("Enter Purity: ")
            purity = int(purity)
            break
        if unit == 'ozt':
            if purity == 999:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.999) \
                                         * silver_weight)
            elif purity == 980:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.98) \
                                         * silver_weight)
            elif purity == 970:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.97) \
                                         * silver_weight)
            elif purity == 960:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.96) \
                                         * silver_weight)
            elif purity == 9584:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.9584) \
                                         * silver_weight)
            elif purity == 950:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.95) \
                                         * silver_weight)
            elif purity == 940:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.94) \
                                         * silver_weight)
            elif purity == 935:
                return '${:,.2f}'.format((silverprice_troy_ounce * 0.935) \
                                         * silver_weight)
            elif purity == 930:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.93) \
                                         * silver_weight)
            elif purity == 925:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.925) \
                                         * silver_weight)
            elif purity == 920:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.92) \
                                         * silver_weight)
            elif purity == 910:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.91) \
                                         * silver_weight)
            elif purity == 900:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.9) \
                                         * silver_weight)
            elif purity == 875:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.875) \
                                         * silver_weight)    
            elif purity == 850:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.85) \
                                         * silver_weight)
            elif purity == 830:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.83) \
                                         * silver_weight)
            elif purity == 800:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.8) \
                                         * silver_weight)
            else:
                return '${:,.2f}'.format((silver_price_troy_ounce * 0.75) \
                                         * silver_weight)
        elif unit == 'dwt':
            if purity == 999:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 20.02006728) * silver_weight)
            elif purity == 980:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 20.40816326) * silver_weight)
            elif purity == 970:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 20.6185567) * silver_weight)
            elif purity == 960:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 20.83333333) * silver_weight)
            elif purity == 9584:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 20.86819568) * silver_weight)
            elif purity == 950:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.05263157) * silver_weight)
            elif purity == 940:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.27659574) * silver_weight)
            elif purity == 935:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.39037433) * silver_weight)
            elif purity == 930:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.50537634) * silver_weight)
            elif purity == 925:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.62162162) * silver_weight)
            elif purity == 920:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.73913043) * silver_weight)
            elif purity == 910:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 21.97802197) * silver_weight)
            elif purity == 900:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 22.22222222) * silver_weight)
            elif purity == 875:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 22.85714285) * silver_weight)
            elif purity == 850:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 23.52941176) * silver_weight)
            elif purity == 830:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 24.096388554) * silver_weight)
            elif purity == 800:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 25) * silver_weight)
            else:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 26.66666666) * silver_weight)
        else:
            if purity == 999:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 31.13469058) * silver_weight)
            elif purity == 980:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 31.73830866) * silver_weight)
            elif purity == 970:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 32.06534069) * silver_weight)
            elif purity == 960:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 32.39918237) * silver_weight)
            elif purity == 9584:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 32.45374002) * silver_weight)
            elif purity == 950:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 32.7406806) * silver_weight)
            elif purity == 940:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 33.08880911) * silver_weight)
            elif purity == 935:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 33.26599062) * silver_weight)
            elif purity == 930:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 33.44442034) * silver_weight)
            elif purity == 925:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 33.62544113) * silver_weight)
            elif purity == 920:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 32.80843217) * silver_weight)
            elif purity == 910:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 34.17876622) * silver_weight)
            elif purity == 900:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 34.55934793) * silver_weight)
            elif purity == 875:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 35.54661301) * silver_weight)
            elif purity == 850:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 36.59194373) * silver_weight)
            elif purity == 830:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 37.47403773) * silver_weight)
            elif purity == 800:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 38.97946449) * silver_weight)
            else:
                return '${:,.2f}'.format((silver_price_troy_ounce \
                                          / 41.47104851) * silver_weight)