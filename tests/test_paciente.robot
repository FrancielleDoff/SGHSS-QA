*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000

*** Test Cases ***
Cadastrar Paciente Com Sucesso
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Input Text    id=nomePaciente    Maria
    Input Text    id=cpfPaciente    12345678901
    Click Button    xpath=//button[contains(text(),"Cadastrar")]

    Sleep    2s
    Page Should Contain    sucesso

    Close Browser