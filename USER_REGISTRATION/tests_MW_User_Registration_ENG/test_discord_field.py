import re
from playwright.sync_api import Page, expect


def test_discordpr_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").click()
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter your Discord username") #Enter a nickname in Discord Enter your Discord username Enter your Discord username


def test_discordpr_space_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type(" ")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter your Discord username") #Enter a nickname in Discord Enter your Discord username Enter your Discord username


def test_discordpr_сyrillic_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("привіт")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username") # Enter a valid Discord username Enter a valid Discord username


def test_discordpr_latin_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("pryvit")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_spacein_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("test test")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username") #Enter a nickname in Discord Enter your Discord username Enter your Discord username


def test_discordpr_1char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("a")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes >2char")


def test_discordpr_2char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("au")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_3char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("duo")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_17char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("meredithmarjoryao")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_31char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_32char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsa")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_33char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsak")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")


def test_discordpr_50char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")


def test_discordpr_up_case_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("NICK")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")


def test_discordpr_numbers_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("test9876541230")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_underline_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("t_anya_qa_manual")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_point_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("t.anya.qa.manu.al")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_begin_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("тanya")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")


def test_discordpr_symbols_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//input[@id='discord']").type("vi@ck!the?be%st")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
