*** Settings ***
Library  Selenium2Library

*** Variables ***

${SERVER}  http://localhost:5000/
${BROWSER}  PhantomJS
*** Test Cases ***

Scenario: Title Check
    Goto Main

    Wait Until Element is Visible  css=a.pure-menu-title


*** Keywords ***


Goto Main
    Create Webdriver  ${BROWSER}
    Go to  ${SERVER}
