*** Settings ***
Library          RequestsLibrary

*** Variables ***
${URL}    https://baconipsum.com/

*** Test Cases ***
Scenario 01: Teste bacon ipsum Method GET
    ${response}=        GET  ${URL}  expected_status=200
    Log To Console    ${response}

Scenario 02: Teste bacon ipsum Method GET zero paragrafos
    ${response}=        GET  ${URL}  params=paras=0  expected_status=200
    Log To Console    ${response}

Scenario 03: Teste bacon ipsum Method GET mais que 99 paragrafos
    ${response}=        GET  ${URL}  params=paras=100  expected_status=200
    Log To Console    ${response}

Scenario 04: Teste bacon ipsum Method GET inicio com Bacon ipsum dolor amet
    ${response}=        GET  ${URL}  params=paras=0  params=start-with-lorem=1  expected_status=200
    Log To Console    ${response}



