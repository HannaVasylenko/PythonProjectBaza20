import re
import pytest
from playwright.sync_api import Page, expect


def test_ln_empty_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").click()
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")


def test_ln_space_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type(" ")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")


def test_ln_valid_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Testdesigntechniques")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_ln_low_case_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/testdesigntechniques")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_ln_up_case_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/TESTING")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_199char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfgh")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_200char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_201char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjl")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


@pytest.mark.skip(reason="The field contains restrictions")
def test_ln_250char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_without_http_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("www.linkedin.com/in/Testdesigntechniques")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_numb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("0123456789")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_symb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("!@#?*")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_num_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Testtechniques1234567890")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_symb_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/T.es,t!de?si@gn")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("Testdesign1234567890")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_lnpart_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


def test_ln_cyrillic_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Тестування")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_only_polski_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/żęóżłŚŁ")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_polski_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/testżęóżłŚŁ")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_space_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Testdesign techniques")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_underline_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/t_est_ing_t")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_point_in_username_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/t.est.ing.t")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")

