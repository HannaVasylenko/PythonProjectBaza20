import re
from playwright.sync_api import Page, expect


def test_close_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()


def test_title_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    expect(setup.locator("form h2")).to_have_text("Реєстрація на участь в проєкті Baza Trainee Ukraine")


def test_select_specialization_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
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


def test_select_availability_of_experience_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.locator("label").filter(has_text="Так").check()
    expect(setup.locator("label").filter(has_text="Так")).to_be_checked()
    setup.locator("label").filter(has_text="Ні").check()
    expect(setup.locator("label").filter(has_text="Ні")).to_be_checked()


def test_select_questionnaire_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    expect(setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine")).to_be_checked()
    setup.locator("label").filter(has_text="На сторінці Baza Educat в Instagram").check()
    expect(setup.locator("label").filter(has_text="На сторінці Baza Educat в Instagram")).to_be_checked()
    setup.locator("label").filter(has_text="На сторінці Baza Educat в Facebook").check()
    expect(setup.locator("label").filter(has_text="На сторінці Baza Educat в Facebook")).to_be_checked()
    setup.locator("label").filter(has_text="в каналі Baza Go в Telegram").check()
    expect(setup.locator("label").filter(has_text="в каналі Baza Go в Telegram")).to_be_checked()
    setup.locator("label").filter(has_text="в пості на LinkedIn").check()
    expect(setup.locator("label").filter(has_text="в пості на LinkedIn")).to_be_checked()


def test_rules_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_role("button", name="Читати тут").click()
    expect(setup.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_visible()
    setup.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    expect(setup.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_hidden()


def test_select_agreement_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.locator("label").filter(has_text="Погоджуюсь").check()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    expect(setup.locator("label").filter(has_text="Погоджуюсь")).to_be_checked()
    expect(setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних")).to_be_checked()


def test_active_send_btn_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ім’я").type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.locator("label").filter(has_text="QA Manual Engineer").check()
    setup.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").type("Юніт тест юа")
    setup.get_by_placeholder("Україна").type("Юніт тест юа")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("test")
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    setup.locator("label").filter(has_text="Так").check()
    setup.get_by_placeholder("Ваша відповідь").type("Юніт тест юа")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    setup.get_by_role("button", name="Читати тут").click()
    setup.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup.locator("label").filter(has_text="Погоджуюсь").check()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    expect(setup.get_by_role("button", name="Відправити")).to_be_enabled()


def test_send_form_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ім’я").type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.locator("label").filter(has_text="QA Manual Engineer").check()
    setup.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").type("Юніт тест юа")
    setup.get_by_placeholder("Україна").type("Юніт тест юа")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("test")
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    setup.locator("label").filter(has_text="Так").check()
    setup.get_by_placeholder("Ваша відповідь").type("Юніт тест юа")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    setup.get_by_role("button", name="Читати тут").click()
    setup.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup.locator("label").filter(has_text="Погоджуюсь").check()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    setup.get_by_role("button", name="Відправити").click()
    expect(setup.locator("div").filter(has_text="Ваші дані успішно відправлено").nth(1)).to_be_visible()


def test_send_form_without_last_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ім’я").type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.locator("label").filter(has_text="QA Manual Engineer").check()
    setup.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").type("Юніт тест юа")
    setup.get_by_placeholder("Україна").type("Юніт тест юа")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("test")
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    setup.locator("label").filter(has_text="Так").check()
    setup.get_by_placeholder("Ваша відповідь").type("Юніт тест юа")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    setup.locator("label").filter(has_text="Погоджуюсь").check()
    expect(setup.get_by_role("button", name="Відправити")).to_be_disabled()


def test_send_form_without_last2_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ім’я").type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.locator("label").filter(has_text="QA Manual Engineer").check()
    setup.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").type("Юніт тест юа")
    setup.get_by_placeholder("Україна").type("Юніт тест юа")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("test")
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    setup.locator("label").filter(has_text="Так").check()
    setup.get_by_placeholder("Ваша відповідь").type("Юніт тест юа")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    setup.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    expect(setup.get_by_role("button", name="Відправити")).to_be_disabled()


def test_empty_form_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ім’я").click()
    setup.get_by_placeholder("Прізвище").click()
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    setup.get_by_placeholder("Київ").click()
    setup.get_by_placeholder("Україна").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").click()
    setup.get_by_placeholder("Лінк на профіль").click()
    setup.get_by_placeholder("Ваша відповідь").click()
    expect(setup.get_by_role("button", name="Відправити")).to_be_disabled()


def test_send_without_checkbox_mw_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ім’я").type("Юніт тест юа")
    setup.get_by_placeholder("Прізвище").type("Юніт тест юа")
    setup.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").type("Юніт тест юа")
    setup.get_by_placeholder("Україна").type("Юніт тест юа")
    setup.get_by_placeholder("Iм'я користувача в Discord").type("test")
    setup.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    setup.get_by_placeholder("Ваша відповідь").type("Юніт тест юа")
    expect(setup.get_by_role("button", name="Відправити")).to_be_disabled()

