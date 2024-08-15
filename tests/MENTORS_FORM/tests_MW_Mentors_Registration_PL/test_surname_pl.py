from playwright.sync_api import Page, expect


def test_surname_empty_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").click()
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Wpisz swoje nazwisko")


def test_surname_space_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type(" ")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Wpisz swoje nazwisko")


def test_surname_1char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("ę")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Nazwisko musi mieć co najmniej 2 znaki")


def test_surname_2char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("ęż")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_3char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Łęż")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_25char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("ŚwiętosławRóżaWięcławBłaż")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_49char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża Więcław BłażejChwalibógBłażejŁuka")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_50char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża Więcław BłażejChwalibógBłażej Łuka")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_51char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław Róża Więcław BłażejChwalibóg Błażej Łuka")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Nazwisko nie może przekraczać 50 znaków")


def test_surname_76char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłaże")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Nazwisko nie może przekraczać 50 znaków")


def test_surname_apostrophe_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Ś'więtosław'Róża'Więcław")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_hyphen_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Ś-więtosław-Róża-Więcław")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_numb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Świętosław1234567890")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Wpisz poprawne nazwisko")


def test_surname_symbols_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Ś_w,ię.to!sła@wRó?ża")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Wpisz poprawne nazwisko")


def test_surname_cyrillic_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("Тестування")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_low_case_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("więtosław")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_up_case_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("ŚŁABCDE")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_space_in_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("Nazwisko").type("więtosław więtosław więtosław")
    setup_pl.get_by_role("textbox", name="Imię", exact=True).click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")
