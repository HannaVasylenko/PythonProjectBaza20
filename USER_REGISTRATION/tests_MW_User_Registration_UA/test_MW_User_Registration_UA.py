import re
from playwright.sync_api import Page, expect


def test_close_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()
    page.screenshot(path="mw_screenshots/mw.png")


def test_title_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    expect(page.locator("form h2")).to_have_text("Реєстрація на участь в проєкті Baza Trainee Ukraine")
    page.screenshot(path="mw_screenshots/titlemw.png")


def test_select_specialization(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
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


def test_select_availability_of_experience(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.locator("label").filter(has_text="Так").check()
    expect(page.locator("label").filter(has_text="Так")).to_be_checked()
    page.screenshot(path="mw_screenshots/yesexp.png")
    page.locator("label").filter(has_text="Ні").check()
    expect(page.locator("label").filter(has_text="Ні")).to_be_checked()
    page.screenshot(path="mw_screenshots/noexp.png")


def test_select_questionnaire(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    expect(page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine")).to_be_checked()
    page.locator("label").filter(has_text="На сторінці Baza Educat в Instagram").check()
    expect(page.locator("label").filter(has_text="На сторінці Baza Educat в Instagram")).to_be_checked()
    page.locator("label").filter(has_text="На сторінці Baza Educat в Facebook").check()
    expect(page.locator("label").filter(has_text="На сторінці Baza Educat в Facebook")).to_be_checked()
    page.locator("label").filter(has_text="в каналі Baza Go в Telegram").check()
    expect(page.locator("label").filter(has_text="в каналі Baza Go в Telegram")).to_be_checked()
    page.locator("label").filter(has_text="в пості на LinkedIn").check()
    expect(page.locator("label").filter(has_text="в пості на LinkedIn")).to_be_checked()


def test_rules_BazaTrainee_project_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_role("button", name="Читати тут").click()
    expect(page.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_visible()
    page.screenshot(path="mw_screenshots/rules.png")
    page.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    expect(page.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_hidden()
    page.screenshot(path="mw_screenshots/closerulesmw.png")


def test_select_agreement(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.locator("label").filter(has_text="Погоджуюсь").check()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    expect(page.locator("label").filter(has_text="Погоджуюсь")).to_be_checked()
    expect(page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних")).to_be_checked()
    page.screenshot(path="mw_screenshots/agreement.png")


def test_active_send_btn_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.locator("label").filter(has_text="QA Manual Engineer").check()
    page.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").type("Юніт тест юа")
    page.get_by_placeholder("Україна").type("Юніт тест юа")
    page.get_by_placeholder("Iм'я користувача в Discord").type("test")
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    page.locator("label").filter(has_text="Так").check()
    page.get_by_placeholder("Ваша відповідь").type("Юніт тест юа")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    page.get_by_role("button", name="Читати тут").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    page.locator("label").filter(has_text="Погоджуюсь").check()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    expect(page.get_by_role("button", name="Відправити")).to_be_enabled()
    page.screenshot(path="mw_screenshots/mwsendbtn.png")


def test_send_form_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.locator("label").filter(has_text="QA Manual Engineer").check()
    page.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").type("Юніт тест юа")
    page.get_by_placeholder("Україна").type("Юніт тест юа")
    page.get_by_placeholder("Iм'я користувача в Discord").type("test")
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    page.locator("label").filter(has_text="Так").check()
    page.get_by_placeholder("Ваша відповідь").type("Юніт тест юа") #min 5 char
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    page.get_by_role("button", name="Читати тут").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    page.locator("label").filter(has_text="Погоджуюсь").check()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    page.get_by_role("button", name="Відправити").click()
    expect(page.locator("div").filter(has_text="Ваші дані успішно відправлено").nth(1)).to_be_visible()
    page.screenshot(path="mw_screenshots/mwsendform.png")


def test_send_form_without_last_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.locator("label").filter(has_text="QA Manual Engineer").check()
    page.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").type("Юніт тест юа")
    page.get_by_placeholder("Україна").type("Юніт тест юа")
    page.get_by_placeholder("Iм'я користувача в Discord").type("test")
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    page.locator("label").filter(has_text="Так").check()
    page.get_by_placeholder("Ваша відповідь").type("Юніт тест юа") #min 5 char
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    page.locator("label").filter(has_text="Погоджуюсь").check()
    expect(page.get_by_role("button", name="Відправити")).to_be_disabled()
    page.screenshot(path="mw_screenshots/mwsendwithoutlast.png")


def test_send_form_without_last2_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.locator("label").filter(has_text="QA Manual Engineer").check()
    page.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").type("Юніт тест юа")
    page.get_by_placeholder("Україна").type("Юніт тест юа")
    page.get_by_placeholder("Iм'я користувача в Discord").type("test")
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    page.locator("label").filter(has_text="Так").check()
    page.get_by_placeholder("Ваша відповідь").type("Юніт тест юа") #min 5 char
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").check()
    page.locator("label").filter(has_text="Надаю згоду на обробку персональних даних").check()
    expect(page.get_by_role("button", name="Відправити")).to_be_disabled()
    page.screenshot(path="mw_screenshots/mwsendwithoutlast2.png")


def test_empty_form_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").click()
    page.get_by_placeholder("Прізвище").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.get_by_placeholder("Київ").click()
    page.get_by_placeholder("Україна").click()
    page.get_by_placeholder("Iм'я користувача в Discord").click()
    page.get_by_placeholder("Лінк на профіль").click()
    page.get_by_placeholder("Ваша відповідь").click()
    expect(page.get_by_role("button", name="Відправити")).to_be_disabled()
    page.screenshot(path="mw_screenshots/mwemptyform.png")


def test_send_without_checkbox_mw(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ім’я").type("Юніт тест юа")
    page.get_by_placeholder("Прізвище").type("Юніт тест юа")
    page.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").type("Юніт тест юа")
    page.get_by_placeholder("Україна").type("Юніт тест юа")
    page.get_by_placeholder("Iм'я користувача в Discord").type("test")
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/test")
    page.get_by_placeholder("Ваша відповідь").type("Юніт тест юа") #min 5 char
    expect(page.get_by_role("button", name="Відправити")).to_be_disabled()
    page.screenshot(path="mw_screenshots/mwsendwithoutcheckbox.png")

