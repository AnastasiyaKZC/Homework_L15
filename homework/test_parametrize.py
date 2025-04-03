"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    """Фикстура, которая создает браузер и устанавливает размер окна"""
    driver = webdriver.Chrome()  # Запускаем браузер
    width, height = request.param  # Получаем параметры (размер окна)
    driver.set_window_size(width, height)  # Устанавливаем размер окна

    yield driver  # Возвращаем объект браузера для тестов

    driver.quit()  # Закрываем браузер после теста


# Параметризация тестов с передачей параметров в фикстуру
@pytest.mark.parametrize("browser", [(1920, 1080), (1366, 768)], indirect=True)
def test_github_desktop(browser):
    pass


@pytest.mark.parametrize("browser", [(375, 812), (414, 896)], indirect=True)
def test_github_mobile(browser):
    pass
