# Original text 
$inputFile1 = "C:\WEBSITES\thecrux.github.io\ss\articles.html" 
# Text to be inserted 
$inputFile2 = "C:\WEBSITES\thecrux.github.io\ss\TEMP\articlesIndex.html" 
# Output file 
$outputFile = "C:\WEBSITES\thecrux.github.io\ss\articles1.html" 
# Find where the last <inputArticle></inputArticle> tag is 
if ((Select-String -Pattern "<inputArticle></inputArticle>" -Path $inputFile1 | 
    select -last 1) -match ":(\d+):") 
{ 
    $insertPoint = $Matches[1] 
  # Build up the output from the various parts  
  Get-Content -Path $inputFile1 | select -First $insertPoint | Out-File $outputFile 
  Get-Content -Path $inputFile2 | Out-File $outputFile -Append 
  Get-Content -Path $inputFile1 | select -Skip $insertPoint | Out-File $outputFile -Append 
} 
