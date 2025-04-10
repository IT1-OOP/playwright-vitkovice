import pytest
from pathlib import Path

def test_elementy_html(page):
    index_path = Path(__file__).parent.parent / "index.html"
    page.goto(index_path.as_uri())
    assert page.locator("div.container").is_visible()
    assert page.locator("div.container").is_visible()
    assert page.locator("div.container-2").is_visible()
    assert page.locator("h1:has-text('Nadpis 1')").is_visible()
    assert page.locator("h1:has-text('Nadpis 2')").is_visible()
    assert page.locator(".nadpis").is_visible()

    link = page.locator("a#w3link")
    assert link.is_visible()
    assert link.inner_text() == "Navštiv W3Schools"

    with page.expect_popup() as popup_info:
        link.click()
    popup = popup_info.value
    assert "w3schools" in popup.url
