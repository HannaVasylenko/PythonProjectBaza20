from playwright.sync_api import Page, expect


def test_city_space_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type(" ")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("Enter the name of your city")


def test_city_empty_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").click()
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("Enter the name of your city")


def test_city_1char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("k")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("The name of the city must be at least 2 characters long")


def test_city_2char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("kh")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_3char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("kha")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_15char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("KharkivLvivSumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_29char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrft")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_30char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftq")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_31char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftqs")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("The name of the city should not exceed 30 characters")


def test_city_50char_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("The name of the city should not exceed 30 characters")


def test_city_numbers_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("0123456789")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("Enter the correct city name")


def test_city_hyphen_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("Kh-arkiv-Lviv-Sumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_apostrophe_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("K'harkiv'Lviv'Sumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_space_in_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv Lviv Sumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_symbols_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("K.h@rk!vLv#v?umy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='city']/following-sibling::p")).to_have_text("Enter the correct city name")


def test_city_cyrillic_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("Харків")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_up_case_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("KHARKIV")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_low_case_user_reg_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("kharkiv")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")

