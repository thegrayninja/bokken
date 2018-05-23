import sys


def main():
    Help()
    Subnets()
    SmartIPRange()

def Help():
    if len(sys.argv) == 1:
        print("""
                                                    BOOM SHOCKA LOCKA

                            O_o  


        You done messed up. Try this next time:
            python ipsubnet_explode.py 192.168.0.15/28
        
        """)
        sys.exit(1)

def Subnets():
    print("""
    
                            O_o
    
    _______________________________________________
    Mask | TotalIP |  Formula   |  Total Usable IPs
    -----------------------------------------------
    32  =  1 IP    =   2**0     =  1 Usable IP
    31  =  2 IPs   =  (2**1)-2  =  0 Usable IPs
    30  =  4 IPs   =  (2**2)-2  =  2 Usable IPs
    29  =  8 IPs   =  (2**3)-2  =  6 Usable IPs
    28  =  16 IPs  =  (2**4)-2  =  14 Usable IPs
    27  =  32 IPs  =  (2**5)-2  =  30 Usable IPs
    26  =  64 IPs  =  (2**6)-2  =  62 Usable IPs
    25  =  128 IPs =  (2**7)-2  =  126 Usable IPs
    24  =  256 IPs =  (2**8)-2  =  254 Usable IPs

    """)


def SmartIPRange():
    FullIP = sys.argv[1]
    #print(FullIP)
    SplitFullIP = FullIP.split("/")
    SubnetMaskNo = SplitFullIP[1]
    IntSubnetMask = int(SubnetMaskNo)
    IPAddress = SplitFullIP[0]
    PrefixSplit = IPAddress.split(".")
    Prefix = "{}.{}.{}.".format(PrefixSplit[0], PrefixSplit[1], PrefixSplit[2])

    SubnetRange = 2**(32 - IntSubnetMask)
    SubnetMaskEnd = 256-SubnetRange


    if IntSubnetMask > 23:
        LastOctet = PrefixSplit[3]

        FoundNetworkIP = "no"
        LowerNumber = 0
        UpperNumber = SubnetRange
        while FoundNetworkIP == "no":
            for i in range(LowerNumber, UpperNumber):
                #print(i)
                if int(LastOctet) == i:
                    #IPNetworkNumber = Prefix + str(LowerNumber)
                    FoundNetworkIP = "yes"
                    break
            else:
                LowerNumber += SubnetRange
                UpperNumber += SubnetRange
                if i >=256:
                    FoundNetworkIP = "yes"

        print("IP Address = {}".format(IPAddress))
        print("SubnetMask = 255.255.255.{}".format(str(SubnetMaskEnd)))
        print("Network IP = {}{}".format(Prefix, str(LowerNumber)))
        print("Broadcast IP = {}{}".format(Prefix, str(UpperNumber)))
        print("Usable IPs = {}".format(SubnetRange - 2))


    elif IntSubnetMask < 24 and IntSubnetMask > 15:
        SubnetRange = 2**(32-(IntSubnetMask + 8))
        SubnetMaskEnd = 256-SubnetRange
        LastOctet = PrefixSplit[2]

        FoundNetworkIP = "no"
        LowerNumber = 0
        UpperNumber = SubnetRange
        while FoundNetworkIP == "no":
            for i in range(LowerNumber, UpperNumber):
                #print(i)
                if int(LastOctet) == i:
                    #IPNetworkNumber = Prefix + str(LowerNumber)
                    FoundNetworkIP = "yes"
                    break
            else:
                LowerNumber += SubnetRange
                UpperNumber += SubnetRange
                if i >=256:
                    FoundNetworkIP = "yes"

        print("IP Address = {}".format(IPAddress))
        print("SubnetMask = 255.255.{}.0".format(str(SubnetMaskEnd)))
        print("Network IP = {}.{}.{}.0".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber)))
        print("Broadcast IP = {}.{}.{}.255".format(PrefixSplit[0], PrefixSplit[1], str(UpperNumber-1)))
        print("Minimum IP = {}.{}.{}.1".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber)))
        print("Maximum IP = {}.{}.{}.254".format(PrefixSplit[0], PrefixSplit[1], str(UpperNumber-1)))
        print("Usable IPs = {}".format(2 ** (32 - (IntSubnetMask)) - 2))



    elif IntSubnetMask < 16 and IntSubnetMask > 7:
        SubnetRange = 2**(32-(IntSubnetMask + 16))
        SubnetMaskEnd = 256-SubnetRange
        LastOctet = PrefixSplit[1]

        FoundNetworkIP = "no"
        LowerNumber = 0
        UpperNumber = SubnetRange
        while FoundNetworkIP == "no":
            for i in range(LowerNumber, UpperNumber):
                #print(i)
                if int(LastOctet) == i:
                    #IPNetworkNumber = Prefix + str(LowerNumber)
                    FoundNetworkIP = "yes"
                    break
            else:
                LowerNumber += SubnetRange
                UpperNumber += SubnetRange
                if i >=256:
                    FoundNetworkIP = "yes"

        print("IP Address = {}".format(IPAddress))
        print("SubnetMask = 255.{}.0.0".format(str(SubnetMaskEnd)))
        print("Network IP = {}.{}.0.0".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber)))
        print("Broadcast IP = {}.{}.255.255".format(PrefixSplit[0], str(UpperNumber-1)))
        print("Minimum IP = {}.{}.0.1".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber)))
        print("Maximum IP = {}.{}.255.254".format(PrefixSplit[0], str(UpperNumber-1)))
        print("Usable IPs = {}".format(2 ** (32 - (IntSubnetMask)) - 2))

    else:
        print("work in progresso")



if __name__ == main():
    main()