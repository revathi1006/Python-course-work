import atm
atm.Welcome()


def Flow_Check(ch):
    if ch=='C':
        Check_Balance()
    elif ch=='D':
        Deposit()
    elif ch=='W':
        Withdraw()
    elif ch=='V':
        View_History()
    elif ch=='V':
        print( "  THANK YOU " . center(40,'*'))
    else:
        print(" INVALID CHOICE ")
    
atm.Menu()