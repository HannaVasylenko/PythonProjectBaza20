import re
from playwright.sync_api import Page, expect


def test_close_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']")).to_be_hidden()


def test_title_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    expect(setup_pl.locator("form h2")).to_have_text("Rejestracja do udziału w projekcie Baza Trainee Ukraine")


def test_select_specialization_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
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


def test_select_availability_of_experience_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.locator("label").filter(has_text="Więc").check()
    expect(setup_pl.locator("label").filter(has_text="Więc")).to_be_checked()
    setup_pl.locator("label").filter(has_text=re.compile(r"^Nie$")).check()
    expect(setup_pl.locator("label").filter(has_text=re.compile(r"^Nie$"))).to_be_checked()


def test_select_questionnaire_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").check()
    expect(setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina")).to_be_checked()
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Educat na Instagramie").check()
    expect(setup_pl.locator("label").filter(has_text="Na stronie Bazy Educat na Instagramie")).to_be_checked()
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Edukacyjnej na Facebooku").check()
    expect(setup_pl.locator("label").filter(has_text="Na stronie Bazy Edukacyjnej na Facebooku")).to_be_checked()
    setup_pl.locator("label").filter(has_text="na kanale Baza Go Telegram").check()
    expect(setup_pl.locator("label").filter(has_text="na kanale Baza Go Telegram")).to_be_checked()
    setup_pl.locator("label").filter(has_text="w poście na LinkedIn").check()
    expect(setup_pl.locator("label").filter(has_text="w poście na LinkedIn")).to_be_checked()


def test_rules_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_role("button", name="przeczytaj tutaj").click()
    expect(setup_pl.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_visible()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    expect(setup_pl.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_hidden()


def test_select_agreement_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.locator("label").filter(has_text="Zgadzam się").check()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na przetwarzanie").check()
    expect(setup_pl.locator("label").filter(has_text="Zgadzam się")).to_be_checked()
    expect(setup_pl.locator("label").filter(has_text="Wyrażam zgodę na przetwarzanie")).to_be_checked()

    
def test_active_send_btn_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Imię").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.get_by_placeholder("Nazwisko").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_pl.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    setup_pl.get_by_placeholder("Ukraina").type("LasławŁukaJózef")
    setup_pl.locator("//input[@id='discord']").type("test")
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/test")
    setup_pl.locator("label").filter(has_text="Więc").check()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("test text")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").check()
    setup_pl.get_by_role("button", name="przeczytaj tutaj").click()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup_pl.locator("label").filter(has_text="Zgadzam się").check()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na przetwarzanie").check()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_enabled()


def test_send_form_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Imię").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.get_by_placeholder("Nazwisko").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_pl.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    setup_pl.get_by_placeholder("Ukraina").type("LasławŁukaJózef")
    setup_pl.locator("//input[@id='discord']").type("test")
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/test")
    setup_pl.locator("label").filter(has_text="Więc").check()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("test text")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").check()
    setup_pl.get_by_role("button", name="przeczytaj tutaj").click()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup_pl.locator("label").filter(has_text="Zgadzam się").check()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na przetwarzanie").check()
    setup_pl.get_by_role("button", name="Wysłać").click()
    expect(setup_pl.locator("div").filter(has_text="Twoje dane zostały pomyślnie").nth(1)).to_be_visible()


def test_send_form_without_last_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Imię").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.get_by_placeholder("Nazwisko").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_pl.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    setup_pl.get_by_placeholder("Ukraina").type("LasławŁukaJózef")
    setup_pl.locator("//input[@id='discord']").type("test")
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/test")
    setup_pl.locator("label").filter(has_text="Więc").check()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("test text")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").check()
    setup_pl.get_by_role("button", name="przeczytaj tutaj").click()
    setup_pl.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup_pl.locator("label").filter(has_text="Zgadzam się").check()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()


def test_send_form_without_last2_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Imię").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.get_by_placeholder("Nazwisko").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_pl.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    setup_pl.get_by_placeholder("Ukraina").type("LasławŁukaJózef")
    setup_pl.locator("//input[@id='discord']").type("test")
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/test")
    setup_pl.locator("label").filter(has_text="Więc").check()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("test text")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").check()
    setup_pl.locator("label").filter(has_text="Wyrażam zgodę na przetwarzanie").check()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()


def test_empty_form_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Imię").click()
    setup_pl.get_by_placeholder("Nazwisko").click()
    setup_pl.get_by_placeholder("email@gmail.com").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_pl.get_by_placeholder("Kijów").click()
    setup_pl.get_by_placeholder("Ukraina").click()
    setup_pl.locator("//input[@id='discord']").click()
    setup_pl.get_by_placeholder("Link do profilu").click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").click()
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()


def test_send_form_without_checkbox_mw_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Imię").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.get_by_placeholder("Nazwisko").type("Żelisław Andrzej BożenaJózefa")
    setup_pl.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.get_by_placeholder("Kijów").type("LasławŁukaJózef")
    setup_pl.get_by_placeholder("Ukraina").type("LasławŁukaJózef")
    setup_pl.locator("//input[@id='discord']").type("test")
    setup_pl.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/test")
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("test text")
    expect(setup_pl.get_by_role("button", name="Wysłać")).to_be_disabled()
