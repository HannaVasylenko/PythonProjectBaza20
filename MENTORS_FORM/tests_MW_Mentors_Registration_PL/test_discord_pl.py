import re
from playwright.sync_api import Page, expect


def test_discord_empty_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").click()
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wpisz swoją nazwę użytkownika Discord")


def test_discord_space_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type(" ")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wpisz swoją nazwę użytkownika Discord")


def test_discord_сyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("привіт")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_polski_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("swiętosław")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_latin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("pryvit")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_1char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("a")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #min char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_2char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("au")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_3char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("oon")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_17char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("meredithmarjoryao")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_31char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_32char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsa")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_33char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsak")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_50char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_up_case_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("TESTING")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_lowcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("testing")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_spacein_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("testing test")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_num_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("test9876541230")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_underline_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("t_est_design_techniques")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_point_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("t.est.design.techniques")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discord_start_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("їyahoo")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_symb_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("v,i@ck!the?best")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")


def test_discord_space_in_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("//input[@id='discord']").type("test design")
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")

