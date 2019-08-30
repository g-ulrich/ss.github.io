@echo off
:LOOP
set /p articletitle="Article Title, without ! ? add it later: "
set /p authorname="Enter author name (e.g. Gabriel Ulrich): "
set /p description="Paste article description here: "
set "source_folder=C:\WEBSITES\ss.github.io\images"
set "result_folder_1=C:\WEBSITES\ss.github.io\images\small-images"
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

for /f "tokens=1-3 delims=:,. " %%A in ("%time%") do (
  set "Hour=%%A"
  set "Min=%%B"
)
set /a Hour = Hour %% 12
if %Hour%==0 set "Hour=12"

set /p ap="Enter AM or PM for time stamp: "

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
echo 							^<article class^="boxArticle post shadow-sm"^> >> %htmlfilename%
echo 							^<a href^="%imghref%" class^="image featured"^>^<img src^="%image%" alt^="%altimg%" /^>^</a^> >> %htmlfilename%
echo								^<div class^="post-author-time"^> >> %htmlfilename%
echo								^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<aside class^="float-right"^>%monthname% %MaS%^<sup^>%ending%^</sup^>^<time^> %Hour%:%Min% %ap%^</time^>^</aside^>^</div^> >> %htmlfilename%
echo								^<section class^="info"^> >> %htmlfilename%
echo								^<header^> >> %htmlfilename%
echo                                    ^<h1^>%articletitle%^</h1^> >> %htmlfilename%
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
echo								^</section^> >> %htmlfilename%
echo 							^</article^> >> %htmlfilename%
echo 						^</div^> >> %htmlfilename%
echo 						^<^!-- Sidebar --^> >> %htmlfilename%
echo 						^<div class^="col-4 col-12-medium"^> >> %htmlfilename%
echo 							^<section class^="boxSide o-h mb-4" itemscope^> >> %htmlfilename%
echo 								^<header style^="padding:20px"^> >> %htmlfilename%
echo 									^<h4^>Search Articles:^</h4^> >> %htmlfilename%
echo 										^<input style^="width:100%%" id^="articleSearch" type^="text" placeholder^="Auto Search..."^> >> %htmlfilename%
echo 								^</header^> >> %htmlfilename%
echo 								^<ul id^="articleList" style^="margin:20px"^> >> %htmlfilename%
echo 									^<div id^="web-rightSideBar"^>^</div^> >> %htmlfilename%
echo 								^</ul^> >> %htmlfilename%
echo 							^</section^> >> %htmlfilename%
echo							^<section class^="boxSide"^> >> %htmlfilename%
echo								^<header style^="padding:20px"^> >> %htmlfilename% 
echo									^<h4^>Resources:^</h4^> >> %htmlfilename%
echo								^</header^> >> %htmlfilename%
echo							^<aside^> >> %htmlfilename%
echo								^<ul style^="padding:20px"^> >> %htmlfilename%
echo									^<div id^="web-resources"^>^</div^> >> %htmlfilename%
echo								^</ul^> >> %htmlfilename%
echo							^</aside^> >> %htmlfilename%
echo							^</section^> >> %htmlfilename% 
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
echo 		^<script src^="js/post.js"^>^</script^> >> %htmlfilename%
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
set articlesHomeSearch=articlesHomeSearch
set ext=.html
set tempHomeSearch=TEMP/articlesHomeSearch%ext%
set homeSearchTrash=articles1%ext%


:start3
echo CHOOSE WHICH COLUMN IN ARTICLES HOME SEARCH:
ECHO 1
ECHO 2
ECHO 3
set articlechoice=
set /p articlechoice=Choose which one you want (e.g. 1, 2, 3):
if not '%articlechoice%'=='' set articlechoice=%articlechoice:~0,1%
if '%articlechoice%'=='1' goto i
if '%articlechoice%'=='2' goto ii
if '%articlechoice%'=='3' goto iii
ECHO "%articlechoice%" is not valid, try again
goto start3


:i
break > %tempHomeSearch%
break > %homeSearchTrash%
@echo ^<li^>^<a class^="search-a" href^="%htmlfileext%" title^="%articletitle%" itemprop^="Article"^>%articletitle%^</a^>^</li^> >> %tempHomeSearch%
Powershell.exe -executionpolicy remotesigned -File col1.ps1
del articles.html
ren articles1%ext% articles.html

goto endSearch
:ii
break > %tempHomeSearch%
break > %homeSearchTrash%
@echo ^<li^>^<a class^="search-a" href^="%htmlfileext%" title^="%articletitle%" itemprop^="Article"^>%articletitle%^</a^>^</li^> >> %tempHomeSearch%
Powershell.exe -executionpolicy remotesigned -File col2.ps1
del articles.html
ren articles1%ext% articles.html

goto endSearch
:iii
break > %tempHomeSearch%
break > %homeSearchTrash%
@echo ^<li^>^<a class^="search-a" href^="%htmlfileext%" title^="%articletitle%" itemprop^="Article"^>%articletitle%^</a^>^</li^> >> %tempHomeSearch%
Powershell.exe -executionpolicy remotesigned -File col3.ps1
del articles.html
ren articles1%ext% articles.html

goto endSearch
:endSearch
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
set "postdescriptor=^<i class^="fas fa-newspaper"^>^</i^> Article^</div^>"
goto end

:video
set "postdescriptor=^<i class^="fab fa-youtube"^>^</i^> Video^</div^>"
goto end

:audio
set "postdescriptor=^<i class^="fas fa-volume-up"^>^</i^> Audio^</div^>"
goto end

:pictures
set "postdescriptor=^<i class^="fas fa-images"^>^</i^> Pictures^</div^>"
goto end

:random
set "postdescriptor=^<i class^="fas fa-comment-alt"^>^</i^> Random^</div^>"
goto end
:end




:start1
echo CHOOSE YOUR POST STYLE:
ECHO 1. With Image - Long
ECHO 2. No Image - Long 
set articlechoice=
set /p postchoice=Choose which one you want (e.g. 1, 2):
if not '%postchoice%'=='' set postchoice=%postchoice:~0,1%
if '%postchoice%'=='1' goto wimage
if '%postchoice%'=='2' goto nimage
ECHO "%postchoice%" is not valid, try again
goto start1


:nimage
@echo ^<article class^="bl-b mb-4"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="position-relative"^> >> %articleIndex%
echo				^<div class^="post-title"^> >> %articleIndex%
echo						^<div class^="post-bg"^>^<div class^="article-descriptor-n-img"^>%postdescriptor%^</div^> >> %articleIndex%
echo					^<div^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<aside class^="float-right"^>%monthname% %MaS%^<sup^>%ending%^</sup^>^<time^> %Hour%:%Min% %ap%^</time^>^</aside^> >> %articleIndex% 					
echo					^</div^> >> %articleIndex%						
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%



goto end1
:wimage
@echo ^<article class^="mb-4 lightBorder"^> >> %articleIndex%
echo    ^<a href^="%htmlfileext%"^> >> %articleIndex%
echo 		^<div class^="row position-relative"^> >> %articleIndex%
echo			^<img class^="col-3 col-4-medium o-cover" src^="%image%"alt="%altimg%"/^> >> %articleIndex%
echo			^<div class^="article-descriptor"^>%postdescriptor% >> %articleIndex%
echo				^<div class^="post-title col-9 col-8-medium"^> >> %articleIndex%
echo					^<div class^="article-d-none"^> ^<h3^>%articletitle%^</h3^> >> %articleIndex%
echo						^<p^>%description%^</p^> >> %articleIndex% 
echo					^</div^> >> %articleIndex%
echo 					^<div class^="article-author-time"^> >> %articleIndex% 
echo						^<img class^="author-icon" src^="%authorImage%"alt^="%altimg2%"/^> %authorname% ^<aside class^="float-right"^>%monthname% %MaS%^<sup^>%ending%^</sup^>^<time^> %Hour%:%Min% %ap%^</time^>^</aside^>^</div^> >> %articleIndex% 
echo				^</div^> >> %articleIndex%
echo			^</div^> >> %articleIndex%
echo 	^</a^> >> %articleIndex%
echo ^</article^> >> %articleIndex%



goto end1
:end1


set filename=articles
set ext=.html
set inputfile=%filename%%ext%
break > %filename%1%ext%
Powershell.exe -executionpolicy remotesigned -File fileInsert.ps1
del "%inputfile%"
ren %filename%1%ext% %inputfile%
timeout /t 2

break > %filename%1%ext%
Powershell.exe -executionpolicy remotesigned -File utf8.ps1
del "%inputfile%"
ren %filename%1%ext% %inputfile%
echo COMPLETED...
pause
