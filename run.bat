@echo off
chcp 65001 >nul 2>&1
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

REM ARQV30 Enhanced v2.0 ULTRA-ROBUSTO - Script de Execução Windows
REM Execute este arquivo para iniciar a aplicação

echo ==========================================
echo ARQV30 Enhanced v2.0 ULTRA-ROBUSTO
echo Analise Ultra-Detalhada de Mercado
echo ==========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERRO: Python não encontrado!
    echo Por favor, execute install.bat primeiro.
    pause
    exit /b 1
)

REM Verifica se está no diretório correto
if not exist "src\run.py" (
    echo ❌ ERRO: Arquivo run.py não encontrado!
    echo Certifique-se de estar no diretório correto do projeto.
    pause
    exit /b 1
)

REM Ativa ambiente virtual se existir
if exist "venv\Scripts\activate.bat" (
    echo 🔄 Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo ⚠️ AVISO: Ambiente virtual não encontrado.
    echo Recomendamos executar install.bat primeiro.
    echo.
)

REM Verifica se arquivo .env existe
if not exist ".env" (
    echo AVISO: Arquivo .env nao encontrado!
    echo Copie o arquivo .env.example para .env e configure suas chaves de API.
    echo.
) else (
    echo Arquivo .env encontrado - APIs configuradas
)

REM Navega para o diretório src
cd src

REM Verifica dependências críticas
echo Verificando dependencias criticas...
python -c "import flask, requests, google.generativeai, supabase" >nul 2>&1
if errorlevel 1 (
    echo ERRO: Dependencias faltando! Execute install.bat
    pause
    exit /b 1
)

REM Inicia a aplicação
echo.
echo Iniciando ARQV30 Enhanced v2.0 ULTRA-ROBUSTO...
echo.
echo Servidor: http://localhost:5000
echo Interface: Analise Ultra-Detalhada de Mercado
echo IA: Google Gemini Pro + HuggingFace
echo Pesquisa: WebSailor + Google Search + Jina AI
echo Banco: Supabase PostgreSQL
echo.
echo RECURSOS ATIVADOS:
echo - Analise com multiplas IAs
echo - Pesquisa web profunda
echo - Processamento de anexos inteligente
echo - Geracao de relatorios PDF
echo - Avatar ultra-detalhado
echo - Drivers mentais customizados
echo - Analise de concorrencia profunda
echo.
echo Pressione Ctrl+C para parar o servidor
echo ==========================================
echo.

python run.py

REM Volta para o diretório raiz
cd ..

echo.
echo ==========================================
echo Aplicacao ULTRA-ROBUSTA encerrada.
echo ==========================================
echo.
echo Para reiniciar, execute run.bat novamente
echo Para reconfigurar, execute install.bat
echo.
pause