import re
import pytest
from playwright.sync_api import Page, expect


def test_lnpr_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").click()
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")


def test_lnpr_without_http_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("www.linkedin.com/in/tanya")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_lnpr_сyrillic_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/тетянка")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_symb_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/te.s,t?i!n@g")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_space_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test test")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_underline_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t_est_test_t")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_point_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t.est.test.t")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_lnpr_lnpart_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_lnpr_valid_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/tanya")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_lnpr_upcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/TESTING")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_lnpr_lowcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/testing")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_199char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/hecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghj")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_200char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ahecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghj")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_201char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjs")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_250char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/qqwertyuiqwertyuiopasdfghjklzqwertyuiophecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjsqasdfghjklo")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_numb_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/tanya1234567890")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_lnpr_numbers_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("1234567890")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_lnpr_symbols_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type("!@#?*")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_lnpr_space_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Link to profile").type(" ")
    setup_en.locator("label").filter(has_text="Yes").locator("use").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")
