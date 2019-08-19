@echo off
:LOOP
set /p articletitle="Article Title: "
set /p authorname="Enter author name (e.g. Gabriel Ulrich): "
set /p description="Paste article description here: "
set "source_folder=C:\WEBSITES\thecrux.github.io\ss\images"
set "result_folder_1=C:\WEBSITES\thecrux.github.io\ss\images\small-images"
set htmlfile=%articleTitle: =-%
set htmlfileext=%htmlfile%.html
set filepath=common\
set htmlfilename=%htmlfile%.html
set articleIndex=TEMP\articlesIndex.html
break > %htmlfilename%
:loopArticleImage
echo CHOOSE IMAGE FOR ARTICLE: 
set dialog="about:<input type=file id=FILE><script>FILE.click();new ActiveXObject
set dialog=%dialog%('Scripting.FileSystemObject').GetStandardStream(1).WriteLine(FILE.value);
set dialog=%dialog%close();resizeTo(0,0);</script>"
for /f "tokens=* delims=" %%p in ('mshta.exe %dialog%') do set "file=%%p"
For %%A in ("%file%") do (
    Set Name=%%~nxA
)
echo You chose: %Name%
setlocal
:PROMPT
SET /P AREYOUSURE=KEEP PICTURE CHOICE?(Y/[N]): 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO loopArticleImage
goto END7
:END7
endlocal
set "smallImage=%source_folder%\%name%"
echo the full path: %smallImage%
for %%a in ("%smallImage%") do (
   call scale.bat -source "%%~fa" -target "%result_folder_1%\%%~nxa" -max-height 250 
)
set image=images/%Name%
set /p altimg="Alt for the image: "
set altimg=[%altimg%]
set /p imghref="Enter reference link for image (if none enter #): "



::header
@echo ^<^!DOCTYPE html^> > %htmlfilename%
echo ^<html^> >> %htmlfilename%
echo 	^<head^> >> %htmlfilename%
echo 		^<title^>Serving Silent ^| %articletitle% ^</title^> >> %htmlfilename%
echo 		^<^!-- Links --^> >> %htmlfilename%
echo 		^<link rel^="stylesheet" href^="css/main.css"^> >> %htmlfilename%
echo 		^<link rel^="stylesheet" href^="css/header.css"^> >> %htmlfilename%
echo 		^<link rel^="shortcut icon" type^="image/x-icon" href^="images/icon/fishsmall.ico"/^> >> %htmlfilename%
echo 		^<^!-- meta --^> >> %htmlfilename%
echo 		^<meta charset^="UTF-8"^> >> %htmlfilename%
echo 		^<meta name^="viewport" content^="width=device-width, initial-scale=1"^>  >> %htmlfilename%
echo 		^<meta name^="author" content^="%authorname%"^> >> %htmlfilename%
echo 		^<meta name^="description" content^="%description%"^>  >> %htmlfilename%
echo 		^<meta property^="og:url" content^="www.servingsilent.com/%htmlfileext%"^>  >> %htmlfilename%
echo 		^<meta property^="og:image" content^="%altimg%"^>  >> %htmlfilename%
echo 		^<meta property^="og:description" content^="%description%"^>  >> %htmlfilename%
echo 		^<meta property^="og:title" content^="Serving Silent | %articletitle%"^> >> %htmlfilename%
echo 		^<meta property^="og:site_name" content^="Serving Silent | Home"^> >> %htmlfilename%
echo 		^<meta property^="og:see_also" content^="www.ServingSilent.com"^> >> %htmlfilename%
echo 		^<meta name^="twitter:card" content^="Serving Silent | %articletitle%"^> >> %htmlfilename%
echo 		^<meta name^="twitter:url" content^="www.servingsielnt.com/%htmlfileext%"^>  >> %htmlfilename% 
echo 		^<meta name^="twitter:title" content^="Serving Silent | Home"^> >> %htmlfilename%
echo 		^<meta name^="twitter:description"content^="%description%"^> >> %htmlfilename%
echo 		^<meta name^="twitter:image" content^="%altimg%"^> >> %htmlfilename%
echo 	^</head^> >> %htmlfilename% 

:loopAuthorImage
echo CHOOSE AUTHOR IMAGE/ICON FOR POST DESCRIPTION: 
set dialog1="about:<input type=file id=FILE><script>FILE.click();new ActiveXObject
set dialog1=%dialog1%('Scripting.FileSystemObject').GetStandardStream(1).WriteLine(FILE.value);
set dialog1=%dialog1%close();resizeTo(0,0);</script>"
for /f "tokens=* delims=" %%p in ('mshta.exe %dialog1%') do set "file1=%%p"
For %%A in ("%file1%") do (
    Set Name1=%%~nxA
)
echo You chose: %Name1%
set /p altimg2="Enter Author Image alt: "
set altimg2=[%altimg2%]

setlocal
:PROMPT
SET /P AREYOUSURE=KEEP PICTURE CHOICE?(Y/[N]): 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO loopAuthorImage
goto END6
:END6
endlocal

set authorImage=images/icon/authors/%Name1%
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set dt=%%a
set year=%dt:~0,4%
set month=%dt:~4,2%
set day=%dt:~6,2%
if %month%==01 set monthname=January
if %month%==02 set monthname=February
if %month%==03 set monthname=March
if %month%==04 set monthname=April
if %month%==05 set monthname=May
if %month%==06 set monthname=June
if %month%==07 set monthname=July
if %month%==08 set monthname=August
if %month%==09 set monthname=September
if %month%==10 set monthname=October
if %month%==11 set monthname=November
if %month%==12 set monthname=December
Set "ToD=%DATE%"
Set "MoY=%ToD:~-7,2%"
If Not "%MoY:~,1%"=="1" (
    If "%MoY:~-1%"=="1" Set "MaS=%MoY%"&Set "ending=st"
    If "%MoY:~-1%"=="2" Set "MaS=%MoY%"&Set "ending=nd"
    If "%MoY:~-1%"=="3" Set "MaS=%MoY%rd"&Set "ending=rd")
If Not Defined MaS Set "MaS=%MoY%"&Set "ending=th"
If "%MaS:~,1%"=="0" Set "MaS=%MaS:~1%"
::body
echo 	^<body^> >> %htmlfilename%
echo 		^<div id^="page-wrapper"^> >> %htmlfilename%
echo 			^<^!-- Header --^> >> %htmlfilename%
echo 			^<div id^="web-header"^>^</div^> >> %htmlfilename%
echo 			^<^!-- Main --^> >> %htmlfilename%
echo 			^<section id^="main"^> >> %htmlfilename%
echo 				^<div class^="container"^> >> %htmlfilename%
echo 					^<div class^="row"^> >> %htmlfilename%
echo 						^<div class^="col-8 col-12-medium"^> >> %htmlfilename%
echo 							^<^!-- Content --^> >> %htmlfilename%
echo 							^<article class^="boxArticle post"^> >> %htmlfilename%
echo 							^<a href^="%imghref%" class^="image featured"^>^<img src^="%image%" alt^="%altimg%" /^>^</a^> >> %htmlfilename%
echo								^<header^> >> %htmlfilename%
echo                                    ^<h2^>%articletitle%^</h2^> >> %htmlfilename%
echo									^<div class^="article-author-time m-3"^> >> %htmlfilename%
echo									^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname% %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %htmlfilename%
echo                                ^</header^> >> %htmlfilename%

::article content
echo Choose an ARTICLE with ext of .html:
set dialog="about:<input type=file id=FILE><script>FILE.click();new ActiveXObject
set dialog=%dialog%('Scripting.FileSystemObject').GetStandardStream(1).WriteLine(FILE.value);
set dialog=%dialog%close();resizeTo(0,0);</script>"
for /f "tokens=* delims=" %%p in ('mshta.exe %dialog%') do set "file=%%p"
echo The file you chose:
for %%F in ("%file%") do echo %%~nxF
type %file% >> %htmlfilename%



::footer & javascript
echo 							^</article^> >> %htmlfilename%
echo 						^</div^> >> %htmlfilename%
echo 						^<^!-- Sidebar --^> >> %htmlfilename%
echo 						^<div class^="col-4 col-12-medium"^> >> %htmlfilename%
echo 							^<section class^="boxSide o-h" itemscope^> >> %htmlfilename%
echo 								^<header style^="padding:20px"^> >> %htmlfilename%
echo 									^<h4^>Search Articles:^</h4^> >> %htmlfilename%
echo 										^<input style^="width:100%%" id^="articleSearch" type^="text" placeholder^="Auto Search..."^> >> %htmlfilename%
echo 								^</header^> >> %htmlfilename%
echo 								^<ul id^="articleList" style^="margin:20px"^> >> %htmlfilename%
echo 									^<div id^="web-rightSideBar"^>^</div^> >> %htmlfilename%
echo 								^</ul^> >> %htmlfilename%
echo 							^</section^> >> %htmlfilename%
echo 							^<section class^="boxSide"^> >> %htmlfilename%
echo 								^<header style^="padding:20px"^> >> %htmlfilename%
echo 									^<h4^>More...^</h4^> >> %htmlfilename%
echo 								^</header^> >> %htmlfilename%
echo 							^</section^> >> %htmlfilename%
echo 						^</div^> >> %htmlfilename%
echo 					^</div^> >> %htmlfilename%
echo 				^</div^> >> %htmlfilename%
echo 			^</section^> >> %htmlfilename%
echo 			^<^!-- footer --^> >> %htmlfilename% 
echo 			^<div id^="web-footer"^>^</div^> >> %htmlfilename%
echo 		^</div^> >> %htmlfilename%
echo		^<^!-- script --^> >> %htmlfilename%
echo 		^<script src^="js/jquery.min.js"^>^</script^> >> %htmlfilename%
echo 		^<script src^="js/main.js"^>^</script^> >> %htmlfilename%
echo 		^<script src^="js/articleOnLoad.js"^>^</script^> >> %htmlfilename%
echo 	^</body^> >> %htmlfilename%
echo ^</html^> >> %htmlfilename%



::Question to continue
setlocal
:PROMPT
SET /P AREYOUSURE=Continue(Y/[N]): 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END
goto YES
:END
goto NO
endlocal
:NO
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to delete your progress?(Y/[N]): 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END1
goto AREYOUSURE
:END1
goto YES
endlocal
:AREYOUSURE
setlocal
:PROMPT
SET /P AREYOUSURE=Are you sure?(Y/[N]): 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END2
goto DELETE
:END2
goto YES
endlocal
:DELETE
del %htmlfilename%
echo DELETED %htmlfileext%! STARTING OVER IN 3 SECONDS.
goto LOOP
endlocal
:YES
@echo ^<li^>^<a class^="search-a" href^="%htmlfileext%" title^="%articletitle%" itemprop^="Article"^>%articletitle%^</a^>^</li^> >> %filepath%search.html

set image=images/small-images/%Name%
:: clear articlesIndex.html
break > %articleindex%
:start
echo CHOOSE YOUR POST DESCRIPTOR:
ECHO 1. Article
ECHO 2. Video
ECHO 3. Audio
ECHO 4. Pictures
ECHO 5. Random
set articlechoice=
set /p articlechoice=Choose which one you want (e.g. 1, 2, 3, 4, 5):
if not '%articlechoice%'=='' set articlechoice=%articlechoice:~0,1%
if '%articlechoice%'=='1' goto article
if '%articlechoice%'=='2' goto video
if '%articlechoice%'=='3' goto audio
if '%articlechoice%'=='4' goto pictures
if '%articlechoice%'=='5' goto random
ECHO "%articlechoice%" is not valid, try again
goto start

:article
@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium col-12-small o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>^<i class^="fas fa-newspaper"^>^</i^> Article^</div^> >> %articleIndex%
echo				^<div class^="article-title col-9 col-8-medium col-12-small"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname% %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%



goto end
:video
@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium col-12-small o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>^<i class^="fab fa-youtube"^>^</i^> Video^</div^> >> %articleIndex%
echo				^<div class^="article-title col-9 col-8-medium col-12-small"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname% %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%


goto end
:audio
@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium col-12-small o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>^<i class^="fas fa-volume-up"^>^</i^> Audio^</div^> >> %articleIndex%
echo				^<div class^="article-title col-9 col-8-medium col-12-small"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname% %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%



goto end
:pictures
@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium col-12-small o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>^<i class^="fas fa-images"^>^</i^> Pictures^</div^> >> %articleIndex%
echo				^<div class^="article-title col-9 col-8-medium col-12-small"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname% %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%



goto end
:random
@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium col-12-small o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>^<i class^="fas fa-comment-alt"^>^</i^> Random^</div^> >> %articleIndex%
echo				^<div class^="article-title col-9 col-8-medium col-12-small"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<time^>%monthname% %MaS%^<sup^>%ending%^</sup^>^</time^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%

goto end
:end

set filename=articles
set ext=.html
set inputfile=%filename%%ext%
break > %filename%1%ext%
Powershell.exe -executionpolicy remotesigned -File fileInsert.ps1
echo deleting articles.html
del "%inputfile%"
echo renaming articles1.html to articles.html
ren %filename%1%ext% %inputfile%
echo COMPLETED MAKING ARTICLE FOR ARTICLES.HTML...
pause
