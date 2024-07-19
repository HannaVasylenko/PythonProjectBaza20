import re
import pytest
from playwright.sync_api import Page, expect


def test_ln_empty_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").click()
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть профіль в Linkedin")


def test_ln_space_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type(" ")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть профіль в Linkedin")


def test_ln_valid_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/StepanBandera")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_ln_upcase_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/TESTING")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_ln_lowcase_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/testing")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_199char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfgh")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_200char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghj")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_201char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjj")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_250char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_without_http_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("www.linkedin.com/in/StepanBandera")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_num_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("0123456789")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_symb_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("!@#?*")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_num_in_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/StepanBandera1234567890")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_symb_in_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/S!epan,Ban?era@")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("StepanBandera1234567890")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_lnpart_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_ln_сyrillic_in_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/СтепанАндрійовичБандера")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_space_in_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/Testdesign techniques")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_underline_in_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t_est_ing_tt")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_point_in_username_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t.est.ing.tt")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")

