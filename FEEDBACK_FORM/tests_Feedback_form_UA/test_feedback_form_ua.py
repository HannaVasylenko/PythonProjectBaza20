import re
from playwright.sync_api import Page, expect


def test_ff_mandatory_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//label[@for='firstName']")).to_have_text("Ім’я *")
    expect(page.locator("//label[@for='email']")).to_have_text("Електронна пошта *")
    expect(page.locator("//label[@for='message']")).to_have_text("Повідомлення *")
    expect(page.get_by_role("button", name="Відправити")).to_be_visible()
    expect(page.get_by_role("button", name="Відправити")).to_be_enabled()
    page.get_by_role("heading", name="Форма зворотного зв’язку").click()
    page.screenshot(path="ff_ffua_scr/ffmandatory.png")


def test_ff_title_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//section[@class='ContactFormSection_section__F3_Zu']//h2")).to_have_text("Форма зворотного зв’язку")
    page.get_by_role("heading", name="Форма зворотного зв’язку").click()
    page.screenshot(path="ff_ffua_scr/fftitle.png")


def test_ff_active_sendbtn_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Степан Андрійович Бандера")
    page.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").type("Тестове повідомлення")
    expect(page.get_by_role("button", name="Відправити")).to_be_enabled()
    page.screenshot(path="ff_ffua_scr/ffactsendbtn.png")


def test_ff_hover_sendbtn_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Відправити").hover()
    page.screenshot(path="ff_ffua_scr/ffhovsendbtn.png")


def test_ff_default_sendbtn_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.get_by_role("button", name="Відправити")).to_be_enabled()
    page.screenshot(path="ff_ffua_scr/ffdefsendbtn.png")


def test_ff_disabled_sendbtn_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("Ваше повідомлення").click()
    page.get_by_role("button", name="Відправити")
    expect(page.get_by_role("button", name="Відправити")).to_be_disabled()
    page.screenshot(path="ff_ffua_scr/ffdissendbtn.png")


def test_ff_send_form_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Юніт тест юа")
    page.get_by_placeholder("email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").type("Тестове повідомлення в юніт тесті юа")
    page.get_by_role("button", name="Відправити").click()
    page.screenshot(path="ff_ffua_scr/ffsendf.png")


def test_ff_placeholders_fields(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("placeholder", "Ім’я")
    expect(page.locator("//input[@id='email']")).to_have_attribute("placeholder", "email@gmail.com")
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("placeholder", "Ваше повідомлення")
    page.get_by_role("heading", name="Форма зворотного зв’язку").click()
    page.screenshot(path="ff_ffua_scr/ffplacehold.png")