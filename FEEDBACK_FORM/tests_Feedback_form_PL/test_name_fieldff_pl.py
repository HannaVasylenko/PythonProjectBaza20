import re
from playwright.sync_api import Page, expect


def test_name_empty_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").click()
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz imię")


def test_name_space_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type(" ")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz imię")


def test_name_1char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa musi mieć co najmniej 2 znaki")


def test_name_2char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ęŁ")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_3char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("śćę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_15char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Świętosław Róża")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_29char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ŚwiętosławRóżaWięcławBłażejŁę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_30char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ęŚwiętosławRóżaWięcławBłażejŁę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_31char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ęŚwiętosławRóżaWięcławBłażejŁęł")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")


def test_name_50char_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")


def test_name_apostrophe_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Ś'więt'osław'Róża'Więcław")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_hyphen_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Ś-więtosław-Róża-Więcław")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_lowcase_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("swiętosławóżaięcław")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_upcase_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("ŚŁABC")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_num_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("1234567890Świętosław")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_name_symb_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Ś,w.ię!tos@ław?")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_name_html_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Świętosław&nbsp")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_name_сyrillic_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Степан Андрійович Бандера")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_latin_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Imię").type("Stepan Andriyovych Bandera")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


