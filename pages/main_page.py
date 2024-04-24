from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    # метод для получения текста вопроса
    def click_on_question(self, index):
        method, locator = MainPageLocators.FAQ_QUESTION
        locator = locator.format(index)
        self.wait_for_load_element((method, locator))
        question = self.find_element((method, locator))
        question.click()
        return question.text

    # метод для получения текста ответа
    def get_answer(self, index):
        method, locator = MainPageLocators.FAQ_ANSWER
        locator = locator.format(index)
        self.wait_for_load_element((method, locator))
        return self.find_element((method, locator)).text
