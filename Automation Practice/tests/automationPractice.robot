*** Settings ***
Library     SeleniumLibrary  #importando a biblioteca Selenium
Test Setup  Open Browser  browser=chrome  #comando para sempre executar o open browser antes de qualquer teste
#Test Teardown  Close All Browsers
Library  FakerLibrary  #biblioteca para gerar aleatoriamente um email

Resource                                ../resources/browse.resource
Resource                                ../resources/validation.resource
Resource                                ../resources/checkout.resource


*** Variables ***
${URL}   http://www.automationpractice.com/  ##boa pratica usar variaveis em maiusculo


*** Test Cases ***
Scenario 01: Open Site and buy
    [Tags]  open
    ${EMAIL} =                           FakerLibrary.Email
    #${FIRST_NAME} =                     FakerLibrary.first_name
    #${LAST_NAME} =                      FakerLibrary.last_name
    ${PHONE_NUMBER} =                    FakerLibrary.phone_number
    ${ZIPCODE} =                         FakerLibrary.Zipcode

    Abrindo o site e validando
    Pesquisando item e validando
    Selecionando o item                         
    Procedendo com o checkout
    Cadastrando email                   ${EMAIL}
    Preenchendo cadastro                ${ZIPCODE}
    Aceitando o termo e processando a compra
    

*** Keywords ***





    
    
    #Click Link  http://automationpractice.com/index.php?controller=order

#Scenario 02: Open Site and clear cart
 #   [Tags]  cart
  #  Go To  ${URL}  #Direcionando para o site definido na variável
   # Maximize Browser Window  #maximizando a tela do browser
    #Title Should Be  My Store  #validando se a pagina realmente é a do site desejado
    #Click Element  xpath=//a[@title = 'View my shopping cart']
    


# exemplo comando xpath para o console do chrome: $x("//a[@title = 'Proceed to checkout']")

#pip install robotframework-faker

    
    
    
    