Тема "Page Object" курс ЯндексПрактикум
Проект по автоматизации тестирования сайта "Яндекс.Самокат"
Ссылка на сайт: https://qa-scooter.praktikum-services.ru/
Автотесты подключены в браузере: Firefox
Основа для написания автотестов: Selenium WebDriver, Pytest
Файлы:
tests/ - папка с файлами тестов
tests/test_main_page.py - тесты блока вопросов и ответов на Главной странице
tests/test_order_page.py - тесты страницы заказа
test/test_redirect.py - тесты с переходом на другие страницы

pages/ - папка с файлами страниц Page Object
pages/base_page.py - файл POM общих функций
pages/main_page.py - файл POM Главной страницы
pages/order_page.py - файл POM страницы заказа

locators/ - папка с локаторами для поиска элементов DOM
locators/base_page_locators.py - общие локаторы
locators/main_page_locators.py - локаторы с главной страницы
locators/order_page_locators.py - локаторы со страницы заказа

data.py - другие константы и URL-адреса
.gitignore - файл для проекта в Git/GinHub
requirements.txt - файл с внешними зависимостями
README.md - файл с описанием проекта (этот файл)

Для запуска тестов должны быть установлены пакеты:
pytest,
selenium,
allure-pytest и
allure-python-commons.

Для генерации отчетов необходимо дополнительно установить:
фреймворк Allure,
JDK

Запуск всех тестов выполняется командой:
pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:
pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:
allure serve allure_results
