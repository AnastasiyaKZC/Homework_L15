import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser(request):
    """Фикстура, которая создает браузер и устанавливает размер окна"""
    driver = webdriver.Chrome()
    width, height = request.param
    driver.set_window_size(width, height)
    yield driver
    driver.quit()


# Параметризация теста под десктопные разрешения
@pytest.mark.parametrize("browser", [(1920, 1080), (1366, 768)], indirect=True)
def test_github_desktop(browser):
    driver = browser
    driver.get("https://github.com/")

    # Находим и кликаем по ссылке "Sign up"
    sign_up_button = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_button.click()

    # Проверка наличия текста на странице
    assert "Create your free account" in driver.page_source


# Параметризация теста под мобильные разрешения
@pytest.mark.parametrize("browser", [(375, 812), (414, 896)], indirect=True)
def test_github_mobile(browser):
    driver = browser
    driver.get("https://github.com/")

    # Кликаем на гамбургер-меню (Toggle navigation)
    menu_button = driver.find_element(By.CSS_SELECTOR, "body > div.logged-out.env-production.page-responsive.header-overlay.header-overlay-fixed.js-header-overlay-fixed > div.position-relative.header-wrapper.js-header-wrapper > header > div > div.d-flex.flex-justify-between.flex-items-center.width-full.width-lg-auto > div:nth-child(1) > button > span")
    menu_button.click()

    # Кликаем по ссылке Sign up
    sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_link.click()

    # Проверка наличия текста на странице
    assert "Create your free account" in driver.page_source