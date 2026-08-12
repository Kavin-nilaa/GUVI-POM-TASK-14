from selenium.webdriver.common.by import By

from pages.base_page import Basepage


class HomePage(Basepage):
    POPUP = (By.CLASS_NAME,"custom-close-button")
    DASHBOARD = (By.CLASS_NAME,"header-name")
    DROPDOWN = (By.CSS_SELECTOR,".avatar-profile-name.d-flex.fs-normal.m-0")
    LOGOUT = (By.XPATH,"//div[text()='Log out']")


    def verify_login(self):
        try:
            self.click(self.POPUP)
            print("Popup Appeared")
        except:
            print("No Popup Appeared")
        actual = self.get_text(self.DASHBOARD)
        assert actual == "Dashboard"

    def logout(self):
        self.click(self.DROPDOWN)
        self.element_displayed_enabled(self.LOGOUT)
        self.click(self.LOGOUT)

    def close(self):
        self.close_browser()



