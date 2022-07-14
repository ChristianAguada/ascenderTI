*** Settings ***


*** Variables ***
${URL}                      http://automationpractice.com/index.php
${SIGNIN}                   //a[@class='login'][contains(.,'Sign in')]
${EMAILNAOCADASTRADO}       christian00000@bloob.com
${SENHANAOCADASTRADA}       0000000
${TITULOPAGINALOGIN}        Login - My Store
${VALIDAPAGINALOGIN}        //h1[@class='page-heading'][contains(.,'Authentication')]
${VALIDAPAGINALOGIN2}       //h3[@class='page-subheading'][contains(.,'Create an account')]
${VALIDAAUTENTICACAO}       //li[contains(.,'Authentication failed.')]


*** Keywords ***


Acessar a home page do site automationpractice.com
    Go To                               ${URL}
    Maximize Browser Window
    Sleep  2s

Entrar na opção Sign in no cabeçalho da página
    Click Element                       locator=${SIGNIN}
    Title Should Be                     ${TITULOPAGINALOGIN}
    Page Should Contain Element         locator=${VALIDAPAGINALOGIN}
    Page Should Contain Element         locator=${VALIDAPAGINALOGIN2}
    Sleep  2s

Digitar o email não cadastrado no campo Email address
    Wait Until Element Is Visible        id=email
    Input Text                           id=email    ${EMAILNAOCADASTRADO}

Digitar a senha não cadastrada no campo Password
    Input Text                          id=passwd    ${SENHANAOCADASTRADA}

Clicar no botão Sign in
    Click Button                        id=SubmitLogin

Verificação de falha no login
    Wait Until Element Is Visible       locator=${VALIDAAUTENTICACAO}
    Title Should Be                     ${TITULOPAGINALOGIN}
    Page Should Contain Element         locator=${VALIDAAUTENTICACAO}