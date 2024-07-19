import re
from playwright.sync_api import Page, expect


def test_name_empty_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter a name")


def test_name_space_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type(" ")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter a name")


def test_name_1char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("a")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must have at least 2 characters")


def test_name_2char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("au")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_3char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("oon")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_15char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Testdesigncaseu")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_29char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Testdesign techniquestestcase")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_30char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("testdesign techniquestestcasee")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_31char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Tstdesign techniquestestcaseENG")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")


def test_name_50char_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("TestdesigntechniquestestcaseChecklistTemplatesTest")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")


def test_name_apostrophe_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("T'est'design'techniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_hyphen_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("T-est-design-techniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_lowcase_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("testdesigntechniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_upcase_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("TESTING")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_num_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("1234567890designtechniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_symb_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("T.es,t!design@techni?ques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_html_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Test&nbsp")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_сyrillic_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Степан Андрійович Бандера")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_polski_field_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Świętosław Lasław Łukasz")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


