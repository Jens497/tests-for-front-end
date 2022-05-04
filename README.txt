Step1. First of all to make the test run, you need to make sure, that the host server is up and running.
Step2. Download a chromedriver and change the file path to in TestBank.py on line 57:
    - self.driver = webdriver.Chrome("path to driver")
Step3. Install selenium package, can be done from IDE, when hovering over the import.
Step4. Run the tests from main.py