import re
from playwright.sync_api import Page, expect


def test_countrypr_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type(" ")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju") #no error mes
    page.screenshot(path="countryprpl_screenshots/countryspace.png")


def test_countrypr_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").click()
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countryempty.png")


def test_countrypr_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ę")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju") #incorrect error mes
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="countryprpl_screenshots/country1char.png")


def test_countrypr_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ęł")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju") #incorrect error mes
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="countryprpl_screenshots/country2char.png")


def test_countrypr_3char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ęłŻ")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju") #incorrect error mes
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="countryprpl_screenshots/country3char.png")


def test_countrypr_4char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ęłŻó")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/country4char.png")


def test_countrypr_5char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ęłŻóż")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/country5char.png")


def test_countrypr_15char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ŚwiętosławJózef")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/country15char.png")


def test_countrypr_29char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("AndrzejŚwiętosławLasławŁukasz")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/country29char.png")


def test_countrypr_30char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("Andrzej ŚwiętosławLasławŁukasz")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/country30char.png")


def test_countrypr_31char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("Andrzej Świętosław LasławŁukasz")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Nazwa kraju nie powinna przekraczać 30 znaków")
    page.screenshot(path="countryprpl_screenshots/country31char.png")


def test_countrypr_50char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("AndrzejŚwiętosławLasławŁukaszBożenaJózefŚwiętosław")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Nazwa kraju nie powinna przekraczać 30 znaków")
    page.screenshot(path="countryprpl_screenshots/country50char.png")


def test_countrypr_numbers_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("1234567890")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/countrynumbers.png")


def test_countrypr_hyphen_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("B-ożena-Józef-Świętosław")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countryhyphen.png")


def test_countrypr_apostrophe_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("B'ożena'Józef'Świętosła'w")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countryapostrophe.png")


def test_countrypr_space_in_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("Bożena Józef Świętosław")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countryspacein.png")


def test_countrypr_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("B@oż?ena.Józef,Świętosław")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/countrysymbols.png")


def test_countrypr_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("Україна")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countryсyrillic.png")


def test_countrypr_latin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("Ukraine")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countrylatin.png")


def test_countrypr_upcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("ŁŚABCDE")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countryupcase.png")


def test_countrypr_lowcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Ukraina").type("żśćóżęł")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprpl_screenshots/countrylowcase.png")


def test_countrypr_piletters_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()

    page.get_by_placeholder("Ukraina").press("Control+A")
    page.get_by_placeholder("Ukraina").press("Delete")
    page.get_by_placeholder("Ukraina").type("Пръерплрт")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/country1piletters.png")

    page.get_by_placeholder("Ukraina").press("Control+A")
    page.get_by_placeholder("Ukraina").press("Delete")
    page.get_by_placeholder("Ukraina").type("Орамыьтор")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/country2piletters.png")

    page.get_by_placeholder("Ukraina").press("Control+A")
    page.get_by_placeholder("Ukraina").press("Delete")
    page.get_by_placeholder("Ukraina").type("апмЭтиор")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/country3piletters.png")

    page.get_by_placeholder("Ukraina").press("Control+A")
    page.get_by_placeholder("Ukraina").press("Delete")
    page.get_by_placeholder("Ukraina").type("потлоЁьтбоа")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/country4piletters.png")

    page.get_by_placeholder("Ukraina").press("Control+A")
    page.get_by_placeholder("Ukraina").press("Delete")
    page.get_by_placeholder("Ukraina").type("Тиитрэтьтор")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/country5piletters.png")

    page.get_by_placeholder("Ukraina").press("Control+A")
    page.get_by_placeholder("Ukraina").press("Delete")
    page.get_by_placeholder("Ukraina").type("Иимпаётир")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    page.screenshot(path="countryprpl_screenshots/country6piletters.png")