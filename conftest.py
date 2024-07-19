import pytest
from pytest import fixture
from playwright.sync_api import Page, sync_playwright


@fixture
def setup(page: Page) -> Page:
    page.goto('/')
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    yield page

