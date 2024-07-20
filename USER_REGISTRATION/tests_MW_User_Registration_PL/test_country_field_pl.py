import re
from playwright.sync_api import Page, expect


def test_countrypr_space_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type(" ")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju") #no error mes


def test_countrypr_empty_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").click()
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_1char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ę")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char")


def test_countrypr_2char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęł")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char")


def test_countrypr_3char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęłŻ")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char")


def test_countrypr_4char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęłŻó")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_5char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęłŻóż")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_15char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ŚwiętosławJózef")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_29char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("AndrzejŚwiętosławLasławŁukasz")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_30char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Andrzej ŚwiętosławLasławŁukasz")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_31char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Andrzej Świętosław LasławŁukasz")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Nazwa kraju nie powinna przekraczać 30 znaków")


def test_countrypr_50char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("AndrzejŚwiętosławLasławŁukaszBożenaJózefŚwiętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Nazwa kraju nie powinna przekraczać 30 znaków")


def test_countrypr_numbers_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("1234567890")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")


def test_countrypr_hyphen_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("B-ożena-Józef-Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_apostrophe_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("B'ożena'Józef'Świętosła'w")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_space_in_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Bożena Józef Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_symbols_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("B@oż?ena.Józef,Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")


def test_countrypr_сyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Україна")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_latin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Ukraine")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_upcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ŁŚABCDE")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_lowcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("żśćóżęł")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")

