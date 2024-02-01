import re
import time

from assertpy import assert_that
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from core.base_page import BaseScreen
from core.data_classes import Config
from pages.my_account_page.elements import MyAccountPageEle


class MyAccountPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = ""
        self.ele = MyAccountPageEle

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def select_my_account(self):
        self.log.info(f"Click the {self.ele.lnk_my_account_page.name}")
        self.se_helper.get_element(self.ele.lnk_my_account_page).click()

    def select_addresses(self):
        self.log.info(f"Click the {self.ele.lnk_addresses_page.name}")
        self.se_helper.get_element(self.ele.lnk_addresses_page).click()

    def select_edit_billing(self):
        self.log.info(f"Click the {self.ele.billing_edit_page.name}")
        self.se_helper.get_element(self.ele.billing_edit_page).click()

    def select_edit_shipping(self):
        self.log.info(f"Click the {self.ele.shipping_edit_page.name}")
        self.se_helper.get_element(self.ele.shipping_edit_page).click()

    def verify_login(self):
        if self.driver.find_elements(By.CSS_SELECTOR, ".woocommerce-MyAccount-content"):
            self.log.info("Login successfully.")
            return True
        return False

    def get_account_name(self):
        text = self.driver.find_element(By.CSS_SELECTOR, ".woocommerce-MyAccount-content").text
        return re.search(r"Hello\s(\w+)\s", text).group(1)

    def verify_page_title(self):
        self.log.info("Verify the page title")
        title = self.driver.title
        assert_that(title).contains("My Account")

    def register(self, account):
        self.log.info(f"Register a new account with email {account.email} and password "
                      f"{account.password}")
        self.se_helper.get_element(self.ele.register_email_ele).clear()
        self.se_helper.get_element(self.ele.register_email_ele).send_keys(account.email)
        self.se_helper.get_element(self.ele.register_pw_ele).clear()
        self.se_helper.get_element(self.ele.register_pw_ele).send_keys(account.password)
        self.se_helper.get_element(self.ele.register_button_ele).click()

    def logout(self):
        self.log.info("Log out.")
        self.se_helper.get_element(self.ele.logout_ele).click()

    def login(self, account, password):
        self.log.info(f"Login with account {account} and password {password}")
        self.se_helper.get_element(self.ele.login_account_ele).clear()
        self.se_helper.get_element(self.ele.login_account_ele).send_keys(account)
        self.se_helper.get_element(self.ele.login_pw_ele).clear()
        self.se_helper.get_element(self.ele.login_pw_ele).send_keys(password)
        self.se_helper.get_element(self.ele.login_button_ele).click()

    def set_billing_address(self, account):
        self.log.info("Edit billing address.")
        self.select_edit_billing()
        self.se_helper.get_element(self.ele.billing_first_name_ele).clear()

        self.se_helper.get_element(self.ele.billing_first_name_ele).send_keys(account.first_name)
        self.se_helper.get_element(self.ele.billing_last_name_ele).clear()
        self.se_helper.get_element(self.ele.billing_last_name_ele).send_keys(account.last_name)

        self.se_helper.get_element(self.ele.billing_phone_ele).clear()
        self.se_helper.get_element(self.ele.billing_phone_ele).send_keys(str(account.phone))

        self.se_helper.get_element(self.ele.billing_country_ele).click()
        self.se_helper.get_element(self.ele.billing_country_search_ele).send_keys(account.country)
        self.se_helper.get_element(self.ele.billing_country_select_ele).click()

        self.se_helper.get_element(self.ele.billing_address_ele).clear()
        self.se_helper.get_element(self.ele.billing_address_ele).send_keys(account.address)

        self.se_helper.get_element(self.ele.billing_city_ele).clear()
        self.se_helper.get_element(self.ele.billing_city_ele).send_keys(account.city)

        if self.driver.find_elements(By.ID, self.ele.billing_state_ele.value):
            self.se_helper.get_element(self.ele.billing_state_ele).click()
            self.se_helper.get_element(self.ele.billing_state_search_ele).send_keys(account.state)
            self.se_helper.get_element(self.ele.billing_state_select_ele).click()

        self.se_helper.get_element(self.ele.billing_postcode_ele).clear()
        self.se_helper.get_element(self.ele.billing_postcode_ele).send_keys(str(account.postcode))

        self.driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.se_helper.get_element(self.ele.save_button_ele).click()

    def set_shipping_address(self, account):
        self.log.info("Edit shipping address.")
        self.select_edit_shipping()
        self.se_helper.get_element(self.ele.shipping_first_name_ele).clear()
        self.se_helper.get_element(self.ele.shipping_first_name_ele).send_keys(account.first_name)

        self.se_helper.get_element(self.ele.shipping_last_name_ele).clear()
        self.se_helper.get_element(self.ele.shipping_last_name_ele).send_keys(account.last_name)

        self.se_helper.get_element(self.ele.shipping_country_ele).click()
        self.se_helper.get_element(self.ele.shipping_country_search_ele).send_keys(account.country)
        self.se_helper.get_element(self.ele.shipping_country_select_ele).click()

        self.se_helper.get_element(self.ele.shipping_address_ele).clear()
        self.se_helper.get_element(self.ele.shipping_address_ele).send_keys(account.address)

        self.se_helper.get_element(self.ele.shipping_city_ele).clear()
        self.se_helper.get_element(self.ele.shipping_city_ele).send_keys(account.city)

        if self.driver.find_elements(By.ID, self.ele.shipping_state_ele.value):
            self.se_helper.get_element(self.ele.shipping_state_ele).click()
            (self.se_helper.get_element(self.ele.shipping_state_search_ele)
             .send_keys(account.country))
            self.se_helper.get_element(self.ele.shipping_state_select_ele).click()

        self.se_helper.get_element(self.ele.shipping_postcode_ele).clear()
        self.se_helper.get_element(self.ele.shipping_postcode_ele).send_keys(str(account.postcode))

        self.driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.se_helper.get_element(self.ele.save_button_ele).click()

    def get_billing_address(self):
        return self.se_helper.get_element(self.ele.billing_info_ele).text

    def get_shipping_address(self):
        return self.se_helper.get_element(self.ele.shipping_info_ele).text
