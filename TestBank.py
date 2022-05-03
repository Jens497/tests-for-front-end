from SeleniumHelpers import SeleniumHelpers
from FileLogger import FileLogging
import unittest
from selenium import webdriver
import time
import sys
import traceback
from io import StringIO
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


STDOUT_LINE = '\n\n%s'
STDERR_LINE = '\n\n%s'

class TestBank(unittest.TestCase):
    """
    """
    def _setupStdout(self):
        if self._stderr_buffer is None:
            self._stderr_buffer = StringIO()
            self._stdout_buffer = StringIO()
        sys.stdout = self._stdout_buffer
        sys.stderr = self._stderr_buffer

    def _restoreStdout(self):
        output = sys.stdout.getvalue()
        error = sys.stderr.getvalue()
        if output:
            if not output.endswith('\n'):
                output += '\n'
            self._original_stdout.write(STDOUT_LINE % output)
        if error:
            if not error.endswith('\n'):
                error += '\n'
            self._original_stderr.write(STDERR_LINE % error)

        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr
        self._stdout_buffer.seek(0)
        self._stdout_buffer.truncate()
        self._stderr_buffer.seek(0)
        self._stderr_buffer.truncate()

    def setUp(self):
        super(TestBank, self).setUp()
        self._stdout_buffer = None
        self._stderr_buffer = None
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr

        self.driver = webdriver.Chrome("C:/Users/Jens/Downloads/chromedriver.exe")

        self.local_ip = "https://recipe.bhsi.xyz/frontend"
        self.driver.get(self.local_ip)
        self.helpers = SeleniumHelpers(driver=self.driver)
        self.logger = FileLogging()
        self.driver.implicitly_wait(30)

        self.logger.info("*************Test Case method starts********")
        self._setupStdout()
        self.logger.info(self._testMethodName)  # Shows MethodName of current running method
        self.logger.info("*************Test Case method ends********")
        # print "Done with setup"
        # print self._testMethodName
        # self.logger.info("Done with setup")
        # self.logger.warn(self._testMethodName)

    def tearDown(self):
        super(TestBank, self).tearDown()
        self.logger.info("********TestClass.tearDown starts*************")
        exctype, value, tb = sys.exc_info()[:3]
        if exctype:  # An exception happened, report it
            msg = traceback.format_exception(exctype, value, tb)

            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            if output:
                if not output.endswith('\n'):
                    output += '\n'
                msg.append(STDOUT_LINE % output)
            if error:
                if not error.endswith('\n'):
                    error += '\n'
                msg.append(STDERR_LINE % error)
            dsa = ''.join(msg)
            # print dsa
            self.logger.error(dsa)
            # print dsa
            # if exctype == self.failureException:  # Register failure, do some post-processing if needed
            # self.on_fail()
        self._restoreStdout()
        self.logger.info("********TestClass.tearDown ends*************")

    def _sign_up(self):
        """
        """
        first_name = "Jens"
        last_name = "Kloster"
        username = "Bozeri"
        email = "dsa@dsa.com"
        password = "123123"

        try:
            self.helpers.find_element_by_xpath("//a[text()='Sign up']").click()
            # input_field = self.helpers.find_element_by_xpath("//input[value id()='mui-1']")
            self.logger.info("Filling out the login form")
            input_field_first_name = self.helpers.find_element_by_id('mui-1')
            input_field_last_name = self.helpers.find_element_by_id('mui-2')
            input_field_username = self.helpers.find_element_by_id('mui-3')
            input_field_email = self.helpers.find_element_by_id('mui-4')
            input_field_password = self.helpers.find_element_by_id('mui-5')
            input_field_passwd_confirm = self.helpers.find_element_by_id('mui-6')
            input_field_first_name.send_keys(first_name)
            input_field_last_name.send_keys(last_name)
            input_field_username.send_keys(username)
            input_field_email.send_keys(email)
            input_field_password.send_keys(password)
            input_field_passwd_confirm.send_keys(password)
            input_field_passwd_confirm.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            raise AssertionError(e)


    def test_see_all_recipe_btn(self):
        """
        Test when click on the 'see all recipes' on home page, that it redirects you to signup page.
        """
        url_after_click = self.local_ip + "/signup"
        self.logger.info("Finding btn-all-recipes and clicking on it")
        try :
            self.helpers.find_element_by_id("btn-all-recipes").click()
            self.logger.info("Redirecting to sign up page.")
        except NoSuchElementException as e:
            raise AssertionError(e)

        unique_print = self.helpers.find_element_by_xpath("//button[text()='Sign up']")

        if unique_print and self.driver.current_url == url_after_click:
            self.logger.info("SUCCESS.:\nThe button redirected to sign up page.")
        else:
            raise AssertionError("The button did not redirect to signup page")


    def check_sign_up(self):
        """
        Check that when signing up then under profile its the same as what you signed up with.
        """
        self.logger.info("Redirecting to sign up page.")
        first_name = "Jens"
        last_name = "Kloster"
        username = "Bozeri"
        email = "dsa@dsa.com"
        password = "123123"
        try:
            self.logger.info("Redirecting to /sign up")
            self.helpers.find_element_by_xpath("//a[text()='Sign up']").click()
            #input_field = self.helpers.find_element_by_xpath("//input[value id()='mui-1']")
            self.logger.info("Filling out the login form")
            input_field_first_name = self.helpers.find_element_by_id('mui-1')
            input_field_last_name = self.helpers.find_element_by_id('mui-2')
            input_field_username = self.helpers.find_element_by_id('mui-3')
            input_field_email = self.helpers.find_element_by_id('mui-4')
            input_field_password = self.helpers.find_element_by_id('mui-5')
            input_field_passwd_confirm = self.helpers.find_element_by_id('mui-6')
            input_field_first_name.send_keys(first_name)
            input_field_last_name.send_keys(last_name)
            input_field_username.send_keys(username)
            input_field_email.send_keys(email)
            input_field_password.send_keys(password)
            input_field_passwd_confirm.send_keys(password)
            # time.sleep(10)
            self.logger.info("Submitting form by 'Enter' key press")
            input_field_passwd_confirm.send_keys(Keys.ENTER)
            self.logger.info("Clicking on avatar icon")
            self.helpers.find_element_by_xpath("//*[@data-testid='PersonIcon']").click()
            self.logger.info("Clicking in on the profile page")
            self.helpers.find_element_by_xpath("//p[text()='Profile']").click()

            #Next
            profile_name = self.helpers.find_element_by_xpath("//p[text()='Name:']/..//following-sibling::div//p").text
            profile_username = self.helpers.find_element_by_xpath("//p[text()='Username:']/..//following-sibling::div//p").text
            profile_email = self.helpers.find_element_by_xpath("//p[text()='Email:']/..//following-sibling::div//p").text
            #print (profile_name, profile_username, profile_email)
            self.assertEqual(profile_name, first_name + " " + last_name, "The signed up first and last name did not match the profiles!")
            self.assertEqual(username, profile_username, "The signed up username did not match the profiles!")
            self.assertEqual(email, profile_email, "The signed up email did not match the profiles!")
            self.logger.info("The test was a success.")

            # time.sleep(10)
        except NoSuchElementException as e:
            raise AssertionError(e)

    def test_lists_filters(self):
        """
        """
        self._sign_up()

        self.helpers.find_element_by_xpath("//a[text()='Lists']").click()
        self.helpers.find_element_by_xpath("//div[contains(@class, 'MuiFormGroup-root css-1h7anqn')]/label/span/input").click()

        text_t = self.helpers.find_element_by_xpath("//div[contains(@class, 'MuiFormGroup-root css-1h7anqn')]/label/span/following-sibling::span").text
        self.logger.info("Unchecking list: %s" % text_t)

        #time.sleep(3)
        header_elements = self.helpers.find_element_by_class_name('list-header', True)
        for list_name in header_elements:
            if text_t == list_name.text:
                raise AssertionError("The test failed, the %s list is still shown" % text_t)
        self.logger.info("The list was unchecked.")

    def search_for_recipe(self):
        """
        """
        search_key = "oa"
        self._sign_up()
        self.helpers.find_element_by_xpath("//a[text()='Lists']").click()
        #input_field = self.helpers.find_element_by_id('mui-32')
        #input_field.send_keys('oatmeal')
        self.helpers.find_element_by_xpath("//input").send_keys(search_key)
        card_headers = self.helpers.find_element_by_xpath("//div[contains(@class, 'MuiCardContent-root')]/h5", True)
        for recipe_name in card_headers:
            if search_key not in recipe_name:
                raise AssertionError("The search key did not work, there is recipes that does not contain the search key: %s" % search_key)
        self.logger.info("The search went well !")


    def test_login(self):
        # get_url = self.local_ip
        # self.driver.get(get_url)
        time.sleep(3)
        self.helpers.find_element_by_xpath("//a[text()='Log in']").click()
        time.sleep(5)
        self.driver.quit()


def suites():
    """
    """
    suite = unittest.TestSuite()
    # suite.addTest(TestBank('test_see_all_recipe_btn'))
    suite.addTest(TestBank('search_for_recipe'))
    # suite.addTest(TestBank('check_username_after_login'))
    # suite.addTest(TestBank('test_login'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suites())
