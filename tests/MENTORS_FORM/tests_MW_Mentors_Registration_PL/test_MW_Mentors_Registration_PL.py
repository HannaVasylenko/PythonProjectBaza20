import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip(reason="Check the test manually")
def test_send_form_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Róża")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/unittestpl")
    setup_pl.get_by_text("-15.00").click()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na").locator("use").click()
    setup_pl.get_by_role("button", name="Wysłać").click()
    expect(setup_pl.locator("div").filter(has_text="Twoje dane zostały pomyślnie").nth(1)).to_be_visible()


@pytest.mark.skip(reason="Check the test manually")
def test_close_success_mw_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Róża")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/unittestpl")
    setup_pl.get_by_text("-15.00").click()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na").locator("use").click()
    setup_pl.get_by_role("button", name="Wysłać").click()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH UseAlert_close_btn__JJTAr']").click()
    expect(setup_pl.locator("div").filter(has_text="Twoje dane zostały pomyślnie").nth(1)).to_be_hidden()


def test_active_send_btn_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Róża")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/unittestpl")
    setup_pl.get_by_text("-15.00").click()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na").locator("use").click()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_enabled()


def test_hover_send_btn_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Róża")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/unittestpl")
    setup_pl.get_by_text("-15.00").click()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na").locator("use").click()
    setup_pl.get_by_role("button", name="Wysłać").hover()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_enabled()


def test_default_send_btn_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_enabled()


def test_disabled_send_btn_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Ś")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/Unittestpl")
    setup_pl.get_by_text("-15.00").click()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na").locator("use").click()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()


def test_without_checkbox_mw_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Róża")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/Unittestpl")
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()


def test_empty_form_mw_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    setup_pl.get_by_placeholder("Nazwisko").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_pl.locator("//input[@id='discord']").click()
    setup_pl.get_by_placeholder("Link do profilu").click()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()


def test_title_mw_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//h2")).to_have_text("Rejestracja mentora na Baza Trainee Ukraine")


def test_close_mw_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    expect(setup_pl.locator(".RegistrationFormModal_wrapper__bgALB")).to_be_visible()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()


def test_chb_specialization_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("label").filter(has_text="UI/UX Designer").check()
    expect(setup_pl.locator("label").filter(has_text="UI/UX Designer")).to_be_checked()
    setup_pl.locator("label").filter(has_text="Frontend").check()
    expect(setup_pl.locator("label").filter(has_text="Frontend")).to_be_checked()
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").check()
    expect(setup_pl.locator("label").filter(has_text="QA Manual Engineer")).to_be_checked()
    setup_pl.locator("label").filter(has_text="Backend").check()
    expect(setup_pl.locator("label").filter(has_text="Backend")).to_be_checked()
    setup_pl.locator("label").filter(has_text="Fullstack Engineer").check()
    expect(setup_pl.locator("label").filter(has_text="Fullstack Engineer")).to_be_checked()
    setup_pl.locator("label").filter(has_text="Project Manager").check()
    expect(setup_pl.locator("label").filter(has_text="Project Manager")).to_be_checked()


def test_chb_consultation_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.locator("label").filter(has_text="-15.00").check()
    expect(setup_pl.locator("label").filter(has_text="-15.00")).to_be_checked()
    setup_pl.locator("label").filter(has_text="-18.00").check()
    expect(setup_pl.locator("label").filter(has_text="-18.00")).to_be_checked()
    setup_pl.locator("label").filter(has_text="-21.00").check()
    expect(setup_pl.locator("label").filter(has_text="-21.00")).to_be_checked()
    setup_pl.locator("label").filter(has_text="kiedykolwiek").check()
    expect(setup_pl.locator("label").filter(has_text="kiedykolwiek")).to_be_checked()


def test_send_form_without_agreement_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).type("Świętosław Róża")
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").locator("use").click()
    setup_pl.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").type("unittestpl")
    setup_pl.get_by_placeholder("Link do profilu").fill("https://www.linkedin.com/in/unittestpl")
    setup_pl.get_by_text("-15.00").click()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()
