import re
import  pytest
from playwright.sync_api import Page, expect


def test_ln_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").click()
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")


def test_ln_space_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type(" ")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")


def test_ln_valid_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Testdesigntechniques")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_ln_lowcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/testing")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_ln_upcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/TESTING")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_199char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfgh")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_200char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_201char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjj")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_250char_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_without_http_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("www.linkedin.com/in/Testdesigntechniques")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_num_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("0123456789")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_symb_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("!@#?*")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_num_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Testtechniques1234567890")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_symb_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/T.es,t!de?si@gn")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("Testdesign1234567890")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_lnpart_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


def test_ln_сyrillic_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Тестування")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_space_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Testdesign techniques")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_underline_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t_est_ing_t")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_point_in_username_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t.est.ing.t")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")

