*** Settings ***
Library     SeleniumLibrary
Test Setup  Open Browser  browser=chrome
Resource    automationResources.robot
Test Teardown  Close All Browsers


*** Test Cases ***

Scenario Login com usuário inexistente
    Acessar a home page do site automationpractice.com
    Entrar na opção Sign in no cabeçalho da página
    Digitar o email não cadastrado no campo Email address
    Digitar a senha não cadastrada no campo Password
    Clicar no botão Sign in
    Verificação de falha no login
