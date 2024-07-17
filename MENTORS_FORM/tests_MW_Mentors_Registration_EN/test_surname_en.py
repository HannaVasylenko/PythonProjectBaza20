import re
from playwright.sync_api import Page, expect


def test_surname_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").click()
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter your last name")
    page.screenshot(path="surname_mentoren_scr/surnameempty.png")


def test_surname_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type(" ")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter your last name")
    page.screenshot(path="surname_mentoren_scr/surnamespace.png")


def test_surname_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("a")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("The last name must have at least 2 characters")
    page.screenshot(path="surname_mentoren_scr/surname1char.png")


def test_surname_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("au")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surname2char.png")


def test_surname_3char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("oon")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surname3char.png")


def test_surname_25char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("ChecklistTemplatesTestcas")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surname25char.png")


def test_surname_49char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("Testdesigntechniques Checklist Testcaseautomation")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surname49char.png")


def test_surname_50char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("Testdesign techniques Checklist Testcaseautomation")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surname50char.png")


def test_surname_51char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("Testdesign techniques Checklist Testcase automation")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("The last name must not exceed 50 characters")
    page.screenshot(path="surname_mentoren_scr/surname51char.png")


def test_surname_76char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("Testdesign techniques Checklist Test case automation eng Checklist Templates")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("The last name must not exceed 50 characters")
    page.screenshot(path="surname_mentoren_scr/surname76char.png")


def test_surname_apostrophe_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("T'est'design'techniques")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surnameapostrophe.png")


def test_surname_hyphen_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("T-est-design-techniques")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surnamehyphen.png")


def test_surname_numb_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("Testdesign1234567890")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter the correct Surname")
    page.screenshot(path="surname_mentoren_scr/surnamenumb.png")


def test_surname_symbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("T.est,design_tec?hniqu!es")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Enter the correct Surname")
    page.screenshot(path="surname_mentoren_scr/surnamesymbols.png")


def test_surname_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("Тестування")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surnameсyrillic.png")


def test_surname_low_case_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("testing")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surnamelcase.png")


def test_surname_upcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("TESTING")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surnameupcase.png")


def test_surname_space_in_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Last Name").type("testing testing testing")
    page.get_by_role("textbox", name="First Name", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentoren_scr/surnamespacein.png")