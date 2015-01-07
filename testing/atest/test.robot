*** Settings ***
Library  Selenium2Library  timeout=2  run_on_failure=Debug
Library  DebugLibrary


*** Variables ***

${SERVER}  http://localhost:5000/
${BROWSER}  PhantomJS
*** Test Cases ***

Scenario: Goto Inbox
    Click Element  id=inbox-link



*** Keywords ***
