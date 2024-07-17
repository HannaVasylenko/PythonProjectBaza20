import re
from playwright.sync_api import Page, expect


def test_name_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).click()
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz swoje imię")
    page.screenshot(path="name_mentorpl_scr/nameempty.png")


def test_name_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type(" ")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz swoje imię")
    page.screenshot(path="name_mentorpl_scr/namespace.png")


def test_name_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("ę")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa musi mieć co najmniej 2 znaki")
    page.screenshot(path="name_mentorpl_scr/name1char.png")


def test_name_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("ęŁ")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/name2char.png")


def test_name_3char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("ęŁŚ")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/name3char.png")


def test_name_15char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("ŚwiętosławLasła")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/name15char.png")


def test_name_29char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("ŚwiętosławLasławJózefBożenapl")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/name29char.png")


def test_name_30char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("Świętosław LasławJózefBożenapl")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/name30char.png")


def test_name_31char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Lasław JózefBożenapl")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")
    page.screenshot(path="name_mentorpl_scr/name31char.png")


def test_name_50char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Lasław JózefBożena WięcławŁódźChwalibóg")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")
    page.screenshot(path="name_mentorpl_scr/name50char.png")


def test_name_apostrophe_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("W'ięcław'Łódź'Chwalibóg")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/nameapostrophe.png")


def test_name_hyphen_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("W-ięcław-Łódź-Chwalibóg")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/namehyphen.png")


def test_name_numb_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("12345Więcław67890")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę wpisać prawidłowe imię")
    page.screenshot(path="name_mentorpl_scr/namenumb.png")


def test_name_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("W_i!ę@cł?awŁ.ód,ź")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę wpisać prawidłowe imię")
    page.screenshot(path="name_mentorpl_scr/namesymbols.png")


def test_name_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("Тестування")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/nameсyrillic.png")


def test_name_latin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("Testing")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/namelatin.png")


def test_name_low_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("więtosław")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/namelcase.png")


def test_name_upcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="Imię", exact=True).type("ŚŁTESTING")
    page.get_by_placeholder("Nazwisko").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorpl_scr/nameupcase.png")