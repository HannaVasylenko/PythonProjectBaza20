from playwright.sync_api import Page, expect


def test_motivation_empty_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").click()
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Podaj swoją motywację")


def test_motivation_space_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type(" ")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Podaj swoją motywację")


def test_motivation_1char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ę")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motivation_2char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óę")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motivation_5char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁęża")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motivation_9char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁężaóŁęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motivation_10char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁężaóŁężd")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_11char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁężaóŁężd")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m")


def test_motivation_20char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętoławRóżaWięcław")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_49char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukszęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_50char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_51char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęża")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst nie powinien przekraczać 50 znaków")


def test_motivation_70char_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqqwertyuiopasdfghjklp")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst nie powinien przekraczać 50 znaków")


def test_motivation_symb1_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("s!-_().,<>&?@$=+{}#*/[\]")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_symb2_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("s|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_num_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("num1234567890")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_up_case_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚŁŻABCD")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motivation_low_case_user_reg_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ógłażejukaszęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
