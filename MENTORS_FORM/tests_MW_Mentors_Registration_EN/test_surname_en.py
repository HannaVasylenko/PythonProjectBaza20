import re
from playwright.sync_api import Page, expect


def test_surname_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter your last name")


def test_surname_space_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type(" ")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter your last name")


def test_surname_1char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("a")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("The last name must have at least 2 characters")


def test_surname_2char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("au")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_3char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("oon")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_25char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("ChecklistTemplatesTestcas")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_49char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("Testdesigntechniques Checklist Testcaseautomation")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_50char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("Testdesign techniques Checklist Testcaseautomation")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_51char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("Testdesign techniques Checklist Testcase automation")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("The last name must not exceed 50 characters")


def test_surname_76char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("Testdesign techniques Checklist Test case automation eng Checklist Templates")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("The last name must not exceed 50 characters")


def test_surname_apostrophe_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("T'est'design'techniques")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_hyphen_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("T-est-design-techniques")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_numb_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("Testdesign1234567890")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter the correct Surname")


def test_surname_symbols_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("T.est,design_tec?hniqu!es")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter the correct Surname")


def test_surname_сyrillic_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("Тестування")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_low_case_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("testing")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_upcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("TESTING")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surname_space_in_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Last Name").type("testing testing testing")
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
