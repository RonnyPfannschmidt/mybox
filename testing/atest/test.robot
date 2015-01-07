*** Settings ***
Library  Selenium2Library  timeout=2  run_on_failure=Debug
Library  DebugLibrary
Test Setup  Goto Main
Test Teardown  Close Browser

*** Variables ***

${SERVER}  http://localhost:5000/
${BROWSER}  PhantomJS
*** Test Cases ***

Scenario: Goto Inbox
    Click Element  id=inbox-link



*** Keywords ***


Goto Main
    Create Webdriver  ${BROWSER}
    Go to  ${SERVER}
    Wait Until Element is Visible  css=a.pure-menu-title
