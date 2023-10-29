print("What type of area are you closest to?")

def find_location():
    valid_input_one = 0
    while (valid_input_one == 0):
        print("(M) Men's Apparel\n(W) Women's Apparel\n(C) Children's Apparel\n(A) Accessories")
        print("(S) Shoes\n(O) Optical\n(D) Department Stores\n(H) Home and Leisure\n(J) Just For Kids")
        print("(B) Health, Beauty, Athletics\n(P) Phone Providers\n(D) Dining\n(E) Entertainment")
        print("(GS) Gateway Shopping\n(GD) Gateway Dining")
        input_one = input("\nInput the option in parentheses: ")

        coord = (0,0)

        match input_one:
            case "M":
                valid_input_one = 1
                valid_input_two = 0
                while (valid_input_two == 0):
                    print("(AF) Abercrombie & Fitch\n(AE) American Eagle\n(BR) Banana Republic")
                    print("(BC) Buckeye Corner\n(BU) Buckle\n(BB) Burberry\n(C) Coach")
                    print("(EB) Eddie Bauer\n(EM) Express Men\n(F) Filson\n(FL) Foot Locker")
                    print("(FX) Forever XXI\n(G) Gap\n(HM) H&M\n(HC) Hollister Co.")
                    print("(H) Hornage\n(HT) Hot Topic\n(J) J. Crew\n(L) L.L. Bean\n(LV) Louis Vuitton")
                    print("(LL) lululemon\n(NF) The North Face\n(P) PacSun\n(T) Tommy Bahama")
                    print("(V) vineyard vines\n(Z) Zara\n(ZU) Zumiez")
                    input_one = input("\nInput the option in parentheses: ")

                    match input_one:
                        case "AF":
                            valid_input_two = 1
                            coord = (388, 1015)
                        case "AE":
                            valid_input_two = 1
                            coord = (387, 711)
                        case "BR":
                            valid_input_two = 1
                            print("TEST")
                        case "BC":
                            valid_input_two = 1
                            print("TEST")
                        case "BU":
                            valid_input_two = 1
                            print("TEST")
                        case "BB":
                            valid_input_two = 1
                            print("TEST")
                        case "C":
                            valid_input_two = 1
                            print("TEST")
                        case "EB":
                            valid_input_two = 1
                            print("TEST")
                        case "EM":
                            valid_input_two = 1
                            print("TEST")
                        case "F":
                            valid_input_two = 1
                            print("TEST")
                        case "FL":
                            valid_input_two = 1
                            print("TEST")
                        case "G":
                            valid_input_two = 1
                            print("TEST")
                        case "HM":
                            valid_input_two = 1
                            print("TEST")
                        case "HC":
                            valid_input_two = 1
                            print("TEST")
                        case "H":
                            valid_input_two = 1
                            print("TEST")
                        case "HT":
                            valid_input_two = 1
                            print("TEST")
                        case "J":
                            valid_input_two = 1
                            print("TEST")
                        case "L":
                            valid_input_two = 1
                            print("TEST")
                        case "LV":
                            valid_input_two = 1
                            print("TEST")
                        case "LL":
                            valid_input_two = 1
                            print("TEST")
                        case "NF":
                            valid_input_two = 1
                            print("TEST")
                        case "P":
                            valid_input_two = 1
                            print("TEST")
                        case "T":
                            valid_input_two = 1
                            print("TEST")
                        case "V":
                            valid_input_two = 1
                            print("TEST")
                        case "Z":
                            valid_input_two = 1
                            print("TEST")
                        case "ZU":
                            valid_input_two = 1
                            print("TEST")
                        case _:
                            print("Invalid Input, try again")
            case "W":
                valid_input_one = 1
                print("TEST")
            case "C":
                valid_input_one = 1
                print("TEST")
            case "A":
                valid_input_one = 1
                print("TEST")
            case "S":
                valid_input_one = 1
                print("TEST")
            case "O":
                valid_input_one = 1
                print("TEST")
            case "D":
                valid_input_one = 1
                print("TEST")
            case "H":
                valid_input_one = 1
                print("TEST")
            case "J":
                valid_input_one = 1
                print("TEST")
            case "B":
                valid_input_one = 1
                print("TEST")
            case "P":
                valid_input_one = 1
                print("TEST")
            case "D":
                valid_input_one = 1
                print("TEST")
            case "E":
                valid_input_one = 1
                print("TEST")
            case "GS":
                valid_input_one = 1
                print("TEST")
            case "GD":
                valid_input_one = 1
                print("TEST")
            case _:
              print("Invalid Input, try again")

    return coord

print(find_location())
