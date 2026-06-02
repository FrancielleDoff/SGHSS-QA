*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000

*** Test Cases ***
Agendar Consulta Com Sucesso
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Input Text    id=dataConsulta    2026-05-20
    Input Text    id=horario    14:00
    Input Text    id=pacienteId    1

    Select From List By Index    id=medicoId    1

    Click Button    xpath=//button[contains(text(),"Agendar")]

    Sleep    2s
    Page Should Contain    sucesso

    Close Browser