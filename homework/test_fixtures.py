"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(params=[(1920, 1080), (1366, 768)])
def desktop_browser(request):
    driver = webdriver.Chrome()
    width, height = request.param  # Получаем параметры
    driver.set_window_size(width, height)
    yield driver
    driver.quit()

@pytest.fixture(params=[(375, 812), (414, 896)])
def mobile_browser(request):
    driver = webdriver.Chrome()
    width, height = request.param
    driver.set_window_size(width, height)
    yield driver
    driver.quit()

def test_github_desktop(desktop_browser):
    driver = desktop_browser
    driver.get("https://github.com/")

    # Находим и кликаем по ссылке "Sign up"
    sign_up_button = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_button.click()
    assert "Create your free account" in driver.page_source


def test_github_mobile(mobile_browser):
    driver = mobile_browser
    driver.get("https://github.com/")

    # Кликаем на гамбургер-меню (Toggle navigation)
    menu_button = driver.find_element(By.CSS_SELECTOR, "body > div.logged-out.env-production.page-responsive.header-overlay.header-overlay-fixed.js-header-overlay-fixed > div.position-relative.header-wrapper.js-header-wrapper > header > div > div.d-flex.flex-justify-between.flex-items-center.width-full.width-lg-auto > div:nth-child(1) > button > span")
    menu_button.click()

    # Кликаем по ссылке Sign up
    sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_link.click()
    assert "Create your free account" in driver.page_source

