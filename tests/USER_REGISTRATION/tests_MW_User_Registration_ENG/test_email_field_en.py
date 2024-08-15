from playwright.sync_api import Page, expect


def test_email_empty_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Enter your email")


def test_email_only_space_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type(" ")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Enter your email")


def test_email_cyrillic_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_latin_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_1char_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_2char_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("oa@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_3char_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("oao@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_35char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_49char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_50char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("aqwertyuiopasdfqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_51char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("daqwertyuiopasdfqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_55char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("xasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_56char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("email@gmail.com").fill("dxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_70char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_num_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_symb_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("vi*kt!ria@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_space_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("test test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_numb_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("1234567890@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_hyphen_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("T-est-design-techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_underline_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_point_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_only_symb_in_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("!%?_+*@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_without_first_domain_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anya@gmail.")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_without_name_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_1char_in_first_domain_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anya@gmail.c")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_2char_in_first_domain_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anya@gmail.co")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_without_dot_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anyagmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_incorrect_dot1_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("@anyagmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_incorrect_dot2_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anyagmail.com@")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_2_dots_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("a@nya@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_up_case_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_with_low_case_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("testing@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_with_ru_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text(".ru and .by domains are not allowed")


def test_email_with_by_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text(".ru and .by domains are not allowed")
