*** Settings ***
Library  Selenium2Library  timeout=2  run_on_failure=Debug
Library  DebugLibrary



*** Test Cases ***

Scenario: Goto Inbox
    Click Element  id=inbox-link



*** Keywords ***
