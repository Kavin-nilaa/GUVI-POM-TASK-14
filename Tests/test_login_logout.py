
from driver_setup import get_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_positive_cases():
    driver = get_driver()
    login = LoginPage(driver)
    home = HomePage(driver)

    try:
        # open login page
        login.open_login_page()

        #check username is displayed and enabled
        login.check_email_box()

        # check password is displayed and enabled
        login.check_password_box()

        #check sign in button is displayed and enabled
        login.check_signin_button()

        #Successful login
        login.login("kavinnilaaj@gmail.com","Nilaasankar99")

        #verify login page
        home.verify_login()

        #logout
        home.logout()

    finally:
        home.close_browser()

def test_negative_cases():
    driver = get_driver()
    login = LoginPage(driver)

    try:
        # open login page
        login.open_login_page()

        # attempt invalid login
        login.login("wronguser@example.com", "wrongpassword")

        # verify error message
        error_text = login.get_error_message()
        assert "Invalid email or password" in error_text

    finally:
        driver.quit()



