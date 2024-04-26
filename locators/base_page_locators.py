from selenium.webdriver.common.by import By


class BasePageLocators:
    # Хедер
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
