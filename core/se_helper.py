from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from core.data_classes import Config, FormElement


class SeleniumHelper:
    def __init__(self, config: Config):
        self.__config = config

    def get_element(self, form_element: FormElement) -> WebElement:
        try:
            match form_element.by:
                case "ID":
                    return self.__config.driver.find_element(By.ID, form_element.value)
                case "XPATH":
                    return self.__config.driver.find_element(By.XPATH, form_element.value)
                case "LINK_TEXT":
                    return self.__config.driver.find_element(By.LINK_TEXT, form_element.value)
                case "PARTIAL_LINK_TEXT":
                    return self.__config.driver.find_element(By.PARTIAL_LINK_TEXT, form_element.value)
                case "NAME":
                    return self.__config.driver.find_element(By.NAME, form_element.value)
                case "TAG_NAME":
                    return self.__config.driver.find_element(By.TAG_NAME, form_element.value)
                case "CLASS_NAME":
                    return self.__config.driver.find_element(By.CLASS_NAME, form_element.value)
                case "CSS_SELECTOR":
                    return self.__config.driver.find_element(By.CSS_SELECTOR, form_element.value)
                case _:
                    self.__config.log.error(f"By '{form_element.by}' is not supported")
                    raise Exception(f"By '{form_element.by}' not supported !!!")
        except NoSuchElementException as e:
            raise e
