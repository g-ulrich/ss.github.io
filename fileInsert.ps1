# Original text 
$inputFile1 = "articles.html" 
# Text to be inserted 
$inputFile2 = "TEMP\articlesIndex.html" 
# Output file 
$outputFile = "articles1.html" 
# Find where the last <!-- insert post --> tag is 
if ((Select-String -Pattern "<!-- insert post -->" -Path $inputFile1 | 
    select -last 1) -match ":(\d+):") 
{ 
    $insertPoint = $Matches[1] 
  # Build up the output from the various parts  
  Get-Content -Path $inputFile1 | select -First $insertPoint | Out-File $outputFile 
  Get-Content -Path $inputFile2 | Out-File $outputFile -Append 
  Get-Content -Path $inputFile1 | select -Skip $insertPoint | Out-File $outputFile -Append 
} 
