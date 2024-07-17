import re
from playwright.sync_api import Page, expect


def test_name_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).click()
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter your name")
    page.screenshot(path="name_mentoren_scr/nameempty.png")


def test_name_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type(" ")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter your name")
    page.screenshot(path="name_mentoren_scr/namespace.png")


def test_name_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("a")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must have at least 2 characters")
    page.screenshot(path="name_mentoren_scr/name1char.png")


def test_name_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("au")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/name2char.png")


def test_name_3char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("oon")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/name3char.png")


def test_name_15char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("Testdesigncases")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/name15char.png")


def test_name_29char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("TestdesigntechniquesChecklist")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/name29char.png")


def test_name_30char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("Testdesigntechniques Checklist")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/name30char.png")


def test_name_31char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("Testdesign techniques Checklist")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")
    page.screenshot(path="name_mentoren_scr/name31char.png")


def test_name_50char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("Testdesign techniques Checklist Testcaseautomation")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")
    page.screenshot(path="name_mentoren_scr/name50char.png")


def test_name_apostrophe_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("T'est'design'techniques")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/nameapostrophe.png")


def test_name_hyphen_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("T-est-design-techniques")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/namehyphen.png")


def test_name_numb_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("Testdesign1234567890")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")
    page.screenshot(path="name_mentoren_scr/namenumb.png")


def test_name_symbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("T_E!S,T.IN?G")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")
    page.screenshot(path="name_mentoren_scr/namesymbols.png")


def test_name_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("Тестування")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/nameсyrillic.png")


def test_name_low_case_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("testing")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/namelcase.png")


def test_name_upcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_role("textbox", name="First Name", exact=True).type("TESTING")
    page.get_by_placeholder("Last Name").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentoren_scr/nameupcase.png")