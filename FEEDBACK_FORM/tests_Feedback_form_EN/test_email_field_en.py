from playwright.sync_api import Page, expect


def test_email_empty_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Enter your email")


def test_email_space_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type(" ")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Enter your email")


def test_email_cyrillic_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_latin_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_1char_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_2char_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("au@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_3char_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("oon@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_25char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("designtechnique@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_50char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_51char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_70char_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_numb_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_up_case_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_symb_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("v?i*kt!ri,a@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_hyphen_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("T-est-design-techniques@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_underline_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_point_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_space_in_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("Test design@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_without_first_domain_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("test@gmail.")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_without_name_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_1char_in_first_domain_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("test@gmail.c")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_2char_in_first_domain_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("test@gmail.co")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_without_dot_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("testgmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_incorrect_dot1_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("@testgmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_incorrect_dot2_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("testgmail.com@")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_2_dots_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("t@est@gmail.com")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_ru_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text(".ru and .by domains are not allowed")


def test_email_with_by_fform_en(setup_en: Page) -> None:
    setup_en.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup_en.get_by_placeholder("Your message").click()
    expect(setup_en.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text(".ru and .by domains are not allowed")
