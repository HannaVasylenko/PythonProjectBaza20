import re
from playwright.sync_api import Page, expect


def test_citypr_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type(" ")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes") #Wpisz poprawną nazwę miasta no error mes
    page.screenshot(path="cityprpl_screenshots/cityspace.png")
    
    
def test_citypr_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").click()
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/cityemptyr.png")


def test_citypr_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("ę")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes >2char") #min char
    page.screenshot(path="cityprpl_screenshots/city1char.png")


def test_citypr_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("ęł")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/city2char.png")


def test_citypr_3char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("ęłŻ")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/city3char.png")


def test_citypr_15char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/city15char.png")


def test_citypr_29char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("ŻelisławAndrzejŚwiętosławJóze")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/city29char.png")


def test_citypr_30char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("ŻelisławAndrzejŚwiętosławJózef")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/city30char.png")


def test_citypr_31char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("ŻelisławAndrzejŚwiętosławJózefę")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Nazwa miasta nie powinna przekraczać 30 znaków")
    page.screenshot(path="cityprpl_screenshots/city31char.png")


def test_citypr_50char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("Żelisław Andrzej Świętosław Józef LasławŁukasJózef")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Nazwa miasta nie powinna przekraczać 30 znaków")
    page.screenshot(path="cityprpl_screenshots/city50char.png")


def test_citypr_numbers_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("0123456789")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/citynumbers.png")


def test_citypr_hyphen_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("L-asław-Łukas-Józef")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/cityhyphen.png")


def test_citypr_apostrophe_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("L'asław'Łukas'Józef")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/cityapostrophe.png")


def test_citypr_space_in_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("Lasław Łukas Józef")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/cityspacein.png")


def test_citypr_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("An!dr.zejŚwi,ętosła?w")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/citysymbols.png")


def test_citypr_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("Харків")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/cityсyrillic.png")


def test_citypr_up_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("LASŁAW")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/cityupcase.png")


def test_citypr_low_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("dołączdoprojektu")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/citylowcase.png")
    
    
def test_citypr_latin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Kijów").type("Kharkiv")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprpl_screenshots/citylatin.png")
    
    
def test_citypr_piletters_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()

    page.get_by_placeholder("Kijów").press("Control+A")
    page.get_by_placeholder("Kijów").press("Delete")
    page.get_by_placeholder("Kijów").type("Пръерплрт")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/city1piletters.png")

    page.get_by_placeholder("Kijów").press("Control+A")
    page.get_by_placeholder("Kijów").press("Delete")
    page.get_by_placeholder("Kijów").type("Орамыьтор")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/city2piletters.png")

    page.get_by_placeholder("Kijów").press("Control+A")
    page.get_by_placeholder("Kijów").press("Delete")
    page.get_by_placeholder("Kijów").type("апмЭтиор")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/city3piletters.png")

    page.get_by_placeholder("Kijów").press("Control+A")
    page.get_by_placeholder("Kijów").press("Delete")
    page.get_by_placeholder("Kijów").type("потлоЁьтбоа")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/city4piletters.png")

    page.get_by_placeholder("Kijów").press("Control+A")
    page.get_by_placeholder("Kijów").press("Delete")
    page.get_by_placeholder("Kijów").type("Тиитрэтьтор")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/city5piletters.png")

    page.get_by_placeholder("Kijów").press("Control+A")
    page.get_by_placeholder("Kijów").press("Delete")
    page.get_by_placeholder("Kijów").type("Иимпаётир")
    page.get_by_placeholder("Ukraina").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    page.screenshot(path="cityprpl_screenshots/city6piletters.png")