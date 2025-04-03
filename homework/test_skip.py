"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selenium import webdriver

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
    width, height = browser.get_window_size()
    if width < height:  # Если ширина меньше высоты — мобильное устройство
        pytest.skip("Пропускаем тест, так как это мобильная версия")
    # Здесь можно добавить логику для теста на десктопе
    pass

@pytest.mark.parametrize("browser", [(375, 812), (414, 896)], indirect=True)
def test_github_mobile(browser):
    width, height = browser.get_window_size()
    if width >= height:  # Если ширина больше или равна высоте — десктоп
        pytest.skip("Пропускаем тест, так как это десктопная версия")
    # Здесь можно добавить логику для теста на мобильном
    pass