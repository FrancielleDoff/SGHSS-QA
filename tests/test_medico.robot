*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000

*** Test Cases ***
Cadastrar Medico Com Sucesso
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    id=nomeMedico    Dr João
    Input Text    id=especialidadeMedico    Cardiologia
    Click Button    Cadastrar
    Page Should Contain    sucesso
    Sleep    2
    Close Browser
