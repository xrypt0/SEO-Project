#SEO Project

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

#This Code Belgons to Xrypt0

url = "https://pagespeed.web.dev/report?url="
first_url = input("First :")
second_url = input("Second :")

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(executable_path = "chromedriver.exe", options = option)

#driver.get(url+first_url)

driver.get(url+first_url)

time.sleep(3)

LCP1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/span/span').text
FID1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/span/span').text
CLS1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/span/span').text
FCP1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div[2]/div[1]/span/span').text
INP1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[7]/div[2]/div[1]/span/span').text
TTFB1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[8]/div[2]/div[1]/span/span').text
#performance1 = driver.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[3]/div[2]/div/div/article/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/a/div[2]').text

"""
if LCP1 or FID1 or CLS1 or FCP1 or INP1 or TTB1 == '':
	print("Unfortunately, the URL you entered is problematic. Please check at https://pagespeed.web.dev/")
	time.sleep(7)
	exit()
"""
LCP1_length = len(LCP1) - 4
LCP1 = LCP1.replace(",",".")
LCP1 = float(LCP1[0:LCP1_length])

FID1_length = len(FID1) - 4
FID1 = int(FID1[0:FID1_length])

CLS1 = CLS1.replace(",",".")
CLS1 = float(CLS1)

FCP1_length = len(FCP1) - 4
FCP1 = FCP1.replace(",",".")
FCP1 = float(FCP1[0:FCP1_length])

INP1_length = len(INP1) - 4
INP1 = int(INP1[0:INP1_length])

TTFB1_length = len(TTFB1) - 4
TTFB1 = TTFB1.replace(",",".")
TTFB1 = float(TTFB1[0:TTFB1_length])


"""
print(LCP1)
print("\n")
print(FID1)
print("\n")
print(CLS1)
print("\n")
print(FCP1)
print("\n")
print(INP1)
print("\n")
print(TTFB1)
driver.close()
"""

driver1 = webdriver.Chrome(executable_path = "chromedriver.exe", options = option)

driver1.get(url+second_url)

time.sleep(4)

LCP2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/span/span').text
FID2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/span/span').text
CLS2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/span/span').text
FCP2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div[2]/div[1]/span/span').text
INP2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[7]/div[2]/div[1]/span/span').text
TTFB2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[8]/div[2]/div[1]/span/span').text
#performance2 = driver1.find_element_by_xpath('/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[3]/div[2]/div/div/article/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/a/div[2]').text

LCP2_length = len(LCP2) - 4
LCP2 = LCP2.replace(",",".")
LCP2 = float(LCP2[0:LCP2_length])

FID2_length = len(FID2) - 4
FID2 = int(FID2[0:FID2_length])

CLS2 = CLS2.replace(",",".")
CLS2 = float(CLS2)

FCP2_length = len(FCP2) - 4
FCP2 = FCP2.replace(",",".")
FCP2 = float(FCP2[0:FCP2_length])

INP2_length = len(INP2) - 4
INP2 = int(INP2[0:INP2_length])

TTFB2_length = len(TTFB2) - 4
TTFB2 = TTFB2.replace(",",".")
TTFB2 = float(TTFB2[0:TTFB2_length])

variable_1 = " "
variable_2 = " "
variable_3 = " "
variable_4 = " "
variable_5 = " "
variable_6 = " "
variable_7 = " "

if LCP1 > LCP2:
	variable_1 = "<"
elif LCP2 > LCP1:
	variable_1 = ">"
elif LCP2 == LCP1:
	variable_1 = "="
else:
	variable_1 = "ERROR"

if FID1 > FID2:
	variable_2 = "<"
elif FID2 > FID1:
	variable_2 = ">"
elif FID2 == FID1:
	variable_2 = "="
else:
	variable_2 = "ERROR"

if CLS1 > CLS2:
	variable_3 = "<"
elif CLS2 > CLS1:
	variable_3 = ">"
elif CLS2 == CLS1:
	variable_3 = "="
else:
	variable_3 = "ERROR"

if FCP1 > FCP2:
	variable_4 = "<"
elif FCP2 > FCP1:
	variable_4 = ">"
elif FCP2 == FCP1:
	variable_4 = "="
else:
	variable_4 = "ERROR"

if INP1 > INP2:
	variable_5 = "<"
elif INP2 > INP1:
	variable_5 = ">"
elif INP2 == INP1:
	variable_5 = "="
else:
	variable_5 = "ERROR"

if TTFB1 > TTFB2:
	variable_6 = "<"
elif TTFB2 > TTFB1:
	variable_6 = ">"
elif TTFB2 == TTFB1:
	variable_6 = "="
else:
	variable_6 = "ERROR"
"""
if performance2 > performance1:
	variable_7 = "<"
elif performance1 > performance2:
	variable_7 = ">"
elif performance1 == performance2:
	variable_7 = "="
else:
	variable_7 = "ERROR"
"""


date = datetime.datetime.now()
report = open("report.txt","w")
report.write(""" DATE : """+str(date)+"""

	LCP =  FIRST""" + variable_1 + "SECOND = LCP("+str(LCP1)+ "--" +str(LCP2)+""")

	FID = FIRST""" + variable_2 + "SECOND = FID("+str(FID1)+ "--" +str(FID2)+""")

	CLS =  FIRST""" + variable_3 + "SECOND = CLS("+str(CLS1)+ "--" +str(CLS2)+""")
	
	FCP = FIRST""" + variable_4 + "SECOND = FCP("+str(FCP1)+ "--" +str(FCP2)+""")

	INP =  FIRST""" + variable_5 + "SECOND = INP("+str(INP1)+ "--" +str(INP2)+""")

	TTFB = FIRST""" + variable_6 + "SECOND = TTFB("+str(TTFB1)+ "--" +str(TTFB2)+""")
	


	\n
	\n
	\n
	\n
	\n
	""")

print("\nCongratulations ! Your Page Speed data is saved in a .txt file located in the program's location.")


"""
print(LCP2)
print("\n")
print(FID2)
print("\n")
print(CLS2)
print("\n")
print(FCP2)
print("\n")
print(INP2)
print("\n")
print(TTFB2)
print("\n")
"""
#Xrypt0
