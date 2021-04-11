import os
from colored import fg, bg, attr


##predefined colours.
redcolour=fg('red_3a')
reset = attr("reset")
whitecolour=fg('white')
greencolour=fg('spring_green_2b')
bluecolour=fg('deep_sky_blue_1')
blackcolour=fg('grey_0')
purplecolour=fg('purple_1a')

## the nuke banner function and display___________________________________________________________________________________
##000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def banner():
 os.system("clear")
 print(blackcolour+dots)
 print(greencolour+"""
HACKERS   OUR  WE    US   OUR   US    SECURITY
YOU YOU   YOU  US    WE   YOU  YOU    WAS
OUR OUR   OUR  WE    US   EXPLOIT     ILLUTION
YOU YOU   YOU  US    WE   YOU DATA    SECURITY
OUR  OUR FATE  WE    US   OUR  INFO   IS
YOU  EXPLOITS  PAYLOADS   YOU  DATA   ILLUTION
""")
 print(blackcolour+dots)
 print(whitecolour+"boredom and lazyness is the mother of scripts")
 print(whitecolour+"type the keyword of the phase/tool to navigate")
 print(whitecolour+"CTRL+C to exit")
 print(blackcolour+dots)
 print(bluecolour+("target url   : "+url))
 print(bluecolour+("target domain: "+target_url))
 print(bluecolour+("target ip    : "+target_ip))
 print(blackcolour+dots+whitecolour)

##into list.this is where it begins_______________________________________________________________________________________
##000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def intro():
 banner()
 print("tools required        : tool")
 print("information gathering : info")
 print("vulnerability analysis: vuln")
 print("exploitation          : exploit")
 print("denial of service(dos): dos")
 print(blackcolour+dots+whitecolour)
 user_input_phase = input(purplecolour+"keyword here: ")

 if user_input_phase == "info":
     info()

 elif user_input_phase == "tool":
         tool()

 elif user_input_phase == "vuln":
              vuln()

 elif user_input_phase == "dos":
                  dos_list()

 elif user_input_phase == "exploit":
                      exploit()

 else:
     print(redcolour+"that is not a keyword!")
     input("press enter: ")
     intro()

##the tool section of intro that lists the tools used___________________________________________________________________
##11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def tool():
      banner()
      print("nmap(network mapper)")
      print("ldb(load balancing detector)")
      print("dnsenum")
      print("dnsrecon")
      print("fierce")
      print("nikto")
      print("skipfish")
      print("whatweb")
      print("joomscan")
      print("wpscan")
      print("metasploit framework")
      print("slowhttptest")
      print("dirb")
      print("gobuster")
      print("seclists(for wordlists)")
      print(blackcolour+dots+whitecolour)
      input(greencolour+"press enter to return to the main menu: ")
      intro()

##the information gathering phase list___________________________________________________________________________________
##111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def info():
  banner()
  print("nmap(network mapper)        : nmap")
  print("directory finder tools      : dird")
  print("lbd(load balancing detector): lbd")
  print("domain recon tools          : dom")
  print("#enter 99 to go back: 99")
  print(blackcolour+dots+whitecolour)
  user_input_info = input(purplecolour+"keyword here: ")

  if user_input_info == "nmap":
      nmap_list()

  elif user_input_info == "dird":
          dird_list()

  elif user_input_info == "lbd":
              lbd()

  elif user_input_info == "dom":
                  dom_list()

  elif user_input_info == "99":
                      intro()

  else:
      print(redcolour+"that is not a keyword!")
      input("press enter: ")
      info()

##the nmap sublist________________________________________________________________________________________________________
##222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

def nmap_list():
   banner()
   print("nmap is a multipurpose scanner.")
   print(blackcolour+dots+whitecolour)
   print("nmap default scan       : default")
   print("nmap speed scan         : speed")
   print("nmap aggresive scan     : aggresive")
   print("nmap tcp port scan      : tcp")
   print("nmap udp port scan      : udp")
   print("nmap scripting engine   : nse")
   print("#enter 99 to go back    : 99")
   print(blackcolour+dots+whitecolour)
   user_input_nmap = input(purplecolour+"keyword here: ")

   if user_input_nmap == "speed":
       banner()
       speed = input("enter the speed (1-5): ")
       print(greencolour+"nmap scan initiated")
       os.system("sudo nmap -vv -T"+speed+" "+target_ip)
       input(purplecolour+"press enter: ")
       intro()

   elif user_input_nmap == "default":
           banner()
           print(greencolour+"nmap scan initiated")
           os.system('sudo nmap -vv '+target_ip)
           input(whitecolour+"press enter: ")
           nmap_list()

   elif user_input_nmap == "aggresive":
               banner()
               print(greencolour+"nmap scan initiated")
               os.system("sudo nmap -vv -A "+target_ip)
               input(whitecolour+"press enter: ")
               intro()

   elif user_input_nmap == "nse":
                   nmap_nse()

   elif user_input_nmap == "tcp":
                       banner()
                       print(greencolour+"nmap scan initiated")
                       os.system("nmap -vv -sT "+target_ip)
                       input(whitecolour+"press enter: ")

   elif user_input_nmap == "udp":
                           banner()
                           print(greencolour+"nmap scan initiated")
                           os.system("nmap -vv -sU "+target_ip)
                           input(whitecolour+"press enter: ")

   elif user_input_nmap == "99":
                               info()

   else:
       print(redcolour+"that is not a keyword!")
       input("press enter: ")

##the nse of nmap of info phase______________________________________________________________________________________
##3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

def nmap_nse():
    banner()
    print("default script scan                 : default")
    print("vuln script scan(takes time)        : vuln")
    print("info script scan                    : info")
    print("all script scan(takes a lot of time): all")
    print("enter 99 to go back                 : 99")
    print(blackcolour+dots+whitecolour)
    user_input_nmap_script = input(purplecolour+"keyword here: ")

    if user_input_nmap_script == "default":
        banner()
        print(greencolour+"nmap scan initiated")
        os.system("sudo nmap -vv -sC "+target_ip)
        input(whitecolour+"press enter: ")
        intro()

    elif user_input_nmap_script == "vuln":
            banner()
            print(greencolour+"nmap scan initiated")
            os.system("sudo nmap -vv --script=vuln "+target_ip)
            input(whitecolour+"press enter: ")
            intro()

    elif user_input_nmap_script == "info":
                print("the script is too long and may outflow your terminal.")
                o_dir = str(input("enter the exact output file path: "))
                banner()
                print(greencolour+"nmap scan initiated")
                os.system("sudo nmap -vv --script=discovery "+target_ip+" -o "+o_dir)
                input(whitecolour+"press enter: ")
                intro()

    elif user_input_nmap_script == "all":
                    banner()
                    print(greencolour+"nmap scan initiated")
                    os.system("sudo nmap -vv --script=all "+target_ip)
                    input(whitecolour+"press enter: ")
                    intro()

    elif user_input_nmap_script == "99":
                        nmap_list()

    else:
        print(redcolour+"that is not a keyword!")
        input("press enter: ")
        nmap_nse()

##lhd tool__________________________________________________________________________________________________________
##222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

def lbd():
    banner()
    print("lbd is load balancing detector")
    print("it takes a lot of time...")
    print("be patient, or cancel it.")
    print(blackcolour+dots+greencolour)
    os.system("lbd "+target_ip)
    input(whitecolour+"press enter: ")
    intro()

##dns tool listing__________________________________________________________________________________________________
##222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

def dom_list():
    banner()
    print("these tools provide info about domains")
    print(blackcolour+dots+whitecolour)
    print("dnsenum           : enum")
    print("dnsrecon          : recon")
    print("fierce            : fierce")
    print("dmitry            : dmitry")
    print("type 99 to go back: 99")
    print(blackcolour+dots+whitecolour)
    user_input_dns_list = input(purplecolour+"keyword here: ")

    if user_input_dns_list == "enum":
        banner()
        print(greencolour+"initiating dnsenum")
        os.system("dnsenum "+target_url)
        input(whitecolour+"press enter: ")
        dom_list()

    elif user_input_dns_list == "recon":
        banner()
        print(greencolour+"initiating dnsrecon")
        os.system("dnsrecon -d "+target_url)
        input(whitecolour+"press enter: ")
        dom_list()

    elif user_input_dns_list == "fierce":
        banner()
        print(greencolour+"initiating fierce")
        os.system("fierce --domain "+target_url)
        input(whitecolour+"press enter: ")
        dom_list()

    elif user_input_dns_list == "dmitry":
        banner()
        base_command = "dmitry "
        oh_no = input(purplecolour+"perform a whois lookup on the ip address of the host?: ")
        if oh_no == "yes":
            base_command = base_command+"-i "

        ohh_no = input("perform a whois lookup on the domain name of host?: ")
        if ohh_no == "yes":
            base_command = base_command+"-w "

        ohh_no_no = input("retrieve netcraft info on host?: ")
        if ohh_no_no == "yes":
            base_command = base_command+"-n "

        no_no_no_no = input("perform a search for subdomains?: ")
        if no_no_no_no == "yes":
            base_command = base_command+"-s "
       
        no_no = input("perform a search for email addresses?: "+greencolour)
        if no_no == "yes":
            base_comman = base_command+"-e "
     
        base_command = base_command+target_url
        os.system(base_command)
        input(whitecolour+"press enter: ")
        dom_list()
    
    elif user_input_dns_list == "99":
        info()

    else:
        print(redcolour+"that is not a keyword!")
        input("press enter: ")
        dom_list()

##vulnerability analysis phase______________________________________________________________________________________
##111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def vuln():
  banner()
  print("nikto scan         : nikto")
  print("nmap vuln script   : nmap")
  print("skipfish           : skip")
  print("whatweb            : what")
  print("joomscan           : joom")
  print("wpscan             : word")
  print("type 99 to go back : 99")
  print(blackcolour+dots+whitecolour)
  user_input_vuln = input(purplecolour+"keyword here: ")

  if user_input_vuln == "nikto":
      nikto()

  elif user_input_vuln == "nmap":
      nmap_nse()

  elif user_input_vuln == "skip":
      banner()
      o_dir = input("enter output directory: ")
      o_dir = str(o_dir)
      print(greencolour+"initiating skipfish")
      os.system("skipfish -o "+o_dir+" -u "+url)
      input(whitecolour+"press enter: ")
      banner()
      vuln()

  elif user_input_vuln == "what":
      banner()
      print(greencolour+"initiating whatweb")
      os.system("whatweb " +target_ip)
      input(whitecolour+"press enter: ")
      vuln()

  elif user_input_vuln == "joom":
      banner()
      print(greencolour+"initialising joomscan")
      os.system("sudo joomscan -u "+target_url)
      input(whitecolour+"press enter: ")
      vuln()

  elif user_input_vuln == "word":
      banner()
      print(greencolour+"initialising wordpress scan")
      os.system("wpscan --url "+url)
      input(whitcolour+"press enter: ")
      vuln()

  elif user_input_vuln == "99":
      intro()

  else:
      print(redcolour+"the input was not recognised as a keyword!")
      input("press enter: ")
      vuln()

def nikto():
    banner()
    y_n = input("do you want output to a file?: ")
    y_n = str(y_n)

    if y_n == "no":
        banner()
        print(greencolour+"initialising nikto")
        os.system("nikto -host "+target_ip)
        input(whitecolour+"press enter: ")
        vuln()

    elif y_n == "yes":
        banner()
        o_file = input("enter the exact path for output file: ")
        banner()
        print(greencolour+"initialising nikto")
        os.system("nikto -host "+target_ip+" -output "+o_file)
        input(whitecolour+"press enter: ")
        vuln()

    else:
        print(redcolour+"pls enter yes or no!")
        input("press enter: ")
        nikto()

##the exploit phase_________________________________________________________________________________________________
##111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def exploit():
    banner()
    print("msfconsole         : msf ")
    print("enter 99 to go back: 99")
    print(blackcolour+dots+whitecolour)
    user_input_exploit = input("keyword here: ")

    if user_input_exploit == "msf":
        banner()
        print(greencolour+"imma honoured to start metasploit framework :)")
        print("this may take time")
        os.system("sudo msfconsole")
        input(whitecolour+"press enter: ")
        exploit()

    elif user_input_exploit == "99":
        intro()

    else:
        print(redcolour+"that was not recognized as a keyword!")
        input("press enter: ")
        exploit()

##the dos attack menu_______________________________________________________________________________________________
##111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def dos_list():
    banner()
    print(disclaimer)
    print("."*50)
    input(whitecolour+"read the above and press enter")
    banner()
    connections = input(purplecolour+"enter the target number of connections: ")
    data_seconds = input("interval between followup data in seconds: ")
    time = input("target test length in seconds: ")
    rate = input("connections per second: ")
    ssl_port = input("ssl port of the target: ")
    banner()
    print("Slowloris attack(slow headers)     : slowloris")
    print("R-U-Dead-Yet attack(slow body)     : rudy")
    print("Apache killer attack(range attack) : apache")
    print("Slow read attack                   : slowread")
    print("thc-ssl-dos attack                 : thcl")
    print("#type 99 to exit                   : 99")
    print("."*50)
    user_input_dos = input(purplecolour+"keyword here: ")

    if user_input_dos == "slowloris":
        banner()
        print(greencolour+"initialising the attack")
        os.system("slowhttptest -H -c "+connections+" -i "+data_seconds+" -l "+time+" -r "+rate+" -u "+url)
        input(whitecolour+"press enter: ")
        intro()

    elif user_input_dos == "rudy":
        banner()
        print(greencolour+"initialising the attack")
        os.system("slowhttptest -B -c "+connections+" -i "+data_seconds+" -l "+time+" -r "+rate+" -u "+url)
        input(whitecolour+"press enter: ")
        intro()

    elif user_input_dos == "apache":    
        banner()
        print(greencolour+"initialising the attack")
        os.system("slowhttptest -R -c "+connections+" -i "+data_seconds+" -l "+time+" -r "+rate+" -u "+url)
        input(whitecolour+"press enter: ")
        intro()

    elif user_input_dos == "slowread":
        banner()
        print(greencolour+"initialising the attack")
        os.system("slowhttptest -X -c "+connections+" -i "+data_seconds+" -l "+time+" -r "+rate+" -u "+url)
        input(whitecolour+"press enter: ")
        intro()

    elif user_input_dos == "thcl":
        banner()
        print(greencolour+"initialising the attack")
        os.system("thc-ssl-dos "+target_ip+" "+ssl_port+" --accept")
        input(whitecolour+"press enter: ")
        intro()

    elif user_input_dos == "99":
        intro()

    else:
        print(redcolour+"that is not a keyword!")
        input("press enter: ")
        intro()

##the dird menu_____________________________________________________________________________________________________
##222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

def dird_list():
   banner()
   print("dirb               : dirb")
   print("gobuster           : gobu")
   print("enter 99 to go back: 99")
   print("."*50)
   user_input_dird = input(purplecolour+"keyword here: ")
   if user_input_dird == "dirb":
       banner()
       yes_no = input("do you have a wordlist for web-content discovery?: ")

       if yes_no == "yes":
           wordlist = input("enter the absolute location of wordlist file: ")
           banner()
           print(greencolour+"initialising dirb")
           os.system("dirb "+url+" "+wordlist)
           input(whitecolour+"press enter: ")
           dird_list()

       elif yes_no == "no": 
           banner()
           print("dirb will use the default wordlist for u")
           print(greencolour+"initialising dirb")
           os.system("dirb "+url)
           input(whitecolour+"press enter: ")
           dird_list()

       else:
           print(redcolour+"next time, enter yes or no")
           input("press enter: ")
           dird_list()

   elif user_input_dird == "gobu":
       gobuster()

   elif user_input_dird == "99":
       info()

   else:
       print(redcolour+"that is not a keyword")
       input("press enter: ")
       dird_list()

def gobuster():
   banner()
   y_n = input(purplecolour+"do you have a wordlist with you?: ")

   if y_n == "no":
       banner()
       print("select a wordlist")
       print(blackcolour+dots+whitecolour)
       print("common                     : comm")
       print("big                        : big")
       print("medium (personal favourite): med")
       print("small                      : small")
       print("enter 99 to go back        : 99")
       print(blackcolour+dot+whitecolour)
       wordlist = input(purplecolour+"keyword here: ")
       if wordlist == "comm":
           banner()
           print(greencolour+"initialising gobuster")
           os.system("gobuster dir -u "+url+" -w /usr/share/seclists/Discovery/Web-Content/common.txt")
           input(whitecolour+"press enter: ")
           info()

       elif wordlist == "big":
           banner()
           print(greencolour+"initialising gobuster")
           os.system("gobuster dir -u "+url+" -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt")
           input(whitecolour+"press enter: ")
           info()

       elif wordlist == "med":
           banner()
           print(greencolour+"initialising gobuster")
           os.system("gobuster dir -u "+url+" -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt")
           input(whitecolour+"press enter: ")
           info()

       elif wordlist == "small":
           banner()
           print(greencolour+"initialising gobuster")
           os.system("gobuster dir -u "+url+" -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt")
           input(whitecolour+"press enter: ")
           info()

       elif wordlist == "99":
           info()

       else:
           print(redcolour+"that is not a keyword")
           input("press enter")
           dird_list()

   elif y_n == "yes":
       banner()
       wordlist = input(purplecolour+"enter the absolute locaton of the wordlist: ")
       banner()
       print(greencolour+"initialising gobuster")
       os.system("gobuster dir -w "+wordlist+" -u "+url)
       input(whitecolour+"press enter: ")
       info()

   elif y_n == "99":
       info()

   else:
       print(redcolour+"that is not a keyword")
       input("press enter")
       gobuster()


##the loop initiator_________________________________________________________________________________________________
##*******************************************************************************************************************

##garbage value initialisation
dots = "."*50
url = "N.A"
target_url = "N.A"
target_ip  = "N.A"
disclaimer = str("""dear user, this program is designed for automation and organisation of penetration testing tasks. as u may already know, "with great power, comes great responsibility. my program is open source and i do not claim any responsibily of the consequences caused by this program""")

##the original loop initiator
banner()
print(whitecolour+"pls have an active internet connection"+bluecolour)
url = input(whitecolour+"enter the absolute url of target: "+bluecolour)
target_url = input(whitecolour+"enter the target domain: "+bluecolour)
print(greencolour+"diging and pinging domain")
target_ip_guess = os.system("dig " + target_url + " | grep A && ping -c 1 "+target_url)
print(target_ip_guess)
target_ip = input(whitecolour+"enter target ip: "+bluecolour)
targer_ip = str(target_ip)
intro()
##******************************************************************************************************************

