*** Settings ***
Library  Selenium2Library  timeout=2
Library  DebugLibrary



*** Test Cases ***

Scenario: Goto Inbox
    Given  The User Clicks inbox in the Mainmenu

*** Keywords ***

The User Clicks ${name} in the Mainmenu
    Click Element  id=${name}-link
