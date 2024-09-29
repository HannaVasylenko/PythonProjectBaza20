from playwright.sync_api import Page, expect


def test_discord_empty_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").click()
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wpisz swoją nazwę użytkownika Discord")


def test_discord_space_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type(" ")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wpisz swoją nazwę użytkownika Discord")


def test_discord_cyrillic_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("привіт")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_polski_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("swiętosław")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_latin_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("pryvit")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_1char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("a")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Nazwa użytkownika musi mieć co najmniej 2 znaki")


def test_discord_2char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("au")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_3char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("oon")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_17char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("meredithmarjoryao")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_29char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrft")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_30char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftg")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_31char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Nazwa użytkownika nie może przekraczać 30 znaków")


def test_discord_50char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Nazwa użytkownika nie może przekraczać 30 znaków")


def test_discord_up_case_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("TESTING")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_low_case_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("testing")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_space_in_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("testing test")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_numb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("test9876541230")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_underline_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("t_est_design_techniques")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_point_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("t.est.design.techniques")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_start_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("їyahoo")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_symb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("v,i@ck!the?best")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")

