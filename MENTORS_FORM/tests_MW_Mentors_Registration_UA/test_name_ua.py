import re
from playwright.sync_api import Page, expect


def test_name_empty_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть своє ім’я")
    page.screenshot(path="name_mentorua_scr/nameempty.png")


def test_name_space_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type(" ")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть своє ім’я")
    page.screenshot(path="name_mentorua_scr/namespace.png")


def test_name_1char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("ї")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")
    page.screenshot(path="name_mentorua_scr/name1char.png")


def test_name_2char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("їє")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/name2char.png")


def test_name_3char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("їєа")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/name3char.png")


def test_name_15char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Шухевич Роман О")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/name15char.png")


def test_name_29char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Степан Андрійович Бандера ОУН")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/name29char.png")


def test_name_30char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("степан андрійович бандераоун-б")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/name30char.png")


def test_name_31char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Степан Андрійович Бандера ОУН-Б")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")
    page.screenshot(path="name_mentorua_scr/name31char.png")


def test_name_50char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Степан Бандера Коновалець Євген Шухевич Романдіячі")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")
    page.screenshot(path="name_mentorua_scr/name50char.png")


def test_name_apostrophe_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("С'тепан'Андрійович'Бандера")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/nameapostrophe.png")


def test_name_hyphen_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("С-тепан-Андрійович-Бандера")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/namehyphen.png")


def test_name_numb_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("СтепанБандера1234567890")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/namenumb.png")


def test_name_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("С.теп@н,Бандер*а!")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/namesymbols.png")


def test_name_latin_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Stepan Andriyovych Bandera")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/namelatin.png")


def test_name_low_case_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("тестування")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/namelcase.png")


def test_name_up_case_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("ТЕСТУВАННЯ")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/nameupcase.png")


def test_name_spacein_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Техніки тест дизайну")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_mentorua_scr/namespacein.png")


def test_name_piletters_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()

    page.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    page.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Пръерплрт")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/name1piletters.png")

    page.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    page.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Орамыьтор")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/name2piletters.png")

    page.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    page.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    page.get_by_role("textbox", name="Ім’я", exact=True).type("апмЭтиор")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/name3piletters.png")

    page.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    page.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    page.get_by_role("textbox", name="Ім’я", exact=True).type("потлоЁьтбоа")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/name4piletters.png")

    page.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    page.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Тиитрэтьтор")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/name5piletters.png")

    page.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    page.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Иимпаётир")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_mentorua_scr/name6piletters.png")