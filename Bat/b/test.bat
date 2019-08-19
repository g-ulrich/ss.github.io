@echo off
set articleIndex=a\a.html
break > %articleIndex%

@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium col-12-small o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>^<i class^="fas fa-comment-alt"^>^</i^> Random34454^</div^> >> %articleIndex%
echo				^<div class^="article-title col-9 col-8-medium col-12-small"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname%, %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%




set filename=b
set ext=.html
set inputfile=%filename%%ext%
break > %filename%1%ext%
Powershell.exe -executionpolicy remotesigned -File  C:\WEBSITES\thecrux.github.io\ss\Bat\b\fileInsert.ps1
del "%inputfile%"
ren C:\WEBSITES\thecrux.github.io\ss\Bat\b\%filename%1%ext% %inputfile%
pause