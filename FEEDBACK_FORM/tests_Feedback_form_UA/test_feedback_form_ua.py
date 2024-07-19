import re
from playwright.sync_api import Page, expect


def test_ff_mandatory_fields(setup: Page) -> None:
    expect(setup.locator("//label[@for='firstName']")).to_have_text("Ім’я *")
    expect(setup.locator("//label[@for='email']")).to_have_text("Електронна пошта *")
    expect(setup.locator("//label[@for='message']")).to_have_text("Повідомлення *")
    expect(setup.get_by_role("button", name="Відправити")).to_be_visible()
    expect(setup.get_by_role("button", name="Відправити")).to_be_enabled()
    setup.get_by_role("heading", name="Форма зворотного зв’язку").click()


def test_ff_title_fields(setup: Page) -> None:
    expect(setup.locator("//section[@class='ContactFormSection_section__F3_Zu']//h2")).to_have_text("Форма зворотного зв’язку")
    setup.get_by_role("heading", name="Форма зворотного зв’язку").click()


def test_ff_active_sendbtn_fields(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Степан Андрійович Бандера")
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").type("Тестове повідомлення")
    expect(setup.get_by_role("button", name="Відправити")).to_be_enabled()


def test_ff_hover_sendbtn_fields(setup: Page) -> None:
    setup.get_by_role("button", name="Відправити").hover()


def test_ff_default_sendbtn_fields(setup: Page) -> None:
    expect(setup.get_by_role("button", name="Відправити")).to_be_enabled()


def test_ff_disabled_sendbtn_fields(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").click()
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("Ваше повідомлення").click()
    setup.get_by_role("button", name="Відправити")
    expect(setup.get_by_role("button", name="Відправити")).to_be_disabled()


def test_ff_send_form_fields(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Юніт тест юа")
    setup.get_by_placeholder("email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").type("Тестове повідомлення в юніт тесті юа")
    setup.get_by_role("button", name="Відправити").click()


def test_ff_placeholders_fields(setup: Page) -> None:
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("placeholder", "Ім’я")
    expect(setup.locator("//input[@id='email']")).to_have_attribute("placeholder", "email@gmail.com")
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("placeholder", "Ваше повідомлення")
    setup.get_by_role("heading", name="Форма зворотного зв’язку").click()
