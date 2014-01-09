@echo off

IF NOT EXIST "c:\pyx" GOTO ONE
COPY /Y diffmov.py c:\pyx\
COPY /Y diffmov.py c:\pyx\diffmove.py
COPY /Y diffmov.py c:\pyx\diffrm.py
COPY /Y diffmov.py c:\pyx\diffdel.py

:ONE
MKDIR "c:\pyx"
COPY /Y diffmov.py c:\pyx\
COPY /Y diffmov.py c:\pyx\diffmove.py
COPY /Y diffmov.py c:\pyx\diffrm.py
COPY /Y diffmov.py c:\pyx\diffdel.py
GOTO END


:END