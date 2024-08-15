from playwright.sync_api import Page, expect


def test_country_space_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type(" ")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")


def test_country_empty_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").click()
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_1char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ę")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("error mes >4char")


def test_country_2char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęł")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("error mes >4char")


def test_country_3char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęłŻ")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("error mes >4char")


def test_country_4char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęłŻó")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_5char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ęłŻóż")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_15char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ŚwiętosławJózef")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_29char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("AndrzejŚwiętosławLasławŁukasz")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_30char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Andrzej ŚwiętosławLasławŁukasz")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_31char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Andrzej Świętosław LasławŁukasz")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Nazwa kraju nie powinna przekraczać 30 znaków")


def test_country_50char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("AndrzejŚwiętosławLasławŁukaszBożenaJózefŚwiętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Nazwa kraju nie powinna przekraczać 30 znaków")


def test_country_numbers_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("1234567890")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")


def test_country_hyphen_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Boże-na-Józef-Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_apostrophe_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("B'ożena'Józef'Świętosła'w")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_space_in_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Bożena Józef Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_symbols_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("B@oż?ena.Józef,Świętosław")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='country']/following-sibling::p")).to_have_text("Wprowadź poprawną nazwę kraju")


def test_country_cyrillic_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Україна")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_latin_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("Ukraine")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_up_case_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("ŁŚABCDE")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_country_low_case_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Ukraina").type("żśćóżęł")
    setup_pl.get_by_placeholder("Kijów").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input__KEXwe")

