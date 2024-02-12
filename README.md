# Diplom_3

# Тест-сьют для проверки UI приложения "Stellar Burgers" с помощью Selenium и Pytest

Файлы:
- tests/ - папка с файлами тестов
- tests/test_main_page.py - тесты главной страницы
- tests/test_order_page.py - тесты страницы заказа
- tests/test_header_page.py - тесты хэдера
- tests/test_password_recovery_page.py - тесты хэдера
- tests/test_user_account_page.py - тесты страницы личного кабинета

- pages/ - папка с файлами страниц Page Object
- pages/base_page.py - файл POM, общие методы
- pages/order_page.py - файл POM страницы заказа
- pages/main_page.py - файл POM главной страницы
- pages/header_page.py - файл POM хэдера
- pages/password_recovery_page.py - файл POM страницы восстановления пароля
- pages/user_account_page.py - файл POM страницы личного кабинета

- locators/ - папка с файлами - указателями по страницам для поиска элементов DOM
- data.py - URL-адреса
- conftest.py - фикстуры драйвера, создания и авторизации пользователя
- helpers.py - вспомогательный файл с методом генерации случайной строки

- .gitignore - файл для проекта в Git/GinHub
- requirements.txt - файл с внешними зависимостями
- README.md - файл с описанием проекта (этот файл)

Для запуска тестов должны быть установлены пакеты: 
- pytest,
- selenium, 
- allure-pytest и
- allure-python-commons.
- 
Для генерации отчетов необходимо дополнительно установить:
- фреймворк Allure,
- JDK

Запуск всех тестов выполняется командой:

    pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

    pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:

    allure serve allure_results

