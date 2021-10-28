
from os import isatty
from typing import runtime_checkable
from selenium import webdriver
import time
import argparse
from datetime import datetime
import AppKit
import time
from selenium.webdriver.support.ui import Select

number = 15
round = 1
isRun = True
priority_list0 = ["Edison"]
priority_list1 = ["Edison", "Bakers Basin", "South Plainfield"]
priority_list2 = ["Rahway", "Freehold", "Newark",
                  "Bayonne", "Eatontown", "Toms River", "North Bergen", "Wayne", "Paterson", "Randolph"]
except_date_text = ["Next Available: 09/13",
                    "Next Available: 09/14", "Next Available: 09/16", "Next Available: 09/17", "Next Available: 10", "Next Available: 11"]

expect_date_text = ["Next Available: 09/18",
                    "Next Available: 09/19", "Next Available: 09/25", "Next Available: 09/26"]

priority_list = priority_list0

# driver & appointment info
personal_info_0 = {'firstName': 'Yijie',
                   'lastName': 'Xu', 'phone': '(609) 356-9060', 'email': 'yijiex@princeton.edu', 'birthDate': "10/21/1998", 'driverLicense': "000000000"}
personal_info_1 = {'firstName': 'Sicheng',
                   'lastName': 'Yin', 'phone': '(753) 697-3514', 'email': 'yinsicheng1999@outlook.com', 'birthDate': '01/19/1999'}
personal_info_2 = {'firstName': 'Dazhao',
                   'lastName': 'Yin', 'phone': '(626) 716-3579', 'email': 'evenqaq@outlook.com', 'birthDate': '06/20/1974'}
personal_info_3 = {'firstName': 'Wenmei',
                   'lastName': 'Wu', 'phone': '(609) 718-9911', 'email': 'even_sc@163.com', 'birthDate': '07/08/1972'}
# permitType = 'Class D'

parser = argparse.ArgumentParser(description='Please choose applicant')
parser.add_argument('-N', '--NO', type=int, default=0)
args = parser.parse_args()
print(args)
personal_info = personal_info_0
applicant = args.NO
if applicant == 0:
    personal_info = personal_info_0
elif applicant == 1:
    personal_info = personal_info_1
elif applicant == 2:
    personal_info = personal_info_2
elif applicant == 3:
    personal_info = personal_info_3

print(personal_info)

# isNotAvailable(loc.text, except_date_text)
# isNotAvailable(span.text, except_date_text)


def isNotAvailable(day_text, exception):
    isNotAvailable = True
    for t in exception:
        if t in day_text:
            isNotAvailable = True
            break
        else:
            isNotAvailable = False
    return isNotAvailable


# isAvailable(loc.text, expect_date_text)
# isAvailable(span.text, expect_date_text)
def isAvailable(day_text, expectation):
    isAvailable = False
    for t in expectation:
        if t in day_text:
            isAvailable = True
            break
        else:
            isAvailable = False
    return isAvailable


# parser = argparse.ArgumentParser(description='Please choose applicant')
# parser.add_argument('-N', '--NO', default=0)
# args = parser.parse_args()
# print(args)
# applicant = args.NO
# if applicant == 0:
#     personal_info = personal_info_0
# elif applicant == 1:
#     personal_info = personal_info_1
# elif applicant == 2:
#     personal_info = personal_info_2
# elif applicant == 3:
#     personal_info = personal_info_3

browser = webdriver.Chrome()
# url = f"file: // /Users/evenqaq/Dev/Codes/PythonApps/LicenseAppointment/test.html"
browser.get(
    "file:///Users/evenqaq/Dev/Codes/PythonApps/LicenseAppointment/test.html")
# browser.implicitly_wait(3)

# locs = browser.find_elements_by_class_name("text-capitalize")


# firstName = browser.find_element_by_id(
#     "firstName").send_keys("Yijie")
# lastName = browser.find_element_by_id(
#     "lastName").send_keys("Xu")
# phone = browser.find_element_by_id(
#     "phone").send_keys("(609) 356-9060")
# email = browser.find_element_by_id(
#     "email").send_keys("yijiex@princeton.edu")

firstName = browser.find_element_by_id(
    "firstName").send_keys(personal_info['firstName'])
lastName = browser.find_element_by_id(
    "lastName").send_keys(personal_info['lastName'])
phone = browser.find_element_by_id(
    "phone").send_keys(personal_info['phone'])
email = browser.find_element_by_id(
    "email").send_keys(personal_info['email'])

birthDate = browser.find_element_by_id(
    "birthDate").send_keys(personal_info['birthDate'])
s = Select(
    browser.find_element_by_id("permitType"))
s.select_by_value("Class D")
# s = Select(
#     browser.find_element_by_id("test"))
# s.select_by_value("Auto")

birthDate = browser.find_element_by_id(
    "driverLicense").send_keys(personal_info['driverLicense'])

browser.find_element_by_id("receiveTexts").click()
browser.find_element_by_name("Attest").click()


# click submit
submit_btn = browser.find_element_by_xpath(
    "//input[@value='Submit']")
submit_btn.click()

# f.write("!!!!!")
# f.write("get")
print("get")

# browser.quit()

time.sleep(5)
# f.close()
