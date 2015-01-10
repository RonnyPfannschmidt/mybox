*** Settings ***
Documentation   Mybox Acceptance Testsuite
Library  Selenium2Library  timeout=2
Library  DebugLibrary

Suite Setup  Goto Main
Suite Teardown  Close Browser

*** Variables ***

${SERVER}  http://localhost:5000/
${BROWSER}  PhantomJS


** Keywords **


Goto Main
    Create Webdriver  ${BROWSER}
    Go to  ${SERVER}
    Wait Until Element is Visible  css=a.pure-menu
