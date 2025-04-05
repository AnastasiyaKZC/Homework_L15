"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Фикстура с параметризацией для разных размеров окна
@pytest.fixture(params=[(1920, 1080), (1366, 768), (375, 812), (414, 896)])
def browser(request):
    driver = webdriver.Chrome()
    width, height = request.param  # Получаем параметры (ширина и высота)
    driver.set_window_size(width, height)  # Устанавливаем размер окна
    yield driver
    driver.quit()

# Пропускаем мобильный тест, если соотношение сторон десктопное (и наоборот)
@pytest.mark.parametrize("browser", [(1920, 1080), (1366, 768)], indirect=True)
def test_github_desktop(browser):
    # Получаем текущие размеры окна браузера
    window_size = browser.get_window_size()
    width = window_size['width']
    height = window_size['height']
    # Пропуск теста, если устройство мобильное (ширина < высоты)
    if width < height:
        pytest.skip("Пропускаем тест, так как это мобильная версия")

    driver = browser
    driver.get("https://github.com/")
    # Находим и кликаем по ссылке "Sign up"
    sign_up_button = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_button.click()
    # Проверка наличия ожидаемого текста на странице
    assert "Create your free account" in driver.page_source


@pytest.mark.parametrize("browser", [(375, 812), (414, 896)], indirect=True)
def test_github_mobile(browser):
    # Получаем текущие размеры окна браузера
    window_size = browser.get_window_size()
    width = window_size['width']
    height = window_size['height']
    # Пропуск теста, если устройство не мобильное (ширина >= высоты)
    if width >= height:
        pytest.skip("Пропускаем тест, так как это десктопная версия")

    driver = browser
    driver.get("https://github.com/")
    # Кликаем на гамбургер-меню
    menu_button = driver.find_element(
        By.CSS_SELECTOR,
        "body > div.logged-out.env-production.page-responsive.header-overlay.header-overlay-fixed.js-header-overlay-fixed > div.position-relative.header-wrapper.js-header-wrapper > header > div > div.d-flex.flex-justify-between.flex-items-center.width-full.width-lg-auto > div:nth-child(1) > button > span"
    )
    menu_button.click()
    # Кликаем по ссылке "Sign up"
    sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_link.click()
    # Проверка наличия текста на странице
    assert "Create your free account" in driver.page_source