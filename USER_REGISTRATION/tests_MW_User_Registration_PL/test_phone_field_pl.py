import re
from playwright.sync_api import Page, expect


def test_phonepr_valid_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_empty_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Wprowadź numer telefonu")


def test_phonepr_space_field_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Wprowadź numer telefonu")


def test_phonepr_enter_digits_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_enter_value_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_value("+380")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_1char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_2char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_6char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_12char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_13char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_14char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_20char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_сyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_onlyсyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_latin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_onlylatin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_polski_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_onlypolski_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_without_start_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phonepr_onlysymbols_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")

    
def test_phonepr_symbols_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
