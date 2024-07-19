import re
from playwright.sync_api import Page, expect


def test_name_empty_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz swoje imię")


def test_name_space_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type(" ")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz swoje imię")


def test_name_1char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("ę")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa musi mieć co najmniej 2 znaki")


def test_name_2char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("ęŁ")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_3char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("ęŁŚ")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_15char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("ŚwiętosławLasła")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_29char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("ŚwiętosławLasławJózefBożenapl")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_30char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław LasławJózefBożenapl")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_31char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Lasław JózefBożenapl")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")


def test_name_50char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Lasław JózefBożena WięcławŁódźChwalibóg")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")


def test_name_apostrophe_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("W'ięcław'Łódź'Chwalibóg")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_hyphen_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("W-ięcław-Łódź-Chwalibóg")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_numb_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("12345Więcław67890")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę wpisać prawidłowe imię")


def test_name_symbols_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("W_i!ę@cł?awŁ.ód,ź")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę wpisać prawidłowe imię")


def test_name_сyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Тестування")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_latin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Testing")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_low_case_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("więtosław")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_upcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("ŚŁTESTING")
    setup_pl.get_by_placeholder("Nazwisko").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
