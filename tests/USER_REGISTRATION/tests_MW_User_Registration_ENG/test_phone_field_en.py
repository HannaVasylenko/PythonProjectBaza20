import re
from playwright.sync_api import Page, expect


def test_phone_valid_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_phone_empty_field_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Enter a phone number")


def test_phone_space_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Enter a phone number")


def test_phone_enter_digits_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_phone_enter_value_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_value("+380")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_1char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_2char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_6char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_12char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_13char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_phone_14char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_20char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_cyrillic_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_only_cyrillic_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_latin_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_only_latin_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_without_start_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_only_symbols_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")


def test_phone_symbols_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Please enter a valid phone number")
