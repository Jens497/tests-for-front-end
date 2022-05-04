'''
@author: SKR
'''
import time
import datetime
from selenium.webdriver.common.by import By


class SeleniumHelpers(object):

    def __init__(self, driver):
        self.driver = driver
        self.command_send_time = None

    def send_find_element_command(self, by, value, elements=False):
        """
        @param by: how the element should be found e.g by_id
        @type by: object
        @param value: the string/int/float the element should be found e.g 1 (if id is 1)
        @type value: string/int/float
        @param elements: if it should return multiple elements with the same naming
        @type elements: boolean
        @return: returns the element(s) if it was found
        @rtype: object/list of objects
        """
        return_element = ""

        # A throttle for sending commands
        # Check if we need to wait before sending next command
        # Setting throttle to around 2 seconds.
        if (self.command_send_time is not None):
            time_since_last = datetime.datetime.now() - self.command_send_time
            if (time_since_last.microseconds < 2000000):
                print ("Throttling command to be send (Selenium). Waiting %f." % (
                            2 - time_since_last.microseconds / float(2000000)))
            time.sleep((2 - time_since_last.microseconds / float(2000000)))

        # Save time for command throttling
        self.command_send_time = datetime.datetime.now()

        if elements:
            return_element = self.driver.find_elements(by, value)
        else:
            return_element = self.driver.find_element(by, value)

        if return_element == "":
            raise ("The element was NOT visible!")

        return return_element


    def test_example(self):
        get_url = self.local_ip
        self.driver.get(get_url)
        time.sleep(3)
        self.find_element_by_xpath("//a[text()='Log in']").click()
        time.sleep(5)
        print ("DONE")
        self.driver.quit()


    def find_element_by_xpath(self, value, elements=False):
        """
        @param value: the string the element should be found with
        @type value: string
        @param elements: if it should return multiple elements with the same naming
        @type elements: boolean
        @return: returns the element if it was found
        @rtype: object/list of objects
        """
        return_element = self.send_find_element_command(By.XPATH, value, elements)

        return return_element


    def find_element_by_class_name(self, value, elements=False):
        """
        @param value: the string the element should be found with
        @type value: string
        @param elements: if it should return multiple elements with the same naming
        @type elements: boolean
        @return: returns the element if it was found
        @rtype: object/list of objects
        """
        return_element = self.send_find_element_command(By.CLASS_NAME, value, elements)

        return return_element


    def find_element_by_tag_name(self, value, elements=False):
        """
        @param value: the string the element should be found with
        @type value: string
        @param elements: if it should return multiple elements with the same naming
        @type elements: boolean
        @return: returns the element if it was found
        @rtype: object/list of objects
        """
        return_element = self.send_find_element_command(By.TAG_NAME, value, elements)

        return return_element


    def find_element_by_id(self, value, elements=False):
        """
        @param value: the string the element should be found with
        @type value: string
        @param elements: if it should return multiple elements with the same naming
        @type elements: boolean
        @return: returns the element if it was found
        @rtype: object/list of objects
        """
        return_element = self.send_find_element_command(By.ID, value, elements)

        return return_element


if __name__ == "__main__":
    test_class = SeleniumHelpers()
    test_class.test_example()
