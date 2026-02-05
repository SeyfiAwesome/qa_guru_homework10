from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

import allure

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'seyfiawesome')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name="Testing")


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Клик по полю поиска')
def search_field_click():
    s('[aria-label="Search or jump to…"]').click()

@allure.step('Вводим название репозитория {repo} в поиск и кли по Enter')
def repository_searching(repo):
    s('input#query-builder-test').type(repo).press_enter()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Перключаемся на таб issue')
def open_tab_issue():
    s('#issues-tab').click()

@allure.step('Проверяем issue по тексту {issue_text}')
def check_issue_by_text(issue_text):
    s(by.text(issue_text)).should(be.visible)

def test_with_decorators_step():
    open_main_page()
    search_field_click()
    repository_searching('eroshenkoam/allure-qaguru')
    go_to_repository("eroshenkoam/allure-qaguru")
    open_tab_issue()
    check_issue_by_text("Заменяем степы на Listener")


