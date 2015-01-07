*** Settings ***
Library  Selenium2Library  timeout=2
Test Setup  Goto Main
Test Teardown  Close Browser

*** Variables ***

${SERVER}  http://localhost:5000/
${BROWSER}  PhantomJS
*** Test Cases ***

Scenario: Title Check
    Click Element  link=Inbox



*** Keywords ***


Goto Main
    Create Webdriver  ${BROWSER}
    Go to  ${SERVER}
    Wait Until Element is Visible  css=a.pure-menu-title
