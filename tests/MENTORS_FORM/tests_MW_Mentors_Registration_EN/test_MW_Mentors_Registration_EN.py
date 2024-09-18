import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip(reason="Check the test manually")
def test_send_form_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Unit test en")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/unittesten")
    setup_en.get_by_text("-15.00").click()
    setup_en.locator("label").filter(has_text="I consent to the processing of personal data").locator("use").click()
    setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button").click()
    expect(setup_en.locator("div").filter(has_text="Your data has been sent").nth(1)).to_be_visible()


@pytest.mark.skip(reason="Check the test manually")
def test_close_success_mw_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Unit test en")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/unittesten")
    setup_en.get_by_text("-15.00").click()
    setup_en.locator("label").filter(has_text="I consent to the processing of personal data").locator("use").click()
    setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button").click()
    setup_en.locator("//button[@class='CloseBtn_btn__ij9AH UseAlert_close_btn__JJTAr']").click()
    expect(setup_en.locator("div").filter(has_text="Your data has been sent").nth(1)).to_be_hidden()


def test_active_send_btn_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Unit test en")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/unittesten")
    setup_en.get_by_text("-15.00").click()
    setup_en.locator("label").filter(has_text="I consent to the processing of personal data").locator("use").click()
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button")).to_be_enabled()


def test_hover_send_btn_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Unit test en")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/unittesten")
    setup_en.get_by_text("-15.00").click()
    setup_en.locator("label").filter(has_text="I consent to the processing of personal data").locator("use").click()
    setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button").hover()
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza")).to_be_enabled()


def test_default_send_btn_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button")).to_be_enabled()


def test_disabled_send_btn_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("a")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/Unittesten")
    setup_en.get_by_text("-15.00").click()
    setup_en.locator("label").filter(has_text="I consent to the processing of personal data").locator("use").click()
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button")).to_be_disabled()


def test_without_checkbox_mw_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Unit test en")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/Unittesten")
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button")).to_be_disabled()


def test_empty_form_mw_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).click()
    setup_en.get_by_placeholder("Last Name").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_en.locator("//input[@id='discord']").click()
    setup_en.get_by_placeholder("Link to profile").click()
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button")).to_be_disabled()


def test_title_mw_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//h2")).to_have_text("Mentor registration on Baza Trainee Ukraine")


def test_close_mw_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_visible()
    setup_en.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()


def test_chb_specialization_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("label").filter(has_text="UI/UX Designer").check()
    expect(setup_en.locator("label").filter(has_text="UI/UX Designer")).to_be_checked()
    setup_en.locator("label").filter(has_text="Frontend").check()
    expect(setup_en.locator("label").filter(has_text="Frontend")).to_be_checked()
    setup_en.locator("label").filter(has_text="QA Manual Engineer").check()
    expect(setup_en.locator("label").filter(has_text="QA Manual Engineer")).to_be_checked()
    setup_en.locator("label").filter(has_text="Backend").check()
    expect(setup_en.locator("label").filter(has_text="Backend")).to_be_checked()
    setup_en.locator("label").filter(has_text="Fullstack Engineer").check()
    expect(setup_en.locator("label").filter(has_text="Fullstack Engineer")).to_be_checked()
    setup_en.locator("label").filter(has_text="Project Manager").check()
    expect(setup_en.locator("label").filter(has_text="Project Manager")).to_be_checked()


def test_chb_consultation_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.locator("label").filter(has_text="-15.00").check()
    expect(setup_en.locator("label").filter(has_text="-15.00")).to_be_checked()
    setup_en.locator("label").filter(has_text="-18.00").check()
    expect(setup_en.locator("label").filter(has_text="-18.00")).to_be_checked()
    setup_en.locator("label").filter(has_text="-21.00").check()
    expect(setup_en.locator("label").filter(has_text="-21.00")).to_be_checked()
    setup_en.locator("label").filter(has_text="anytime").check()
    expect(setup_en.locator("label").filter(has_text="anytime")).to_be_checked()


def test_send_form_without_agreement_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="First Name", exact=True).type("Unit test en")
    setup_en.get_by_placeholder("Last Name").type("Unit test en")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.locator("//input[@id='discord']").type("unittesten")
    setup_en.get_by_placeholder("Link to profile").fill("https://www.linkedin.com/in/unittesten")
    setup_en.get_by_text("-15.00").click()
    expect(setup_en.locator("form").filter(has_text="Mentor registration on Baza").get_by_role("button")).to_be_disabled()
