from playwright.sync_api import Page, expect


def test_close_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("//button[@class='CloseBtn_btn__ij9AH RegistrationFormModal_closeButton__Wn1pT']").click()
    expect(setup_en.locator(".RegistrationFormModal_wrapper__bgALB")).to_be_hidden()


def test_title_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    expect(setup_en.locator("form h2")).to_have_text("Registration for participation in the Baza Trainee Ukraine project")


def test_select_specialization_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
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


def test_select_availability_of_experience_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("label").filter(has_text="Yes").check()
    expect(setup_en.locator("label").filter(has_text="Yes")).to_be_checked()
    setup_en.locator("label").filter(has_text="No").check()
    expect(setup_en.locator("label").filter(has_text="No")).to_be_checked()


def test_select_questionnaire_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine").check()
    expect(setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine")).to_be_checked()
    setup_en.locator("label").filter(has_text="On the Baza Educat Instagram").check()
    expect(setup_en.locator("label").filter(has_text="On the Baza Educat Instagram")).to_be_checked()
    setup_en.locator("label").filter(has_text="On the Baza Educat Facebook").check()
    expect(setup_en.locator("label").filter(has_text="On the Baza Educat Facebook")).to_be_checked()
    setup_en.locator("label").filter(has_text="in the Baza Go Telegram").check()
    expect(setup_en.locator("label").filter(has_text="in the Baza Go Telegram")).to_be_checked()
    setup_en.locator("label").filter(has_text="in a LinkedIn post").check()
    expect(setup_en.locator("label").filter(has_text="in a LinkedIn post")).to_be_checked()


def test_rules_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_role("button", name="Read here").click()
    expect(setup_en.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_visible()
    setup_en.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    expect(setup_en.locator("//div[@class='ModalDocumentPdf_wrapper___sx__']")).to_be_hidden()


def test_select_agreement_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.locator("label").filter(has_text="I agree").check()
    setup_en.locator("label").filter(has_text="I consent to the processing").check()
    expect(setup_en.locator("label").filter(has_text="I agree")).to_be_checked()
    expect(setup_en.locator("label").filter(has_text="I consent to the processing")).to_be_checked()


def test_active_send_btn_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("First Name").type("Test")
    setup_en.get_by_placeholder("Last Name").type("Test")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_en.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv")
    setup_en.get_by_placeholder("Ukraine").type("Ukraine")
    setup_en.locator("//input[@id='discord']").type("test")
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test")
    setup_en.locator("label").filter(has_text="Yes").check()
    setup_en.get_by_placeholder("Your answer").type("test text")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine").check()
    setup_en.get_by_role("button", name="Read here").click()
    setup_en.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup_en.locator("label").filter(has_text="I agree").check()
    setup_en.locator("label").filter(has_text="I consent to the processing").check()
    expect(setup_en.get_by_role("button", name="Send")).to_be_enabled()


def test_send_form_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("First Name").type("Test")
    setup_en.get_by_placeholder("Last Name").type("Test")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_en.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv")
    setup_en.get_by_placeholder("Ukraine").type("Ukraine")
    setup_en.locator("//input[@id='discord']").type("test")
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test")
    setup_en.locator("label").filter(has_text="Yes").check()
    setup_en.get_by_placeholder("Your answer").type("test text")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine").check()
    setup_en.get_by_role("button", name="Read here").click()
    setup_en.locator("//button[@class='CloseBtn_btn__ij9AH ModalDocumentPdf_closeButton__eH4h7']").click()
    setup_en.locator("label").filter(has_text="I agree").check()
    setup_en.locator("label").filter(has_text="I consent to the processing").check()
    setup_en.get_by_role("button", name="Send").click()
    expect(setup_en.locator("div").filter(has_text="Your data has been sent").nth(1)).to_be_visible()


def test_send_form_without_last_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("First Name").type("Test")
    setup_en.get_by_placeholder("Last Name").type("Test")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_en.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv")
    setup_en.get_by_placeholder("Ukraine").type("Ukraine")
    setup_en.locator("//input[@id='discord']").type("test")
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test")
    setup_en.locator("label").filter(has_text="Yes").check()
    setup_en.get_by_placeholder("Your answer").type("test text")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine").check()
    setup_en.locator("label").filter(has_text="I agree").check()
    expect(setup_en.get_by_role("button", name="Send")).to_be_disabled()


def test_send_form_without_last2_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("First Name").type("Test")
    setup_en.get_by_placeholder("Last Name").type("Test")
    setup_en.locator("label").filter(has_text="QA Manual Engineer").check()
    setup_en.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv")
    setup_en.get_by_placeholder("Ukraine").type("Ukraine")
    setup_en.locator("//input[@id='discord']").type("test")
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test")
    setup_en.locator("label").filter(has_text="Yes").check()
    setup_en.get_by_placeholder("Your answer").type("test text")
    setup_en.locator("label").filter(has_text="On the Baza Trainee Ukraine").check()
    setup_en.locator("label").filter(has_text="I consent to the processing").check()
    expect(setup_en.get_by_role("button", name="Send")).to_be_disabled()


def test_empty_form_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("First Name").click()
    setup_en.get_by_placeholder("Last Name").click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_en.get_by_placeholder("Kyiv").click()
    setup_en.get_by_placeholder("Ukraine").click()
    setup_en.locator("//input[@id='discord']").click()
    setup_en.get_by_placeholder("Link to profile").click()
    setup_en.get_by_placeholder("Your answer").click()
    expect(setup_en.get_by_role("button", name="Send")).to_be_disabled()


def test_send_without_checkbox_mw_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("First Name").type("Test")
    setup_en.get_by_placeholder("Last Name").type("Test")
    setup_en.get_by_placeholder("email@gmail.com").fill("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv")
    setup_en.get_by_placeholder("Ukraine").type("Ukraine")
    setup_en.locator("//input[@id='discord']").type("test")
    setup_en.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test")
    setup_en.get_by_placeholder("Your answer").type("test text")
    expect(setup_en.get_by_role("button", name="Send")).to_be_disabled()

