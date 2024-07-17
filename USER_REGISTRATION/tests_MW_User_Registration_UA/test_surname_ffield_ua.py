import re
from playwright.sync_api import Page, expect


def test_surnamepr_1char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("ї")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно мати не менше 2 знаків")
    page.screenshot(path="surnameprua_screenshots/surname1char.png")


def test_surnamepr_empty_field_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").click()
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть своє прізвище")
    page.screenshot(path="surnameprua_screenshots/surnameemptyfield.png")


def test_surnamepr_2char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("їє")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surname2char.png")


def test_surnamepr_3char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("їєа")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surname3char.png")


def test_surnamepr_25char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Технікитестдизайнучекліст")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surname25char.png")


def test_surnamepr_49char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсию")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surname49char.png")


def test_surnamepr_50char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсиюа")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surname50char.png")


def test_surnamepr_51char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсиюаю")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")
    page.screenshot(path="surnameprua_screenshots/surname51char.png")


def test_surnamepr_70char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсиюайцукенгшщзфівапролдї")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")
    page.screenshot(path="surnameprua_screenshots/surname70char.png")


def test_surnamepr_apostrophe_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Т'ехніки'тест'дизайну")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surnameapostrophe.png")


def test_surnamepr_hyphen_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Т-ехніки-тест-дизайну")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surnamehyphen.png")


def test_surnamepr_space_in_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Техніки тест дизайну")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surnamespacein.png")


def test_surnamepr_low_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("технікитестдизайну")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surnamelowcase.png")


def test_surnamepr_up_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("ТЕХНІКИТЕСТДИЗАЙНУ")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnameprua_screenshots/surnameupcase.png")


def test_surnamepr_numbers_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Технікитестдизайну1234567890")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище") #last name
    page.screenshot(path="surnameprua_screenshots/surnamenumbers.png")


def test_surnamepr_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type("Т.ех,ні!ките@стдиз_айну")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище") #last name
    page.screenshot(path="surnameprua_screenshots/surnamesymbols.png")


def test_surnamepr_only_spce_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Прізвище").type(" ")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть своє прізвище")
    page.screenshot(path="surnameprua_screenshots/surnameonlyspace.png")


def test_surnamepr_piletters_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Пръерплрт")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище") #last name
    page.screenshot(path="surnameprua_screenshots/surnamepiletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Орамыьтор")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")  # last name
    page.screenshot(path="surnameprua_screenshots/surnamepiletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("апмЭтиор")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")  # last name
    page.screenshot(path="surnameprua_screenshots/surnamepiletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("потлоЁьтбоа")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")  # last name
    page.screenshot(path="surnameprua_screenshots/surnamepiletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Тиитрэтьтор")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")  # last name
    page.screenshot(path="surnameprua_screenshots/surnamepiletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Иимпаётир")
    page.get_by_placeholder("Ім’я").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")  # last name
    page.screenshot(path="surnameprua_screenshots/surnamepiletters.png")








