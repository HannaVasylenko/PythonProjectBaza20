import re
from playwright.sync_api import Page, expect


def test_ff_mandatory_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//label[@for='firstName']")).to_have_text("Name *")
    expect(page.locator("//label[@for='email']")).to_have_text("Email *")
    expect(page.locator("//label[@for='message']")).to_have_text("Message *")
    expect(page.get_by_role("button", name="Send")).to_be_visible()
    expect(page.get_by_role("button", name="Send")).to_be_enabled()
    page.get_by_role("heading", name="Feedback form").click()
    page.screenshot(path="ff_ffen_scr/ffmandatory.png")


def test_ff_title_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//section[@class='ContactFormSection_section__F3_Zu']//h2")).to_have_text("Feedback form")
    page.get_by_role("heading", name="Feedback form").click()
    page.screenshot(path="ff_ffen_scr/fftitle.png")


def test_ff_active_sendbtn_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Test")
    page.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("Your message").type("Test test Test test")
    expect(page.get_by_role("button", name="Send")).to_be_enabled()
    page.screenshot(path="ff_ffen_scr/ffactsendbtn.png")


def test_ff_hover_sendbtn_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Send").hover()
    page.screenshot(path="ff_ffen_scr/ffhovsendbtn.png")


def test_ff_default_sendbtn_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.get_by_role("button", name="Send")).to_be_enabled()
    page.screenshot(path="ff_ffen_scr/ffdefsendbtn.png")


def test_ff_disabled_sendbtn_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("Your message").click()
    expect(page.get_by_role("button", name="Send")).to_be_disabled()
    page.screenshot(path="ff_ffen_scr/ffdissendbtn.png")


def test_ff_send_form_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Unit test en")
    page.get_by_placeholder("email@gmail.com").type("unittesten@gmail.com")
    page.get_by_placeholder("Your message").type("unit test mes en")
    page.get_by_role("button", name="Send").click()
    page.screenshot(path="ff_ffen_scr/ffsendf.png")


def test_ff_placeholders_fields_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("placeholder", "Name")
    expect(page.locator("//input[@id='email']")).to_have_attribute("placeholder", "email@gmail.com")
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("placeholder", "Your message")
    page.get_by_role("heading", name="Feedback form").click()
    page.screenshot(path="ff_ffen_scr/ffplacehold.png")