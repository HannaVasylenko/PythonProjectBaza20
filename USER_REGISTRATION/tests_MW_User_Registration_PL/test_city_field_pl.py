import re
from playwright.sync_api import Page, expect


def test_citypr_space_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type(" ")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes") #Wpisz poprawną nazwę miasta no error mes

    
def test_citypr_empty_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").click()
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_1char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("ę")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes >2char") #min char


def test_citypr_2char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("ęł")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_3char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("ęłŻ")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_15char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_29char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("ŻelisławAndrzejŚwiętosławJóze")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_30char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("ŻelisławAndrzejŚwiętosławJózef")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_31char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("ŻelisławAndrzejŚwiętosławJózefę")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Nazwa miasta nie powinna przekraczać 30 znaków")


def test_citypr_50char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("Żelisław Andrzej Świętosław Józef LasławŁukasJózef")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Nazwa miasta nie powinna przekraczać 30 znaków")


def test_citypr_numbers_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("0123456789")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")


def test_citypr_hyphen_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("L-asław-Łukas-Józef")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_apostrophe_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("L'asław'Łukas'Józef")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_space_in_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("Lasław Łukas Józef")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_symbols_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("An!dr.zejŚwi,ętosła?w")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Wpisz poprawną nazwę miasta")


def test_citypr_сyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("Харків")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_up_case_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("LASŁAW")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_low_case_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("dołączdoprojektu")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")

    
def test_citypr_latin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Kijów").type("Kharkiv")
    setup_pl.get_by_placeholder("Ukraina").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")

