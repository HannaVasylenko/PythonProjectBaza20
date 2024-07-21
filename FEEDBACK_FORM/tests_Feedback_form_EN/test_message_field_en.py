from playwright.sync_api import Page, expect


def test_message_empty_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Enter a message")


def test_message_space_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type(" ")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Enter a message")


def test_message_1char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("a")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")


def test_message_2char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("au")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")


def test_message_5char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("tests")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")


def test_message_9char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("technique")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")


def test_message_10char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("techniques")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_11char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("techniquese")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_150char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuioh")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_299char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuio")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_300char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuioW")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_301char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuioWE")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Please limit your message to 300 characters")


def test_message_up_case_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("TESTINGTESTTEST")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_low_case_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("testingtesttest")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_symb_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("Test design techniques !-_().,<>&?@$=+{}#*/[]\|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_numb_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("Your message").type("Test design techniques 1234567890")
    setup_en.get_by_placeholder("email@gmail.com").click()
    expect(setup_en.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
