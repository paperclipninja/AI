#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arianna
#
# Created:     12/09/2013
# Copyright:   (c) Arianna 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    for n in range (1,51):
        print("%3d"%n, end=" ")
        print("%3d"%(n*n), end=" ")
        print("%9.3f"%(n**(1/2)),end="")
        print("%9.3f"%(n**(1/3)), end="   ")
        #gets to here fine
        print("%3d"%(n+50), end=" ")
        print("%3d"%((n+50)**2),end=" ")
        print("%9.3f"%((n+50)**(1/2)),end=" ")
        print("%9.3f"%((n+50)**(1/3)))
        print("\n")
if __name__ == '__main__':
    main()
