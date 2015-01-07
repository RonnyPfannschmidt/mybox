*** Settings ***
Library  Selenium2Library

*** Variables ***

${server}  http://localhost:5000/

*** Test Cases ***

Scenario: test
    Create Webdriver  PhantomJS
    Go to  ${server}

