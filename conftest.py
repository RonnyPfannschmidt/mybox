import pytest


@pytest.fixture()
def browser(request, tmpdir):
    import selenium.webdriver
    browser = selenium.webdriver.PhantomJS()
    print(dir(request))
    request.node._browser = browser
    browser.screenshotdir = tmpdir.ensure('screens', dir=1)

    return browser


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    browser = getattr(item, 'browser', None)
    if rep.when == "call" and rep.failed and browser:
        target = item.browser.screenshotdir.join('_failure.png')
        item.browser.get_screenshot_as_file(target.strpath)
        rep.sections.append(('screenshot', str(target)))
    return rep
