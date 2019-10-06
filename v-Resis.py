import sys
import os

os.system('clear')

def logo():
    print ("""
              =========================
            ==  ))  ))  ))  ))    ) )  ==
============    ))  ))  ))  ))    ) )    ============
            ==  ))  ))  ))  ))    ) )  ==
              =========================

      <<<<  v-Resis : Count The Resistor  >>>>
      """)

def men():
    menu = {"1":"4 Ring", "2":"5 Ring"}
    for i in menu:
        print (i ,"==>",menu[i])

    pilih = input('Choose : ')
    if pilih == "1":
        empat()
    elif pilih == "2":
        lima()
    else:
        os.system('clear')
        print ("Number Please")
        men()

def empat():
    def a():
        os.system('clear')
        print ("""
                                    =========================
                                  ==     ))  ))  ))    ) )   ==
                      ============       ))  ))  ))    ) )    ============
                                  ==     ))  ))  ))    ) )   ==
                                    =========================

                            <<<<  v-Resis : Count The Resistor  >>>>
                            <<<<            4 Ring            >>>>
        """)
        print ("""
|========(Ring 1 & 2)========|=============(Ring 3)==============|===========(Ring 4)===========|
|> BLACK  = 0   > GREEN  = 5 |> BLACK  = 10**0   > GREEN  = 10**5 |> BROWN = 1%   > SILVER = 10%|
|> BROWN  = 1   > BLUE   = 6 |> BROWN  = 10**1   > BLUE   = 10**6 |> RED   = 2%                 |
|> RED    = 2   > PURPLE = 7 |> RED    = 10**2   > PURPLE = 10**7 |> GREEN = 0.5%               |
|> ORANGE = 3   > GRAY   = 8 |> ORANGE = 10**3   > GRAY   = 10**8 |> BLUE  = 0.10%              |
|> YELLOW = 4   > WHITE  = 9 |> YELLOW = 10**4   > WHITE  = 10**9 |> GOLD  = 5%                 |
=================================================================================================
    """)
        print ("Please Enter Ring's Color ")
        a = input('\nRing  1 : ').upper()
        if a == "BLACK":
            a = 0
        elif a == "BROWN":
            a = 1
        elif a == "RED":
            a = 2
        elif a == "ORANGE":
            a = 3
        elif a == "YELLOW":
            a = 4
        elif a == "GREEN":
            a = 5
        elif a == "BLUE":
            a = 6
        elif a == "PURPLE":
            a = 7
        elif a == "GRAY":
            a = 8
        elif a == "WHITE":
            a = 9
        else:
            print ("\nRing Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                empat()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)

        b = input('Ring  2 : ').upper()
        if b == "BLACK":
            b = str(a) + str(0)
        elif b == "BROWN":
            b = str(a) + str(1)
        elif b == "RED":
            b = str(a) + str(2)
        elif b == "ORANGE":
            b = str(a) + str(3)
        elif b == "YELLOW":
            b = str(a) + str(4)
        elif b == "GREEN":
            b = str(a) + str(5)
        elif b == "BLUE":
            b = str(a) + str(6)
        elif b == "PURPLE":
            b = str(a) + str(7)
        elif b == "GRAY":
            b = str(a) + str(8)
        elif b == "WHITE":
            b = str(a) + str(9)
        else:
            print ("\nRing Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                empat()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)

        c = input('Ring  3 : ').upper()
        if c == "BLACK":
            c = 10**0
        elif c == "BROWN":
            c = 10**1
        elif c == "RED":
            c = 10**2
        elif c == "ORANGE":
            c = 10**3
        elif c == "YELLOW":
            c = 10**4
        elif c == "GREEN":
            c = 10**5
        elif c == "BLUE":
            c = 10**6
        elif c == "PURPLE":
            c = 10**7
        elif c == "GRAY":
            c = 10**8
        elif c == "WHITE":
            c = 10**9
        else:
            print ("\nMultiplier Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                empat()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)

        d = input('Ring  4 : ').upper()
        if d == "BROWN":
            d = 0.01
        elif d == "RED":
            d = 0.02
        elif d == "GREEN":
            d = 0.005
        elif d == "BLUE":
            d = 0.0025
        elif d == "PURPLE":
            d = 0.001
        elif d == "GOLD":
            d = 0.05
        elif d == "SILVER":
            d = 0.1
        else:
            print ("\nResistance Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                empat()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)
        
        def jaw():  
            jadi = input('\nColor You Entered Is Correct ? Y/N ? ').upper()
            if jadi == "Y":
                jawab = int(b) * c
                print ("\nR = %s * %s  %s" % (b,c,d))
                print ("R = " + str(jawab) + " Ohm" + " +/-" + " %s" % (d))
                print ("")
                rmax = jawab + (d * jawab)
                con1 = int(rmax)
                print ("Rmax = " + str(jawab) + " +" + " (%s * %s)" % (d,jawab))
                print ("Rmax = " + str(con1))
                rmin = jawab - (d * jawab)
                con2 = int(rmin)
                print ("\nRmin = " + str(jawab) + " -" + " (%s * %s)" % (d,jawab))
                print ("Rmin = " + str(con2))
                print ("")
                sys.exit(1)
            elif jadi == "N":
                empat()
            else:
                jaw()

        jaw()
    a()

def lima():
    def a():
        os.system('clear')
        print ("""
                                    =========================
                                  == ))  ))  ))  ))    ) )   ==
                      ============   ))  ))  ))  ))    ) )    ============
                                  == ))  ))  ))  ))    ) )   ==
                                    =========================

                            <<<<  v-Resis : Count The Resistor  >>>>
                            <<<<            5 Ring            >>>>
        """)
        print ("""
|======(Ring 1 , 2 , 3)======|==============(Ring 4)==============|===========(Ring 5)===========|
|> BLACK  = 0   > GREEN  = 5 |> BLACK  = 10**0   > GREEN  = 10**5 |> BROWN = 1%    > SILVER = 10%|
|> BROWN  = 1   > BLUE   = 6 |> BROWN  = 10**1   > BLUE   = 10**6 |> RED   = 2%                  |
|> RED    = 2   > PURPLE = 7 |> RED    = 10**2   > PURPLE = 10**7 |> GREEN = 0.5%                |
|> ORANGE = 3   > GRAY   = 8 |> ORANGE = 10**3   > GRAY   = 10**8 |> BLUE  = 0.10%               |
|> YELLOW = 4   > WHITE  = 9 |> YELLOW = 10**4   > WHITE  = 10**9 |> GOLD  = 5%                  |
==================================================================================================
    """)
        print ("Please Enter Ring's Color ")
        a = input('\nRing  1 : ').upper()
        if a == "BLACK":
            a = 0
        elif a == "BROWN":
            a = 1
        elif a == "RED":
            a = 2
        elif a == "ORANGE":
            a = 3
        elif a == "YELLOW":
            a = 4
        elif a == "GREEN":
            a = 5
        elif a == "BLUE":
            a = 6
        elif a == "PURPLE":
            a = 7
        elif a == "GRAY":
            a = 8
        elif a == "WHITE":
            a = 9
        else:
            print ("\nRing Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                empat()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)

        b = input('Ring  2 : ').upper()
        if b == "BLACK":
            b = str(a) + str(0)
        elif b == "BROWN":
            b = str(a) + str(1)
        elif b == "RED":
            b = str(a) + str(2)
        elif b == "ORANGE":
            b = str(a) + str(3)
        elif b == "YELLOW":
            b = str(a) + str(4)
        elif b == "GREEN":
            b = str(a) + str(5)
        elif b == "BLUE":
            b = str(a) + str(6)
        elif b == "PURPLE":
            b = str(a) + str(7)
        elif b == "GRAY":
            b = str(a) + str(8)
        elif b == "WHITE":
            b = str(a) + str(9)
        else:
            print ("\nRing Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                lima()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)
                
        ba = input('Ring  3 : ').upper()
        if ba == "BLACK":
            ba = str(a) + str(0) + str(0)
        elif ba == "BROWN":
            ba = str(a) + str(1) + str(1)
        elif ba == "RED":
            ba = str(a) + str(2) + str(2)
        elif ba == "ORANGE":
            ba = str(a) + str(3) + str(3)
        elif ba == "YELLOW":
            ba = str(a) + str(4) + str(4)
        elif ba == "GREEN":
            ba = str(a) + str(5) + str(5)
        elif ba == "BLUE":
            ba = str(a) + str(6) + str(6)
        elif ba == "PURPLE":
            ba = str(a) + str(7) + str(7)
        elif ba == "GRAY":
            ba = str(a) + str(8) + str(8)
        elif ba == "WHITE":
            ba = str(a) + str(9) + str(9)
        else:
            print ("\nRing Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                lima()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)

        c = input('Ring  4 : ').upper()
        if c == "BLACK":
            c = 10**0
        elif c == "BROWN":
            c = 10**1
        elif c == "RED":
            c = 10**2
        elif c == "ORANGE":
            c = 10**3
        elif c == "YELLOW":
            c = 10**4
        elif c == "GREEN":
            c = 10**5
        elif c == "BLUE":
            c = 10**6
        elif c == "PURPLE":
            c = 10**7
        elif c == "GRAY":
            c = 10**8
        elif c == "WHITE":
            c = 10**9
        else:
            print ("\nMultiplier Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                lima()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)

        d = input('Ring  5 : ').upper()
        if d == "BROWN":
            d = 0.01
        elif d == "RED":
            d = 0.02
        elif d == "GREEN":
            d = 0.005
        elif d == "BLUE":
            d = 0.0025
        elif d == "PURPLE":
            d = 0.001
        elif d == "GOLD":
            d = 0.05
        elif d == "SILVER":
            d = 0.1
        else:
            print ("\nResistance Color Not Found")
            l = input('\nTry Again ? Y/N ? ').upper()
            if l == "Y":
                lima()
            elif l == "N":
                print ("\nBye Bye :)")
                sys.exit(1)
            else:
                print ('\nWrong Input')
                sys.exit(1)
        
        def jaw():  
            jadi = input('\nColor You Entered Is Correct ? Y/N ? ').upper()
            if jadi == "Y":
                jawab = int(ba) * c
                print ("\nR = %s * %s (%s)" % (b,c,d))
                print ("R = " + str(jawab) + " Ohm" + " +/-" + " %s" % (d))
                print ("")
                rmax = jawab + (d * jawab)
                con1 = int(rmax)
                print ("Rmax = " + str(jawab) + " +" + " (%s * %s)" % (d,jawab))
                print ("Rmax = " + str(con1))
                rmin = jawab - (d * jawab)
                con2 = int(rmin)
                print ("\nRmin = " + str(jawab) + " -" + " (%s * %s)" % (d,jawab))
                print ("Rmin = " + str(con2))
                print ("")
                sys.exit(1)
            elif jadi == "N":
                lima()
            else:
                jaw()

        jaw()
    a()
    
logo()
men()
