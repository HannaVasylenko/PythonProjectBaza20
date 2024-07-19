import re
from playwright.sync_api import Page, expect


def test_ff_mandatory_fields_pl(setup_pl: Page) -> None:
    expect(setup_pl.locator("//label[@for='firstName']")).to_have_text("Imię *")
    expect(setup_pl.locator("//label[@for='email']")).to_have_text("E-mail *")
    expect(setup_pl.locator("//label[@for='message']")).to_have_text("Wiadomość *")
    expect(setup_pl.get_by_role("button", name="Wyślać")).to_be_visible()
    expect(setup_pl.get_by_role("button", name="Wyślać")).to_be_enabled()
    setup_pl.get_by_role("heading", name="Formularz zwrotny").click()


def test_ff_title_fields_pl(setup_pl: Page) -> None:
    expect(setup_pl.locator("//section[@class='ContactFormSection_section__F3_Zu']//h2")).to_have_text("Formularz zwrotny")
    setup_pl.get_by_role("heading", name="Formularz zwrotny").click()


def test_ff_active_sendbtn_fields_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Świętosław")
    setup_pl.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("Twoja wiadomość").type("Świętosław Róża Więcław")
    expect(setup_pl.get_by_role("button", name="Wyślać")).to_be_enabled()


def test_ff_hover_sendbtn_fields_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Wyślać").hover()


def test_ff_default_sendbtn_fields_pl(setup_pl: Page) -> None:
    expect(setup_pl.get_by_role("button", name="Wyślać")).to_be_enabled()


def test_ff_disabled_sendbtn_fields_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").click()
    setup_pl.get_by_placeholder("email@gmail.com").click()
    setup_pl.get_by_placeholder("Twoja wiadomość").click()
    expect(setup_pl.get_by_role("button", name="Wyślać")).to_be_disabled()


def test_ff_send_form_fields_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Test jednostkowy pl")
    setup_pl.get_by_placeholder("email@gmail.com").type("unittestpl@gmail.com")
    setup_pl.get_by_placeholder("Twoja wiadomość").type("Test jednostkowy pl")
    setup_pl.get_by_role("button", name="Wyślać").click()


def test_ff_placeholders_fields_pl(setup_pl: Page) -> None:
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("placeholder", "Imię")
    expect(setup_pl.locator("//input[@id='email']")).to_have_attribute("placeholder", "email@gmail.com")
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("placeholder", "Twoja wiadomość")
    setup_pl.get_by_role("heading", name="Formularz zwrotny").click()
