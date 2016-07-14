@echo off
REM stop MPGU perfmon if it works
logman stop MPGU
REM delete any MPGU perfmon counter
logman delete MPGU
REM create MPGU perfmon counter from template
logman import MPGU -xml "MPGU_perfmon_1.xml"
REM start MPGU counter
logman start MPGU
pause