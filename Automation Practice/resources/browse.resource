*** Settings ***
Documentation   Browse manipulation keywords


*** Keywords ***
Abrindo o site e validando
    Go To                                ${URL}  #Direcionando para o site definido na variável
    Maximize Browser Window  #maximizando a tela do browser
    Title Should Be                      My Store  #validando se a pagina realmente é a do site desejado