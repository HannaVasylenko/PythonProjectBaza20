from playwright.sync_api import Page, expect


def test_discord_empty_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").click()
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter your Discord username")


def test_discord_space_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type(" ")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter your Discord username")


def test_discord_cyrillic_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("привіт")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter a valid Discord username")


def test_discord_latin_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("pryvit")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_1char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("a")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Username must have at least 2 characters")


def test_discord_2char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("au")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_3char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("oon")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_17char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("meredithmarjoryao")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_29char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrft")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_30char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftg")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_31char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Username must not exceed 30 characters")


def test_discord_50char_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Username must not exceed 30 characters")


def test_discord_up_case_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("TESTING")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter a valid Discord username")


def test_discord_low_case_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("testing")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_space_in_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("testing test")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter a valid Discord username")


def test_discord_numb_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("test9876541230")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_underline_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("t_est_design_techniques")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_point_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("t.est.design.techniques")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_start_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("їyahoo")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter a valid Discord username")


def test_discord_symb_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("//input[@id='discord']").type("v,i@ck!the?best")
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Enter a valid Discord username")

