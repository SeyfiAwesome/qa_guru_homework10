from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com')

    s('[aria-label="Search or jump to…"]').click()

    s('input#query-builder-test').type('eroshenkoam/allure-qaguru').press_enter()

    s(by.link_text('eroshenkoam/allure-qaguru')).click()

    s('#issues-tab').click()

    s(by.text("Заменяем степы на Listener")).should(be.visible)
