import re
import pytest
from playwright.sync_api import Page, expect


def test_lnpr_empty_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").click()
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть профіль в Linkedin")


def test_lnpr_сyrillic_in_username_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/тетянка")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_symb_in_username_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t.es,ti@n?g")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_space_in_username_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test test")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_underlines_in_username_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t_est_test_t")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_point_in_username_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t.est.test.t")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_lnpr_lnpart_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_lnpr_without_http_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("www.linkedin.com/in/tanya")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_lnpr_valid_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/tanya")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_lnpr_up_case_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/TESTING")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_lnpr_low_case_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/testing")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_199char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/hecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_200char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/shecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_201char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghja")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_250char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_lnpr_num_in_username_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/tanya1234567890")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_lnpr_numbers_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("1234567890")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_lnpr_symbols_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type("!@#?*")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")


def test_lnprua_space_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Лінк на профіль").type(" ")
    setup.locator("label").filter(has_text="Так").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть профіль в Linkedin")
