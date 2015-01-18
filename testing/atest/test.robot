*** Settings ***
Library  Selenium2Library  timeout=2
Library  DebugLibrary



*** Test Cases ***

Scenario: Goto Inbox
    Given the User Clicks inbox in the Mainmenu
    Then the Mailboxes are visible

*** Keywords ***

the User Clicks ${name} in the Mainmenu
    Click Element  id=${name}-link


the Mailboxes are visible
    Page Should Contain  wut
