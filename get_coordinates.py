def get_coordinates():
    valid_input_one = 0
    coord = [0, 0]
    while valid_input_one == 0:
        print("(M) Men's Apparel\n(W) Women's Apparel\n(CA) Children's Apparel\n(A) Accessories")
        print("(S) Shoes\n(O) Optical\n(DS) Department Stores\n(H) Home and Leisure\n(J) Just For Kids")
        print("(B) Health, Beauty, Athletics\n(CO) Connections\n(D) Dining\n(E) Entertainment")
        input_one = input("\nInput the option in parentheses: ")

        match input_one:
            case "M":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(AF) Abercrombie & Fitch\n(AE) American Eagle\n(BR) Banana Republic")
                    print("(BC) Buckeye Corner\n(BU) Buckle\n(BB) Burberry\n(C) Coach")
                    print("(EB) Eddie Bauer\n(EM) Express Men\n(F) Filson\n(FL) Foot Locker")
                    print("(FX) Forever XXI\n(G) Gap\n(HM) H&M\n(HC) Hollister Co.")
                    print("(HOM) Homage\n(HT) Hot Topic\n(JC) J. Crew\n(LL) L.L. Bean\n(LV) Louis Vuitton")
                    print("(LU) lululemon\n(NF) The North Face\n(P) PacSun\n(TB) Tommy Bahama")
                    print("(V) vineyard vines\n(Z) Zara\n(ZU) Zumiez")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "AF":
                            valid_input_two = 1
                            coord = [388, 1015]
                        case "AE":
                            valid_input_two = 1
                            coord = [387, 711]
                        case "BR":
                            valid_input_two = 1
                            coord = [387, 1063]
                        case "BC":
                            valid_input_two = 1
                            coord = [167, 911]
                        case "BU":
                            valid_input_two = 1
                            coord = [399, 937]
                        case "BB":
                            valid_input_two = 1
                            coord = [422, 394]
                        case "C":
                            valid_input_two = 1
                            coord = [478, 396]
                        case "EB":
                            valid_input_two = 1
                            coord = [576, 781]
                        case "EM":
                            valid_input_two = 1
                            coord = [517, 563]
                        case "F":
                            valid_input_two = 1
                            coord = [460, 1015]
                        case "FL":
                            valid_input_two = 1
                            coord = [540, 900]
                        case "FX":
                            valid_input_two = 1
                            coord = [421, 821]
                        case "G":
                            valid_input_two = 1
                            coord = [525, 1028]
                        case "HM":
                            valid_input_two = 1
                            coord = [491, 934]
                        case "HC":
                            valid_input_two = 1
                            coord = [77, 863]
                        case "HOM":
                            valid_input_two = 1
                            coord = [654, 1026]
                        case "HT":
                            valid_input_two = 1
                            coord = [80, 878]
                        case "JC":
                            valid_input_two = 1
                            coord = [519, 1148]
                        case "LL":
                            valid_input_two = 1
                            coord = [244, 374]
                        case "LV":
                            valid_input_two = 1
                            coord = [475, 470]
                        case "LU":
                            valid_input_two = 1
                            coord = [383, 600]
                        case "NF":
                            valid_input_two = 1
                            coord = [546, 777]
                        case "P":
                            valid_input_two = 1
                            coord = [492, 967]
                        case "TB":
                            valid_input_two = 1
                            coord = [430, 421]
                        case "V":
                            valid_input_two = 1
                            coord = [517, 701]
                        case "Z":
                            valid_input_two = 1
                            coord = [517, 727]
                        case "ZU":
                            valid_input_two = 1
                            coord = [492, 993]
                        case _:
                            print("Invalid Input, try again")
            case "W":
                valid_input_one = 1
                valid_input_two = 0

                while valid_input_two == 0:
                    print("(AF) Abercrombie & Fitch\n(AE) American Eagle\n(AR) Aerie\n(AT) Ann Taylor")
                    print("(AN) Anthropologie\n(ATH) Athleta\n(BR) Banana Republic\n(BC) Buckeye Corner")
                    print("(BU) Buckle\n(BB) Burberry\n(CH) Chico's\n(EB) Eddie Bauer\n(ELQ) ELOQUII")
                    print("(EV) Evereve\n(EX) Express\n(F) Filson\n(FX) Forever XXI\n(FC) Francesca's Collections")
                    print("(FP) Free People\n(G) Gap\n(HM) H&M\n(HC) Hollister Co.\n(HOM) Homage")
                    print("(HT) Hot Topic\n(JC) J. Crew\n(JJ) J. Jill\n(KS) kate spade new york\n(LL) L.L. Bean")
                    print("(LS) La Senza\n(LFL) Lady Foot Locker\n(LB) Lane Bryant\n(LP) Lilly Pulitzer")
                    print("(LOFT) LOFT\n(LV) Louis Vuitton\n(LU) lululemon\n(MW) Madewell")
                    print("(MK) Michael Kors\n(NYC) New York & Company\n(NF) The North Face")
                    print("(PS) PacSun\n(PP) A Pea in the Pod\n(PINK) PINK\n(SM) Scout & Molly's")
                    print("(SS) Soft Surroundings\n(TB) Tommy Bahama\n(T) Torrid\n(VS) Victoria's Secret")
                    print("(V) vineyard vines\n(WHBM) White House | Black Market\n(Z) Zara\n(ZU) Zumiez")

                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "AF":
                            valid_input_two = 1
                            coord = [388, 1015]
                        case "AE":
                            valid_input_two = 1
                            coord = [387, 711]
                        case "AR":
                            valid_input_two = 1
                            coord = [387, 711]
                        case "AT":
                            valid_input_two = 1
                            coord = [470,421]
                        case "AN":
                            valid_input_two = 1
                            coord = [432, 331]
                        case "ATH":
                            valid_input_two = 1
                            coord = [384, 674]
                        case "BR":
                            valid_input_two = 1
                            coord = [387, 1063]
                        case "BC":
                            valid_input_two = 1
                            coord = [167, 911]
                        case "BU":
                            valid_input_two = 1
                            coord = [399, 937]
                        case "BB":
                            valid_input_two = 1
                            coord = [422, 394]
                        case "CH":
                            valid_input_two = 1
                            coord = [521, 1121]
                        case "EB":
                            valid_input_two = 1
                            coord = [576, 781]
                        case "ELQ":
                            valid_input_two = 1
                            coord = [384, 655]
                        case "EV":
                            valid_input_two = 1
                            coord = [628, 652]
                        case "EX":
                            valid_input_two = 1
                            coord = [515, 549]
                        case "F":
                            valid_input_two = 1
                            coord = [460, 1015]
                        case "FX":
                            valid_input_two = 1
                            coord = [421, 821]
                        case "FC":
                            valid_input_two = 1
                            coord = [450, 976]
                        case "FP":
                            valid_input_two = 1
                            coord = [629, 726]
                        case "G":
                            valid_input_two = 1
                            coord = [525, 1028]
                        case "HM":
                            valid_input_two = 1
                            coord = [491, 934]
                        case "HC":
                            valid_input_two = 1
                            coord = [77, 863]
                        case "HOM":
                            valid_input_two = 1
                            coord = [654, 1026]
                        case "HT":
                            valid_input_two = 1
                            coord = [80, 878]
                        case "JC":
                            valid_input_two = 1
                            coord = [519, 1148]
                        case "JJ":
                            valid_input_two = 1
                            coord = [383, 616]
                        case "KS":
                            valid_input_two = 1
                            coord = [430, 361]
                        case "LL":
                            valid_input_two = 1
                            coord = [244, 374]
                        case "LS":
                            valid_input_two = 1
                            coord = [485, 847]
                        case "LFL":
                            valid_input_two = 1
                            coord = [525, 895]
                        case "LB":
                            valid_input_two = 1
                            coord = [549, 512]
                        case "LP":
                            valid_input_two = 1
                            coord = [519, 678]
                        case "LOFT":
                            valid_input_two = 1
                            coord = [517, 679]
                        case "LV":
                            valid_input_two = 1
                            coord = [475, 470]
                        case "LU":
                            valid_input_two = 1
                            coord = [383, 600]
                        case "MW":
                            valid_input_two = 1
                            coord = [431,380]
                        case "MK":
                            valid_input_two = 1
                            coord = [433, 471]
                        case "KS":
                            valid_input_two = 1
                            coord = [431, 360]
                        case "NF":
                            valid_input_two = 1
                            coord = [546, 777]
                        case "PS":
                            valid_input_two = 1
                            coord = [492, 967]
                        case "PP":
                            valid_input_two = 1
                            coord = [420, 622]
                        case "PINK":
                            valid_input_two = 1
                            coord = [516, 577]
                        case "SM":
                            valid_input_two = 1
                            coord = [629, 636]
                        case "SS":
                            valid_input_two = 1
                            coord = [520, 1089]
                        case "TB":
                            valid_input_two = 1
                            coord = [430, 421]
                        case "T":
                            valid_input_two = 1
                            coord = [565, 512]
                        case "VS":
                            valid_input_two = 1
                            coord = [382, 557]
                        case "V":
                            valid_input_two = 1
                            coord = [517, 701]
                        case "WHBM":
                            valid_input_two = 1
                            coord = [384, 577]
                        case "Z":
                            valid_input_two = 1
                            coord = [517, 727]
                        case "ZU":
                            valid_input_two = 1
                            coord = [492, 993]
                        case _:
                            print("Invalid Input, try again")
            case "CA":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(A) Abercrombie\n(AG) American Girl\n(BG) babyGap\n(CP) The Children's Place")
                    print("(FX) Forever XXI\n(GK) GapKids\n(GY) Gymboree\n(HM) H&M")
                    print("(HA) Hanna Andersson\n(JC) J. Crew\n(JU) Justice\n(KF) Kids Foot Locker")
                    print("(LL) L.L. Bean\n(V) vineyard vines\n(Z) Zara")

                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "A":
                            valid_input_two = 1
                            coord = [350, 1025]
                        case "AG":
                            valid_input_two = 1
                            coord = [530, 647]
                        case "BG":
                            valid_input_two = 1
                            coord = [568, 1027]
                        case "CP":
                            valid_input_two = 1
                            coord = [627, 693]
                        case "FX":
                            valid_input_two = 1
                            coord = [421, 821]
                        case "GK":
                            valid_input_two = 1
                            coord = [544, 1028]
                        case "GY":
                            valid_input_two = 1
                            coord = [629, 682]
                        case "HM":
                            valid_input_two = 1
                            coord = [491, 934]
                        case "HA":
                            valid_input_two = 1
                            coord = [481, 699]
                        case "JC":
                            valid_input_two = 1
                            coord = [519, 1148]
                        case "JU":
                            valid_input_two = 1
                            coord = [385, 691]
                        case "KF":
                            valid_input_two = 1
                            coord = [421, 839]
                        case "LL":
                            valid_input_two = 1
                            coord = [244, 374]
                        case "V":
                            valid_input_two = 1
                            coord = [517, 701]
                        case "Z":
                            valid_input_two = 1
                            coord = [517, 727]
                        case _:
                            print("Invalid Input, try again")
            case "A":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(AJ) Andrews Jewelers\n(BC) Brighton Collectibles\n(CL) Claire's")
                    print("(C) Coach\n(DW) Dakota Watch Company\n(DC) Diamond Cellar\n(F) Filson\n(FO) Fossil")
                    print("(HB) Henri Bendel\n(KSN) kate spade new york\n(KJ) Kay Jewelers\n(KSC) Kendra Scott")
                    print("(L) Lids\n(LV) Louis Vuitton\n(MK) Michael Kors\n(OY) Occasionally Yours\n(P) Pandora")
                    print("(SH) Shinola\n(SM) Silver Mountain Jewelry\n(SW) Stitch Wow\n(S) Swarovski\n(TC) Tiffany & Co")
                    print("(T) Tumi\n(Z) Zales")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "AJ":
                            valid_input_two = 1
                            coord = [482, 653]
                        case "BC":
                            valid_input_two = 1
                            coord = [472, 374]
                        case "CL":
                            valid_input_two = 1
                            coord = [491, 979]
                        case "C":
                            valid_input_two = 1
                            coord = [478, 396]
                        case "DW":
                            valid_input_two = 1
                            coord = [449, 839]
                        case "DC":
                            valid_input_two = 1
                            coord = [310, 509]
                        case "F":
                            valid_input_two = 1
                            coord = [460, 1015]
                        case "FO":
                            valid_input_two = 1
                            coord = [489, 864]
                        case "HB":
                            valid_input_two = 1
                            coord = [520, 513]
                        case "KSN":
                            valid_input_two = 1
                            coord = [431, 360]
                        case "KJ":
                            valid_input_two = 1
                            coord = [422, 729]
                        case "KSC":
                            valid_input_two = 1
                            coord = [330, 453]
                        case "L":
                            valid_input_two = 1
                            coord = [432, 995]
                        case "LV":
                            valid_input_two = 1
                            coord = [475, 470]
                        case "MK":
                            valid_input_two = 1
                            coord = [433, 471]
                        case "OY":
                            valid_input_two = 1
                            coord = [518, 607]
                        case "P":
                            valid_input_two = 1
                            coord = [480, 718]
                        case "SH":
                            valid_input_two = 1
                            coord = [445, 1017]
                        case "SM":
                            valid_input_two = 1
                            coord = [535, 916]
                        case "SW":
                            valid_input_two = 1
                            coord = [658, 662]
                        case "S":
                            valid_input_two = 1
                            coord = [522, 778]
                        case "TC":
                            valid_input_two = 1
                            coord = [497, 484]
                        case "T":
                            valid_input_two = 1
                            coord = [432, 346]
                        case "Z":
                            valid_input_two = 1
                            coord = [494, 896]
                        case _:
                            print("Invalid Input, try again")
            case "S":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(AS) Aldo Shoes\n(CS) Champs Sports\n(C) Clarks\n(FF) Flip Flop Shops")
                    print("(FL) Foot Locker\n(J) Journeys\n(JK) Journeys Kidz\n(KFL) Kids Foot Locker")
                    print("(LFL) Lady Foot Locker\n(LS) Lucky Shoes\n(NB) New Balance\n(SK) Skechers")
                    print("(WC) Walking Company")

                    input_one = input("\nInput the option in parentheses: ")
                    match input_one:
                        case "AS":
                            valid_input_two = 1
                            coord = [407, 990]
                        case "CS":
                            valid_input_two = 1
                            coord = [561, 780]
                        case "C":
                            valid_input_two = 1
                            coord = [420, 712]
                        case "FF":
                            valid_input_two = 1
                            coord = [550, 626]
                        case "FL":
                            valid_input_two = 1
                            coord = [537, 897]
                        case "J":
                            valid_input_two = 1
                            coord = [493, 947]
                        case "JK":
                            valid_input_two = 1
                            coord = [493, 955]
                        case "KFL":
                            valid_input_two = 1
                            coord = [421, 839]
                        case "LFL":
                            valid_input_two = 1
                            coord = [527, 895]
                        case "LS":
                            valid_input_two = 1
                            coord = [153, 1151]
                        case "NB":
                            valid_input_two = 1
                            coord = [138, 1151]
                        case "SK":
                            valid_input_two = 1
                            coord = [423, 743]
                        case "WC":
                            valid_input_two = 1
                            coord = [491, 878]
                        case _:
                            print("Invalid Input, try again")
            case "O":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(LC) LensCrafters\n(OK) Oakley\n(SE) SEE\n(SH) Sunglass Hut")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "LC":
                            valid_input_two = 1
                            coord = [604, 1027]
                        case "OK":
                            valid_input_two = 1
                            coord = [417, 854]
                        case "SE":
                            valid_input_two = 1
                            coord = [418, 701]
                        case "SH":
                            valid_input_two = 1
                            coord = [405, 1003]
                        case _:
                            print("Invalid Input, try again")
            case "DS":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(M) Macy's\n(N) Nordstrom")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "M":
                            valid_input_two = 1
                            coord = [627, 532]
                        case "N":
                            valid_input_two = 1
                            coord = [450, 291]
                        case _:
                            print("Invalid Input, try again")
            case "H":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(A) Apple\n(BN) Barnes & Noble\n(BD) Bink Davies\n(BO) Bose")
                    print("(CL) Celebrate Local\n(CB) Crate & Barrel\n(HU) Holiday House at Urban Home & Garden")
                    print("(MS) Microsoft\n(PS) Paper Source\n(PB) Pottery Barn\n(RH) Restoration Hardware")
                    print("(TS) The Shade Store\n(SL) Sur La Table\n(TM) Tesla Motors\n(TR) Things Remembered")
                    print("(TB) Tinder Box\n(WE) west elm\n(WB) White Barn\n(WS) Williams Sonoma")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "A":
                            valid_input_two = 1
                            coord = [469, 354]
                        case "BN":
                            valid_input_two = 1
                            coord = [478, 1193]
                        case "BD":
                            valid_input_two = 1
                            coord = [491, 1005]
                        case "BO":
                            valid_input_two = 1
                            coord = [451, 902]
                        case "CL":
                            valid_input_two = 1
                            coord = [344, 1154]
                        case "CB":
                            valid_input_two = 1
                            coord = [392, 1191]
                        case "HU":
                            valid_input_two = 1
                            coord = [518, 593]
                        case "MS":
                            valid_input_two = 1
                            coord = [418, 867]
                        case "PS":
                            valid_input_two = 1
                            coord = [627, 740]
                        case "PB":
                            valid_input_two = 1
                            coord = [389, 1123]
                        case "RH":
                            valid_input_two = 1
                            coord = [389, 1149]
                        case "TS":
                            valid_input_two = 1
                            coord = [328, 1152]
                        case "SL":
                            valid_input_two = 1
                            coord = [350, 512]
                        case "TM":
                            valid_input_two = 1
                            coord = [384, 739]
                        case "TR":
                            valid_input_two = 1
                            coord = [418, 687]
                        case "TB":
                            valid_input_two = 1
                            coord = [612, 1151]
                        case "WE":
                            valid_input_two = 1
                            coord = [623, 1028]
                        case "WB":
                            valid_input_two = 1
                            coord = [476, 826]
                        case "WS":
                            valid_input_two = 1
                            coord = [519, 1068]
                        case _:
                            print("Invalid Input, try again")
            case "J":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(A) American Girl\n(B) Build-A-Bear Workshop")
                    print("(GG) Games Galore\n(GL) Gee Lillie")
                    print("(L) LEGO")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "A":
                            valid_input_two = 1
                            coord = [529, 650]
                        case "B":
                            valid_input_two = 1
                            coord = [630, 611]
                        case "GG":
                            valid_input_two = 1
                            coord = [162, 890]
                        case "GL":
                            valid_input_two = 1
                            coord = [628, 713]
                        case "L":
                            valid_input_two = 1
                            coord = [479, 741]
                        case _:
                            print("Invalid Input, try again")
            case "B":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(AS) Art of Shaving\n(AN) Avalon Nails\n(AV) Aveda\n(BBW) Bath & Body Works")
                    print("(TBS) The Body Shop\n(CAP) Columbus Aesthetic & Plastic Surgery")
                    print("(TDC) The Dental Center\n(GNC) GNC\n(JMC) James Mammography Center")
                    print("(LC) LasikPlus Columbus\n(LTF) Life Time Fitness/LifeClinic\n(LO) L'Occitane")
                    print("(LU) LUSH\n(MAC) MAC Cosmetics\n(ME) Miracle Eyebrows\n(MN) Modern Nails")
                    print("(SC) Saribalas Clinic\n(SCT) Scentology\n(S) Sephora\n(WK) WomanKind Ob/Gyn")

                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "AS":
                            valid_input_two = 1
                            coord = [482, 676]
                        case "AN":
                            valid_input_two = 1
                            coord = [661, 608]
                        case "AV":
                            valid_input_two = 1
                            coord = [419, 662]
                        case "BBW":
                            valid_input_two = 1
                            coord = [476, 835]
                        case "TBS":
                            valid_input_two = 1
                            coord = [427, 1100]
                        case "CAP":
                            valid_input_two = 1
                            coord = [665, 899]
                        case "TDC":
                            valid_input_two = 1
                            coord = [662, 916]
                        case "GNC":
                            valid_input_two = 1
                            coord = [168, 1154]
                        case "JMC":
                            valid_input_two = 1
                            coord = [679, 578]
                        case "LC":
                            valid_input_two = 1
                            coord = [664, 929]
                        case "LTF":
                            valid_input_two = 1
                            coord = [261, 1000]
                        case "LO":
                            valid_input_two = 1
                            coord = [481, 588]
                        case "LU":
                            valid_input_two = 1
                            coord = [491, 1021]
                        case "MAC":
                            valid_input_two = 1
                            coord = [477, 779]
                        case "ME":
                            valid_input_two = 1
                            coord = [83, 897]
                        case "MN":
                            valid_input_two = 1
                            coord = [33, 859]
                        case "SC":
                            valid_input_two = 1
                            coord = [661, 941]
                        case "SCT":
                            valid_input_two = 1
                            coord = [467, 886]
                        case "S":
                            valid_input_two = 1
                            coord = [471, 446]
                        case "WK":
                            valid_input_two = 1
                            coord = [669, 954]
                        case _:
                            print("Invalid Input, try again")
            case "CO":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(A) AT&T Experience\n(ES) Easton Station News\n(EC) Experience Columbus")
                    print("(S) Sprint\n(T) T-Mobile")
                    input_one = input("\nInput the option in parentheses: ")
                    match input_one:
                        case "A":
                            valid_input_two = 1
                            coord = [344, 1195]
                        case "ES":
                            valid_input_two = 1
                            coord = [467, 873]
                        case "EC":
                            valid_input_two = 1
                            coord = [476, 805]
                        case "S":
                            valid_input_two = 1
                            coord = [236, 1153]
                        case "T":
                            valid_input_two = 1
                            coord = [71, 919]
                        case _:
                            print("Invalid Input, try again")
            case "D":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(AB) Abuelo's\n(AG) Adobe Gila's\n(AGB) American Girl Bistro\n(AA) Auntie Anne's")
                    print("(BL) Bar Louie\n(BMG) bd's Mongolian Grill\n(BEB) Berry Blendz\n(BIB) Bibibop")
                    print("(BVB) Bon Vie Bistro\n(BTG) Brio Tuscan Grille\n(BTJ) Bubbles Tea & Juice Co.")
                    print("(CBN) Cafe Bistro at Nordstrom\n(CIMC) Cafe Istanbul Mediterranean Cuisine\n(CZ) Cafe Zupas")
                    print("(CF) Cheesecake Factory\n(CH) Cheryl's\n(CMG) Chipotle Mexican Grill\n(CB) Cinnabon")
                    print("(CT) Condado Tacos\n(CHWR) Cooper's Hawk Winery & Restaurant\n(DT) DAVIDsTEA")
                    print("(E) ebar at Nordstrom\n(FIP) Fado Irish Pub\n(FGBF) Five Guys Burgers & Fries")
                    print("(FS) Flip Side\n(GD) Godiva\n(GI) Graeter's Ice Cream\n(IS) IT SUGAR")
                    print("(JS) Jeni's Splendid Ice Creams\n(KG) Kona Grill\n(LC) LifeCafe at Life Time Fitness")
                    print("(MS) McCormick & Schmick's Seafood Restaurant\n(TMP) The Melting Pot")
                    print("(MOC) Mitchell's Ocean Club\n(NC) Northstar Cafe\n(PF) P.F. Chang's China Bistro")
                    print("(PE) Panda Express\n(PB) Panera Bread\n(PD) Piada\n(RB) Rusty Bucket\n(SB) Sbarro")
                    print("(SC) See's Candies\n(SW) Smith & Wollensky\n(SC) Starbucks Cafe\n(TB) Texas de Brazil")
                    print("(TJ) Trader Joe's\n(WB) World of Beer")
                    print("(ZJ) Zest Juice Co.")

                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "AB":
                            valid_input_two = 1
                            coord = [304, 730]
                        case "AG":
                            valid_input_two = 1
                            coord = [124, 931]
                        case "AGB":
                            valid_input_two = 1
                            coord = [549, 650]
                        case "AA":
                            valid_input_two = 1
                            coord = [406, 950]
                        case "BL":
                            valid_input_two = 1
                            coord = [94, 932]
                        case "BMG":
                            valid_input_two = 1
                            coord = [304, 377]
                        case "BEB":
                            valid_input_two = 1
                            coord = [679, 568]
                        case "BIB":
                            valid_input_two = 1
                            coord = [122, 842]
                        case "BVB":
                            valid_input_two = 1
                            coord = [450, 589]
                        case "BTG":
                            valid_input_two = 1
                            coord = [453, 1064]
                        case "BTJ":
                            valid_input_two = 1
                            coord = [164, 865]
                        case "CBN":
                            valid_input_two = 1
                            coord = [465, 278]
                        case "CIMC":
                            valid_input_two = 1
                            coord = [332, 346]
                        case "CZ":
                            valid_input_two = 1
                            coord = [263, 338]
                        case "CF":
                            valid_input_two = 1
                            coord = [420, 1217]
                        case "CH":
                            valid_input_two = 1
                            coord = [423, 808]
                        case "CMG":
                            valid_input_two = 1
                            coord = [623, 1151]
                        case "CB":
                            valid_input_two = 1
                            coord = [397, 888]
                        case "CT":
                            valid_input_two = 1
                            coord = [588, 610]
                        case "CHWR":
                            valid_input_two = 1
                            coord = [503, 333]
                        case "DT":
                            valid_input_two = 1
                            coord = [430, 651]
                        case "E":
                            valid_input_two = 1
                            coord = [466, 266]
                        case "FIP":
                            valid_input_two = 1
                            coord = [590, 1141]
                        case "FGBF":
                            valid_input_two = 1
                            coord = [123, 909]
                        case "FS":
                            valid_input_two = 1
                            coord = [325, 1069]
                        case "GD":
                            valid_input_two = 1
                            coord = [423, 674]
                        case "GI":
                            valid_input_two = 1
                            coord = [493, 916]
                        case "IS":
                            valid_input_two = 1
                            coord = [400, 963]
                        case "JS":
                            valid_input_two = 1
                            coord = [451, 743]
                        case "KG":
                            valid_input_two = 1
                            coord = [585, 550]
                        case "LC":
                            valid_input_two = 1
                            coord = [261, 1021]
                        case "MS":
                            valid_input_two = 1
                            coord = [302, 573]
                        case "TMP":
                            valid_input_two = 1
                            coord = [548, 1149]
                        case "MOC":
                            valid_input_two = 1
                            coord = [174, 933]
                        case "NC":
                            valid_input_two = 1
                            coord = [537, 1195]
                        case "PF":
                            valid_input_two = 1
                            coord = [656, 1140]
                        case "PE":
                            valid_input_two = 1
                            coord = [456, 959]
                        case "PB":
                            valid_input_two = 1
                            coord = [297, 1147]
                        case "PD":
                            valid_input_two = 1
                            coord = [591, 1067]
                        case "RB":
                            valid_input_two = 1
                            coord = [587, 738]
                        case "SB":
                            valid_input_two = 1
                            coord = [441, 960]
                        case "SC":
                            valid_input_two = 1
                            coord = [422, 795]
                        case "SW":
                            valid_input_two = 1
                            coord = [397, 489]
                        case "SC":
                            valid_input_two = 1
                            coord = [576, 1063]
                        case "TB":
                            valid_input_two = 1
                            coord = [668, 1025]
                        case "TJ":
                            valid_input_two = 1
                            coord = [182, 1151]
                        case "WB":
                            valid_input_two = 1
                            coord = [274, 1151]
                        case "ZC":
                            valid_input_two = 1
                            coord = [593, 667]
                        case _:
                            print("Invalid Input, try again")
            case "E":
                valid_input_one = 1
                valid_input_two = 0
                while valid_input_two == 0:
                    print("(A) AMC Easton\n(F) Funny Bone")
                    input_one = input("\nInput the option in parentheses: ")
                    match input_one:
                        case "A":
                            valid_input_two = 1
                            coord = [122, 793]
                        case "F":
                            valid_input_two = 1
                            coord = [328, 952]
                        case _:
                            print("Invalid Input, try again")
            case _:
                print("Invalid Input, try again")
    return coord