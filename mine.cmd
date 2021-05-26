echo Mining Gauntlet...
@echo off
:x
curl --location --request POST "localhost:5000/mine"
goto x