from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def open_url(self,url):
        self.driver.get(url)

    def element_displayed_enabled(self,locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.is_enabled()
        return element.is_displayed() and element.is_enabled()

    def enter_text(self,locators,value):
        element = self.wait.until(EC.visibility_of_element_located(locators))
        element.clear()
        element.send_keys(value)

    def click(self,locator):
        click_element = self.wait.until(EC.element_to_be_clickable(locator))
        click_element.click()

    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def close_browser(self):
        self.driver.quit()
