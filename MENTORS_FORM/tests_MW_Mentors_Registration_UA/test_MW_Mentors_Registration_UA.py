import re
from playwright.sync_api import Page, expect


def test_send_form_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_text("QA Manual Engineer").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.get_by_text("-15.00").click()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").click()
    expect(setup.locator("div").filter(has_text="Ваші дані успішно відправлено").nth(1)).to_be_visible()


def test_close_success_mw_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_text("QA Manual Engineer").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.get_by_text("-15.00").click()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").click()
    setup.screenshot(path="mw_mentorua_scr/mwclosesmwO.png")
    setup.locator("//button[@class='CloseBtn_btn__ij9AH UseAlert_close_btn__JJTAr']").click()
    expect(setup.locator("div").filter(has_text="Ваші дані успішно відправлено").nth(1)).to_be_hidden()


def test_active_send_btn_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_text("QA Manual Engineer").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.get_by_text("-15.00").click()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_enabled()


def test_hover_send_btn_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_text("QA Manual Engineer").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.get_by_text("-15.00").click()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").hover()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_enabled()


def test_default_send_btn_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_enabled()


def test_disabled_send_btn_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("ю")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_text("QA Manual Engineer").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.get_by_text("-15.00").click()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()


def test_without_checkbox_mw_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").hover()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()


def test_empty_form_mw_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    setup.get_by_placeholder("Прізвище").click()
    setup.get_by_role("textbox", name="email@gmail.com").click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").click()
    setup.get_by_placeholder("Лінк на профіль").click()
    setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").hover()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()


def test_title_mw_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//h2")).to_have_text("Реєстрація ментора на Baza Trainee Ukraine")


def test_close_mw_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_visible()
    setup.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()


def test_chb_specialization_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.locator("label").filter(has_text="UI/UX Designer").check()
    expect(setup.locator("label").filter(has_text="UI/UX Designer")).to_be_checked()
    setup.locator("label").filter(has_text="Frontend").check()
    expect(setup.locator("label").filter(has_text="Frontend")).to_be_checked()
    setup.locator("label").filter(has_text="QA Manual Engineer").check()
    expect(setup.locator("label").filter(has_text="QA Manual Engineer")).to_be_checked()
    setup.locator("label").filter(has_text="Backend").check()
    expect(setup.locator("label").filter(has_text="Backend")).to_be_checked()
    setup.locator("label").filter(has_text="Fullstack Engineer").check()
    expect(setup.locator("label").filter(has_text="Fullstack Engineer")).to_be_checked()
    setup.locator("label").filter(has_text="Project Manager").check()
    expect(setup.locator("label").filter(has_text="Project Manager")).to_be_checked()


def test_chb_consultation_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.locator("label").filter(has_text="-15.00").check()
    expect(setup.locator("label").filter(has_text="-15.00")).to_be_checked()
    setup.locator("label").filter(has_text="-18.00").check()
    expect(setup.locator("label").filter(has_text="-18.00")).to_be_checked()
    setup.locator("label").filter(has_text="-21.00").check()
    expect(setup.locator("label").filter(has_text="-21.00")).to_be_checked()
    setup.locator("label").filter(has_text="будь-який").check()
    expect(setup.locator("label").filter(has_text="будь-який")).to_be_checked()


def test_send_form_without_agreement_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_text("QA Manual Engineer").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    setup.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    setup.get_by_text("-15.00").click()
    expect(setup.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()
