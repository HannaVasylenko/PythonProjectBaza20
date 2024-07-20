import re
from playwright.sync_api import Page, expect


def test_phonepr_valid_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_empty_field_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Enter a phone number")


def test_phonepr_space_field_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Enter a phone number")


def test_phonepr_enter_digits_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_enter_value_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_value("+380")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_1char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_2char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_6char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_12char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_13char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_14char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_20char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_сyrillic_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_onlyсyrillic_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_latin_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_onlylatin_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_without_start_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_onlysymbols_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phonepr_symbols_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
