"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selenium import webdriver

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
    pass


def test_github_mobile(mobile_browser):
    pass


