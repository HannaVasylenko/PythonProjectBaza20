import re
from playwright.sync_api import Page, expect


def test_send_form_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_text("QA Manual Engineer").click()
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.get_by_text("-15.00").click()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").click()
    expect(page.locator("div").filter(has_text="Ваші дані успішно відправлено").nth(1)).to_be_visible()
    page.screenshot(path="mw_mentorua_scr/mwsendform.png")


def test_close_success_mw_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_text("QA Manual Engineer").click()
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.get_by_text("-15.00").click()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").click()
    page.screenshot(path="mw_mentorua_scr/mwclosesmwO.png")
    page.locator("//button[@class='CloseBtn_btn__ij9AH UseAlert_close_btn__JJTAr']").click()
    #page.locator(".CloseBtn_btn__ij9AH").click()
    expect(page.locator("div").filter(has_text="Ваші дані успішно відправлено").nth(1)).to_be_hidden()
    page.screenshot(path="mw_mentorua_scr/mwclosesmwC.png")


def test_active_sendbtn_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_text("QA Manual Engineer").click()
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.get_by_text("-15.00").click()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_enabled()
    page.screenshot(path="mw_mentorua_scr/mwasendbtn.png")


def test_hover_sendbtn_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_text("QA Manual Engineer").click()
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.get_by_text("-15.00").click()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").hover()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_enabled()
    page.screenshot(path="mw_mentorua_scr/mwhsendbtn.png")


def test_default_sendbtn_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()
    page.screenshot(path="mw_mentorua_scr/mwdefsendbtn.png")


def test_disabled_sendbtn_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("ю")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_text("QA Manual Engineer").click()
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.get_by_text("-15.00").click()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").locator("use").click()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()
    page.screenshot(path="mw_mentorua_scr/mwdsendbtn.png")


def test_without_checkbox_mw_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").hover()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()
    page.screenshot(path="mw_mentorua_scr/mwwithoutch.png")


def test_empty_form_mw_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    page.get_by_placeholder("Прізвище").click()
    page.get_by_role("textbox", name="email@gmail.com").click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.get_by_placeholder("Iм'я користувача в Discord").click()
    page.get_by_placeholder("Лінк на профіль").click()
    page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button").hover()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()
    page.screenshot(path="mw_mentorua_scr/mwemptyform.png")


def test_title_mw_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//h2")).to_have_text("Реєстрація ментора на Baza Trainee Ukraine")
    page.screenshot(path="mw_mentorua_scr/mwtitle.png")


def test_close_mw_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_visible()
    page.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()
    page.screenshot(path="mw_mentorua_scr/mwclosemw.png")


def test_chb_specialization_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.locator("label").filter(has_text="UI/UX Designer").check()
    expect(page.locator("label").filter(has_text="UI/UX Designer")).to_be_checked()
    page.locator("label").filter(has_text="Frontend").check()
    expect(page.locator("label").filter(has_text="Frontend")).to_be_checked()
    page.locator("label").filter(has_text="QA Manual Engineer").check()
    expect(page.locator("label").filter(has_text="QA Manual Engineer")).to_be_checked()
    page.locator("label").filter(has_text="Backend").check()
    expect(page.locator("label").filter(has_text="Backend")).to_be_checked()
    page.locator("label").filter(has_text="Fullstack Engineer").check()
    expect(page.locator("label").filter(has_text="Fullstack Engineer")).to_be_checked()
    page.locator("label").filter(has_text="Project Manager").check()
    expect(page.locator("label").filter(has_text="Project Manager")).to_be_checked()


def test_chb_consultation_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.locator("label").filter(has_text="-15.00").check()
    expect(page.locator("label").filter(has_text="-15.00")).to_be_checked()
    page.locator("label").filter(has_text="-18.00").check()
    expect(page.locator("label").filter(has_text="-18.00")).to_be_checked()
    page.locator("label").filter(has_text="-21.00").check()
    expect(page.locator("label").filter(has_text="-21.00")).to_be_checked()
    page.locator("label").filter(has_text="будь-який").check()
    expect(page.locator("label").filter(has_text="будь-який")).to_be_checked()


def test_send_form_without_agreement_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_text("QA Manual Engineer").click()
    page.get_by_role("textbox", name="email@gmail.com").type("unittestua@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Iм'я користувача в Discord").type("unittestua")
    page.get_by_placeholder("Лінк на профіль").fill("https://www.linkedin.com/in/tanya")
    page.get_by_text("-15.00").click()
    expect(page.locator("form").filter(has_text="Реєстрація ментора на Baza").get_by_role("button")).to_be_disabled()
    page.screenshot(path="mw_mentorua_scr/mwsendformwithoutagr.png")