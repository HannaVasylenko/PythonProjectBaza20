from playwright.sync_api import Page, expect


def test_ff_mandatory_fields_fform_en(setup_en: Page) -> None:
    expect(setup_en.locator("//label[@for='firstName']")).to_have_text("Name *")
    expect(setup_en.locator("//label[@for='email']")).to_have_text("Email *")
    expect(setup_en.locator("//label[@for='message']")).to_have_text("Message *")
    expect(setup_en.get_by_role("button", name="Send")).to_be_visible()
    expect(setup_en.get_by_role("button", name="Send")).to_be_enabled()
    setup_en.get_by_role("heading", name="Feedback form").click()


def test_ff_title_fform_en(setup_en: Page) -> None:
    expect(setup_en.locator("//section[@class='ContactFormSection_section__Afhov']//h2")).to_have_text("Feedback form")
    setup_en.get_by_role("heading", name="Feedback form").click()


def test_ff_active_send_btn_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Test")
    setup_en.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("Your message").type("Test test Test test")
    expect(setup_en.get_by_role("button", name="Send")).to_be_enabled()


def test_ff_hover_send_btn_fform_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Send").hover()


def test_ff_default_send_btn_fform_en(setup_en: Page) -> None:
    expect(setup_en.get_by_role("button", name="Send")).to_be_enabled()


def test_ff_disabled_send_btn_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.get_by_role("button", name="Send")).to_be_disabled()


def test_ff_send_form_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Name").type("Unit test en")
    setup_en.get_by_placeholder("email@gmail.com").type("unittesten@gmail.com")
    setup_en.get_by_placeholder("Your message").type("unit test mes en")
    setup_en.get_by_role("button", name="Send").click()


def test_ff_placeholders_fform_en(setup_en: Page) -> None:
    expect(setup_en.locator("//input[@id='firstName']")).to_have_attribute("placeholder", "Name")
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("placeholder", "email@gmail.com")
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("placeholder", "Your message")
    setup_en.get_by_role("heading", name="Feedback form").click()
