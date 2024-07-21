import re
from playwright.sync_api import Page, expect


def test_message_empty_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").click()
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wpisz wiadomość")


def test_message_space_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type(" ")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wpisz wiadomość")


def test_message_1char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")


def test_message_2char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ęŁ")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")


def test_message_5char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ężŚwę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")


def test_message_9char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ężŚwęŁóżż")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")


def test_message_10char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ężŚwęŁóżęż")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_11char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ężŚwęŁóżęża")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_150char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_299char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszę")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_300char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_301char_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęża")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Prosimy o ograniczenie wiadomości do 300 znaków")


def test_message_up_case_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("ŚŁBTESTINGTEST")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_low_case_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("więtosławasławukaszożena")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_symb_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("Świętosław Lasław Łukasz !-_().,<>&?@$=+{}#*/[]\|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_numb_fform_pl(setup_pl: Page) -> None:
    setup_pl.get_by_placeholder("Twoja wiadomość").type("Świętosław Lasław Łukasz 0123456789")
    setup_pl.get_by_placeholder("email@gmail.com").click()
    expect(setup_pl.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
