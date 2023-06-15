import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):
    
    # Arrange
    page.goto('https://demo.applitools.com')

    # Act
    page.locator('id=username').fill('aulia')
    page.locator('id=password').fill('Asyx436!!')
    page.locator('id=log-in').click()
    