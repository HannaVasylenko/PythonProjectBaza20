import re
from playwright.sync_api import Page, expect


def test_namepr_1_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("ї")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")
    page.screenshot(path="nameprua_screenshots/name1char.png")


def test_namepr_empty_field_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").click()
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть своє ім’я")
    page.screenshot(path="nameprua_screenshots/nameemptyfield.png")


def test_namepr_2_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("їє")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/name2char.png")


def test_namepr_3_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("їєа")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/name3char.png")


def test_namepr_15_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Технікитестдиза")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/name15char.png")


def test_namepr_29_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Техніки тест дизайну чеклісти")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/name29char.png")


def test_namepr_30_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Техніки тест дизайну чеклістів")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/name30char.png")


def test_namepr_31_char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Техніки тестдизайну чеклістівюа")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")
    page.screenshot(path="nameprua_screenshots/name31char.png")


def test_namepr_50_cha_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Технікитестдизайну чеклисти дефектрепортитесткейси")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")
    page.screenshot(path="nameprua_screenshots/name50char.png")


def test_namepr_apostrophe_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Т'ехніки'тест'дизайну")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/nameapostrophe.png")


def test_namepr_hyphen_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Т-ехніки-тест-дизайну")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/namehyphen.png")


def test_namepr_space_in_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Техніки тест дизайну")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/namespacein.png")


def test_namepr_low_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("технікитестдизайну")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/namelowcase.png")


def test_namepr_up_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("ТЕСТУВАННЯ")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="nameprua_screenshots/nameupcase.png")


def test_namepr_numbers_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Технікитестдизайну1234567890")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/namenumbers.png")


def test_namepr_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Т,е.хн?іки!те@ст")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/namesymbols.png")


def test_namepr_piletters_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Пръерплрт")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/name1piletters.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Орамыьтор")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/name2piletters.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("апмЭтиор")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/name3piletters.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("потлоЁьтбоа")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/name4piletters.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Тиитрэтьтор")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/name5piletters.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Иимпаётир")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="nameprua_screenshots/name6piletters.png")


def test_namepr_only_space_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type(" ")
    page.get_by_placeholder("Прізвище").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть своє ім’я")
    page.screenshot(path="nameprua_screenshots/nameonlyspace.png")
