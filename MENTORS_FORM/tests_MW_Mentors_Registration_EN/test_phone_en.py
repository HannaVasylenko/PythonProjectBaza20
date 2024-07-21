import re
from playwright.sync_api import Page, expect


def test_phone_empty_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Enter a phone number")


def test_phone_with_begin_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_valid_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phone_enter_numb_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phone_1char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_2char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_6char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_12char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12345678")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_13char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phone_14char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_20char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("9999999999123456")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_cyrillic_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_latin_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_symb_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_without_begin_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("1234567890123")
    setup_en.locator("//input[@id='discord']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")

