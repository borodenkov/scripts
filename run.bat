@echo off
cd %userprofile%\desktop
fsutil hardlink create 2.iso ubuntu-15.04-desktop-i386.iso
mklink /d 3.iso origin.iso

pause