import re
from playwright.sync_api import Page, expect


def test_surname_1_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ę")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Nazwisko musi mieć co najmniej 2 znaki")
    page.screenshot(path="surnamepl_screenshots/surname1char.png")


def test_surname_empty_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").click()
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz swoje nazwisko")
    page.screenshot(path="surnamepl_screenshots/surnameemptyfield.png")


def test_surname_2_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ęł")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surname2char.png")


def test_surname_3_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ęłŻ")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surname3char.png")


def test_surname_25_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ŻelisławAndrzejBożenJózef")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surname25char.png")


def test_surname_49_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ŻelisławAndrzejBożenaJózefaLasławŁukaszŚwiętosław")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surname49char.png")


def test_surname_50_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ŻelisławAndrzejBożenaJózefaLasławŁukaszŚwiętosława")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surname50char.png")


def test_surname_51_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ŻelisławAndrzejBożenaJózefaLasławŁukaszŚwiętosławas")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Nazwisko nie może przekraczać 50 znaków")
    page.screenshot(path="surnamepl_screenshots/surname51char.png")


def test_surname_70_char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("ŻelisławAndrzejBożenaJózefaLasławŁukasŚwiętosławJózefaLasławŚwiętosław")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Nazwisko nie może przekraczać 50 znaków")
    page.screenshot(path="surnamepl_screenshots/surname70char.png")


def test_surname_apostrophe_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("Ż'elis'ławAndrze'j")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surnameapostrophe.png")


def test_surname_hyphen_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("B-ożena-Józef")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surnamehyphen.png")


def test_surname_space_in_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("Bożena Józef")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class","InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surnamespacein.png")


def test_surname_up_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("BOŚŁTEST")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class","InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surnameupcase.png")


def test_surname_low_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("więcławbłaż")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class","InputField_input___Wj0m")
    page.screenshot(path="surnamepl_screenshots/surnamelowcase.png")


def test_surname_numbers_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("Łukas12345Świętosław67890")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz poprawne nazwisko")
    page.screenshot(path="surnamepl_screenshots/surnamenumbers.png")


def test_surname_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type("Że.lis,ław!Andr:zej")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz poprawne nazwisko")
    page.screenshot(path="surnamepl_screenshots/surnamesymbols.png")


def test_surname_only_spce_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Nazwisko").type(" ")
    page.get_by_placeholder("Imię").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz swoje nazwisko")
    page.screenshot(path="surnamepl_screenshots/surnameonlyspace.png")
