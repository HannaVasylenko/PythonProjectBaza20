from playwright.sync_api import Page, expect


def test_name_empty_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Enter your name")


def test_name_space_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type(" ")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Enter your name")


def test_name_1char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("a")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("The name must have at least 2 characters")


def test_name_2char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("au")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_3char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("oon")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_15char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Testdesigncases")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_29char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("TestdesigntechniquesChecklist")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_30char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Testdesigntechniques Checklist")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_31char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Testdesign techniques Checklist")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("The name must not exceed 30 characters")


def test_name_50char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Testdesign techniques Checklist Testcaseautomation")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("The name must not exceed 30 characters")


def test_name_apostrophe_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("T'est'design'techniques")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_hyphen_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("T-est-design-techniques")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_numb_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Testdesign1234567890")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_symbols_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("T_E!S,T.IN?G")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_cyrillic_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Тестування")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_low_case_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("testing")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_up_case_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("TESTING")
    setup_en.get_by_placeholder("Last Name").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")
