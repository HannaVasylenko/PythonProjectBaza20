import pytest
from playwright.sync_api import Page
from pytest import fixture


@fixture
def setup(page: Page) -> Page:
    page.goto('/')
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    yield page


@pytest.fixture(autouse=True)
def screenshot_after_test(request, setup: Page):
    yield
    test_name = request.node.name
    screenshot_path = f"test_scr/{test_name}.png"
    setup.screenshot(path=screenshot_path)


@fixture
def setup_en(page: Page) -> Page:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    yield page


@fixture
def setup_pl(page: Page) -> Page:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    yield page

