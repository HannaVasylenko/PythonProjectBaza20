from playwright.sync_api import Page, expect


def test_email_empty_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_only_space_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type(" ")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_cyrillic_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_latin_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_1char_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_2char_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("oa@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_3char_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("oao@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_35char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_49char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawseqwertyuiopasdf@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_50char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("sqwertyuiopasdfghjklqqawseqwertyuiopasdf@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_51char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("qsqwertyuiopasdfghjklqqawseqwertyuiopasdf@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_70char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_num_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_symb_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("vi*kt!ria@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_space_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("test test@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_hyphen_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("t-est-design-techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_underline_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_point_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_only_symbols_in_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("!%?_+*@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_first_domain_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anya@gmail.")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_name_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_1char_in_first_domain_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anya@gmail.c")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2char_in_first_domain_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anya@gmail.co")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_without_dot_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anyagmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_incorrect_dot1_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("@anyagmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_incorrect_dot2_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anyagmail.com@")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2_dots_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("a@nya@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_up_case_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_with_low_case_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("testing@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_with_ru_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")


def test_email_with_by_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
