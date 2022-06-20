*** Settings ***
Documentation   Checkout feature keywords

*** Keywords ***

Pesquisando item e validando
    Input Text                           name=search_query  Short  #Escrevendo o texto short no campo de pesquisa
    Submit Form  #submetendo a pesquisa
    Page Should Contain                  Faded Short Sleeve T-shirts  #Verificando se a pagina possui o produto pretendido
    #Wait Until Element Is Visible       title=Faded Short Sleeve T-shirts timeout=30
    
Selecionando o item
    Click Element                        xpath=//a[@title = 'Blouse']  #Referenciando por xpath o elemento que precisamos que clique
    Click Button                         name=Submit  #Clicando no botão que tem nome de Submit
    
Procedendo com o checkout
    Wait Until Element Is Visible        xpath=//a[@title = 'Proceed to checkout']  #Esperando o botão do checkout aparecer
    Click Element                        xpath=//a[@title = 'Proceed to checkout']  #Clicando no elemento referenciado por xpath
    Wait Until Element Is Visible        xpath=//a[@class = 'button btn btn-default standard-checkout button-medium']
    Click Element                        xpath=//a[@class = 'button btn btn-default standard-checkout button-medium']

Cadastrando email
    [Arguments]                          ${EMAIL}
    Input Text                           id=email_create  ${EMAIL}
    Click Element                        xpath=//button[@id = 'SubmitCreate']
    
Preenchendo cadastro
    [Arguments]                          ${ZIPCODE}
    Wait Until Element Is Visible        name=customer_firstname
    Click Element                        xpath=//input[@id = 'id_gender1']
    Input Text                           name=customer_firstname  Christian
    Input Text                           id=customer_lastname  Aguada
    Input Text                           id=passwd  12345
    Input Text                           id=company  AscenderTI
    Input Text                           id=address1  Rua Coronel Corte Real
    Input Text                           id=address2  975
    Input Text                           id=city  Porto Alegre
    Select From List By Value            id=days    6
    Select From List By Value            id=months    7
    Select From List By Value            id=years    1989
    Select From List By Label            id=id_state    Alabama
    Input Text                           id=postcode   ${ZIPCODE}
    Input Text                           id=phone  123456
    Click Button                         id=submitAccount
    Click Element                        xpath=//button[@name = 'processAddress']

Aceitando o termo e processando a compra
    Click Element                        id=cgv
    Click Element                        xpath=//button[@name = 'processCarrier']
    Click Element                        xpath=//a[@class = 'bankwire']
    Click Element                        xpath=//button[@class = 'button btn btn-default button-medium']

