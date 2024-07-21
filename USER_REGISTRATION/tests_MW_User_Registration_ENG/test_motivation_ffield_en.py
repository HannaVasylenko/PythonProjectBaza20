import re
from playwright.sync_api import Page, expect


def test_motivation_empty_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").click()
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("State your motivation")


def test_motivation_space_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type(" ")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("State your motivation")


def test_motivation_1char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("t")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes <10>")


def test_motivation_2char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("te")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes <10>")


def test_motivation_5char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("testi")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes <10>")


def test_motivation_9char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("testiasdf")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes <10>")


def test_motivation_10char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("testingasd")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_11char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("testiasdfas")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m")


def test_motivation_20char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklq")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_49char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjkl")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_50char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_51char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqr")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("The text should not exceed 50 characters")


def test_motivation_70char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqqwertyuiopasdfghjklp")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("The text should not exceed 50 characters")


def test_motivation_symb1_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("s!-_().,<>&?@$=+{}#*/[\]")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")

    
def test_motivation_symb2_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("s|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_numb_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("num1234567890")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_up_case_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("TESTING")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_low_case_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Your answer").type("testing")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
