import re
from playwright.sync_api import Page, expect


def test_ff_mandatory_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//label[@for='firstName']")).to_have_text("Imię *")
    expect(page.locator("//label[@for='email']")).to_have_text("E-mail *")
    expect(page.locator("//label[@for='message']")).to_have_text("Wiadomość *")
    expect(page.get_by_role("button", name="Wyślać")).to_be_visible()
    expect(page.get_by_role("button", name="Wyślać")).to_be_enabled()
    page.get_by_role("heading", name="Formularz zwrotny").click()
    page.screenshot(path="ff_ffpl_scr/ffmandatory.png")


def test_ff_title_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//section[@class='ContactFormSection_section__F3_Zu']//h2")).to_have_text("Formularz zwrotny")
    page.get_by_role("heading", name="Formularz zwrotny").click()
    page.screenshot(path="ff_ffpl_scr/fftitle.png")


def test_ff_active_sendbtn_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Świętosław")
    page.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").type("Świętosław Róża Więcław")
    expect(page.get_by_role("button", name="Wyślać")).to_be_enabled()
    page.screenshot(path="ff_ffpl_scr/ffactsendbtn.png")


def test_ff_hover_sendbtn_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Wyślać").hover()
    page.screenshot(path="ff_ffpl_scr/ffhovsendbtn.png")


def test_ff_default_sendbtn_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.get_by_role("button", name="Wyślać")).to_be_enabled()
    page.screenshot(path="ff_ffpl_scr/ffdefsendbtn.png")


def test_ff_disabled_sendbtn_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.get_by_role("button", name="Wyślać")).to_be_disabled()
    page.screenshot(path="ff_ffpl_scr/ffdissendbtn.png")


def test_ff_send_form_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Test jednostkowy pl")
    page.get_by_placeholder("email@gmail.com").type("unittestpl@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").type("Test jednostkowy pl")
    page.get_by_role("button", name="Wyślać").click()
    page.screenshot(path="ff_ffpl_scr/ffsendf.png")


def test_ff_placeholders_fields_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("placeholder", "Imię")
    expect(page.locator("//input[@id='email']")).to_have_attribute("placeholder", "email@gmail.com")
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("placeholder", "Twoja wiadomość")
    page.get_by_role("heading", name="Formularz zwrotny").click()
    page.screenshot(path="ff_ffpl_scr/ffplacehold.png")