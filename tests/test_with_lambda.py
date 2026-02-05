from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

import allure

@allure.tag('web')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'seyfiawesome')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name="Testing")


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Клик по полю поиска'):
        s('[aria-label="Search or jump to…"]').click()

    with allure.step('Вводим название репозитория в поиск и кли по Enter'):
        s('input#query-builder-test').type('eroshenkoam/allure-qaguru').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-qaguru')).click()

    with allure.step('Переключаемся на таб issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем название issue по тексту'):
        s(by.text("Заменяем степы на Listener")).should(be.visible)
