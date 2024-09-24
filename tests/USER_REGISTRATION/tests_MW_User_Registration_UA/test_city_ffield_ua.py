import pytest
from playwright.sync_api import Page, expect


def test_city_space_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type(" ")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Введіть назву вашого міста")


def test_city_empty_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").click()
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Введіть назву вашого міста")


def test_city_1char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("х")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Назва міста повинна бути не менше 2 знаків")


def test_city_2char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ха")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_3char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("хар")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_15char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ХарківЛьвівСуми")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_29char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворів")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_30char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворівю")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_31char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворівюа")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Назва міста повинна бути не більше 30 знаків")


def test_city_50char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворівШепетівкаЧорнобильРим")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Назва міста повинна бути не більше 30 знаків")


def test_city_numbers_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("0123456789")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Введіть коректну назву міста")


def test_city_hyphen_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("Ха-рків-Львів-Суми")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_apostrophe_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("Х'арків'Львів'Суми")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_space_in_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("Харків Львів Суми")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_symbols_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("Х,ар.кі!вЛ?ьв@ів")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='city']/following-sibling::p")).to_have_text("Введіть коректну назву міста")


def test_city_latin_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("Kharkiv")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_up_case_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("ХАРКІВ")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_city_low_case_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").type("харків")
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_piletters_user_reg_ua(setup: Page, test_input) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Київ").press("Control+A")
    setup.get_by_placeholder("Київ").press("Delete")
    setup.get_by_placeholder("Київ").type(test_input)
    setup.get_by_placeholder("Україна").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")

