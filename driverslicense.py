
from os import isatty
from typing import Mapping, runtime_checkable
from selenium import webdriver
import time
import argparse
from datetime import datetime
import AppKit
import time
from selenium.webdriver.support.ui import Select

# 15Initial 17KnowledgeTest
number = 15
round = 1
isRun = True
priority_list0 = ["South Plainfield"]
priority_list1 = ["Edison", "Bakers Basin", "South Plainfield"]
priority_list2 = ["Rahway", "Freehold", "Newark",
                  "Bayonne", "Eatontown", "Toms River", "North Bergen", "Wayne", "Paterson", "Randolph"]
except_date_text = ["Next Available: 09/23",
                    "Next Available: 09/24", "Next Available: 09/25", "Next Available: 09/26", "Next Available: 10/01", "Next Available: 10/02", "Next Available: 12"]

expect_date_text = ["Next Available: 09/18",
                    "Next Available: 09/19", "Next Available: 09/25", "Next Available: 09/26"]

priority_list = priority_list0

# driver & appointment info
personal_info_0 = {'firstName': 'Yijie',
                   'lastName': 'Xu', 'phone': '(609) 356-9060', 'email': 'yijiex@princeton.edu', 'birthDate': "10/21/1998", 'driverLicense': "X90017900060981"}
personal_info_1 = {'firstName': 'Sicheng',
                   'lastName': 'Yin', 'phone': '(753) 697-3514', 'email': 'yinsicheng1999@outlook.com', 'birthDate': '01/19/1999'}
personal_info_2 = {'firstName': 'Dazhao',
                   'lastName': 'Yin', 'phone': '(626) 716-3579', 'email': 'evenqaq@outlook.com', 'birthDate': '06/20/1974'}
personal_info_3 = {'firstName': 'Wenmei',
                   'lastName': 'Wu', 'phone': '(609) 718-9911', 'email': 'even_sc@163.com', 'birthDate': '07/08/1972'}
# permitType = 'Class D'


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
browser = webdriver.Chrome()
url = f"https://telegov.njportal.com/njmvc/AppointmentWizard/{number}"
try:
    browser.get(url)
    browser.implicitly_wait(3)
except TimeoutError:
    print("Timeout")
    browser.quit()


with open("mvc_output" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt", "a") as f:
    while isRun:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"\n\n\nDate Time: {dt_string} \n\n")

        try:
            browser.refresh()  # 刷新方法 refresh
            # print('test pass: refresh successful')
        except Exception as e:
            print("Exception found", format(e))

        locs = browser.find_elements_by_class_name("text-capitalize")
        # print(len(locs))
        if len(locs) != 24:
            f.write("!!!!!")
            time.sleep(0.1)
            AppKit.NSBeep()
            print("error")
            break

        for loc in locs:
            # print(loc)
            # print("loc text")
            # print("!!!")
            # print(loc.text)
            f.write(loc.text)
            for location in priority_list:
                if location in loc.text:
                    # if True:
                    # print("print loc text")
                    # print(type(loc.text))
                    # print(location)
                    if not "No Appointments Available" in loc.text:
                        print("Have Appointments")
                        # if isAvailable(loc.text, expect_date_text):
                        if not isNotAvailable(loc.text, except_date_text):
                            # if True:
                            bs = browser.find_elements_by_class_name("btn")
                            to_click = None
                            for b in bs:
                                if b.text == "MAKE APPOINTMENT":
                                    print(dir(b))
                                    id = b.get_property("id")
                                    print(f"dateText{id[7:]}")
                                    span = browser.find_element_by_id(
                                        f"dateText{id[7:]}")
                                    print(span.text)
                                    # if isAvailable(span.text, expect_date_text):
                                    if not isNotAvailable(span.text, except_date_text):
                                        # if True:
                                        to_click = b
                                        break
                            print(to_click.text)
                            to_click.click()

                            # html_choose = open("choose.html", "wb")
                            # html_choose.write(
                            #     browser.page_source.encode("utf-8", "ignore"))
                            # html_choose.close()

                            slots = browser.find_elements_by_class_name(
                                "text-primary")
                            for slot in slots:
                                slot.click()
                                break

                            # html_info = open("info.html", "wb")
                            # html_info.write(
                            #     browser.page_source.encode("utf-8", "ignore"))
                            # html_info.close()
                            time.sleep(1)

                            firstName = browser.find_element_by_id(
                                "firstName").send_keys(personal_info['firstName'])
                            lastName = browser.find_element_by_id(
                                "lastName").send_keys(personal_info['lastName'])
                            phone = browser.find_element_by_id(
                                "phone").send_keys(personal_info['phone'])
                            email = browser.find_element_by_id(
                                "email").send_keys(personal_info['email'])

                            s = Select(
                                browser.find_element_by_id("permitType"))
                            s.select_by_value("Class D")

                            birthDate = browser.find_element_by_id(
                                "birthDate").send_keys(personal_info['birthDate'])

                            # s = Select(
                            #     browser.find_element_by_id("test"))
                            # s.select_by_value("Auto")

                            # birthDate = browser.find_element_by_id(
                            #     "driverLicense").send_keys(personal_info['driverLicense'])

                            browser.find_element_by_id("receiveTexts").click()
                            browser.find_element_by_name("Attest").click()

                            # click submit
                            submit_btn = browser.find_element_by_xpath(
                                "//input[@value='Submit']")
                            submit_btn.click()

                            f.write("!!!!!")
                            f.write("get")
                            print("get")

                            isRun = False
                            break
                        break
        # browser.close()
        f.write("end round = " + str(round))
        round += 1
        time.sleep(5)
browser.quit()
# f.close()
while True:
    AppKit.NSBeep()
