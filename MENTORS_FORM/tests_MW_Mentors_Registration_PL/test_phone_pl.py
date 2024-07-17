import re
from playwright.sync_api import Page, expect


def test_phone_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Wprowadź numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phoneempty.png")


def test_phone_with_begin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phonewithbegin.png")


def test_phone_valid_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phone_mentorpl_scr/phonevalid.png")


def test_phone_enter_num_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phone_mentorpl_scr/phoneenternum.png")


def test_phone_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phone1char.png")


def test_phone_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phone2char.png")


def test_phone_6char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phone6char.png")


def test_phone_12char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12345678")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phone12char.png")


def test_phone_13char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phone_mentorpl_scr/phone13char.png")


def test_phone_14char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phone14char.png")


def test_phone_20char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999123456")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phone20char.png")


def test_phone_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phoneсyrillic.png")


def test_phone_latin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phonelatin.png")


def test_phone_polski_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("Świętosław")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phonepolski.png")


def test_phone_symb_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phonesymb.png")


def test_phone_without_begin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1234567890123")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phone_mentorpl_scr/phonewithoutbegin.png")

