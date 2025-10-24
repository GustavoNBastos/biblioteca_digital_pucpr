@echo off
REM ---------------------------------------------------
REM Sistema de Gerenciamento de Biblioteca Digital
REM Arquivo de inicialização para usuários finais
REM ---------------------------------------------------

REM Navega até a pasta do projeto (opcional, se já estiver no diretório)
cd /d %~dp0

REM Executa o script Python principal
python main.py

REM Mantém a janela aberta após sair do programa
pause
