@echo off
rem Onayli tam kampanya CLI baslatici (Jeff -> graft -> Anna -> masa).
rem Cift tiklayarak veya "oyna.bat" yazarak calistir. Ek argumanlar aktarilir:
rem   oyna.bat --seed 7
rem Eski Jeff-only tani modu: oyna.bat --phase-1

chcp 65001 >nul
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [HATA] .venv bulunamadi.
    echo Once sanal ortami kur:
    echo     python -m venv .venv
    echo     .venv\Scripts\python.exe -m pip install -e ".[dev]"
    echo.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" -m game_att2_sim.play_cli %*

echo.
echo --- Oturum bitti. Pencereyi kapatmak icin bir tusa bas. ---
pause >nul
