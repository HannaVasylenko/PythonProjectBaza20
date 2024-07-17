import re
from playwright.sync_api import Page, expect


def test_name_empty_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter a name")
    page.screenshot(path="name_ffen_scr/nameemptyf.png")


def test_name_space_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type(" ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Enter a name")
    page.screenshot(path="name_ffen_scr/namespacef.png")


def test_name_1char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("a")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must have at least 2 characters")
    page.screenshot(path="name_ffen_scr/name1charf.png")


def test_name_2char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("au")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/name2charf.png")


def test_name_3char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("oon")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/name2charf.png")


def test_name_15char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Testdesigncaseu")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/name15charf.png")


def test_name_29char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Testdesign techniquestestcase")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/name29charf.png")


def test_name_30char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("testdesign techniquestestcasee")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/name30charf.png")


def test_name_31char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Tstdesign techniquestestcaseENG")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")
    page.screenshot(path="name_ffen_scr/name31charf.png")


def test_name_50char_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("TestdesigntechniquestestcaseChecklistTemplatesTest")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("The name must not exceed 30 characters")
    page.screenshot(path="name_ffen_scr/name50charf.png")


def test_name_apostrophe_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("T'est'design'techniques")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/nameapostrophef.png")


def test_name_hyphen_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("T-est-design-techniques")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/namehyphenf.png")


def test_name_lowcase_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("testdesigntechniques")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/namelowcasef.png")


def test_name_upcase_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("TESTING")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/nameupcasef.png")


def test_name_num_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("1234567890designtechniques")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")
    page.screenshot(path="name_ffen_scr/namenumf.png")


def test_name_symb_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("T.es,t!design@techni?ques")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")
    page.screenshot(path="name_ffen_scr/namesymbf.png")


def test_name_html_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Test&nbsp")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Please enter a valid name")
    page.screenshot(path="name_ffen_scr/namehtmlf.png")


def test_name_сyrillic_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Степан Андрійович Бандера")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/nameсyrillicf.png")


def test_name_polski_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Name").type("Świętosław Lasław Łukasz")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffen_scr/namepolskif.png")


