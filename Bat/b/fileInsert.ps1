# Original text 
$inputFile1 = "b.html" 
# Text to be inserted 
$inputFile2 = "a\a.html" 
# Output file 
$outputFile = "b1.html" 
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
