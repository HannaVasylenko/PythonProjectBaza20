from playwright.sync_api import Page, expect


def test_name_empty_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter a name")


def test_name_space_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type(" ")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter a name")


def test_name_1char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("a")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must have at least 2 characters")


def test_name_2char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("au")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_3char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("oon")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_15char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Testdesigncaseu")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_29char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Testdesign techniquestestcase")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_30char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("testdesign techniquestestcasee")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_31char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Tstdesign techniquestestcaseENG")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")


def test_name_50char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("TestdesigntechniquestestcaseChecklistTemplatesTest")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")


def test_name_apostrophe_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("T'est'design'techniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_hyphen_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("T-est-design-techniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_low_case_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("testdesigntechniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_up_case_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("TESTING")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_numb_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("1234567890designtechniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_symb_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("T.es,t!design@techni?ques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_html_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Test&nbsp")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")


def test_name_cyrillic_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Степан Андрійович Бандера")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_polski_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Świętosław Lasław Łukasz")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


