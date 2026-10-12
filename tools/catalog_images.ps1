$images = Get-ChildItem "$PSScriptRoot\assets\images" | Select-Object Name, Length | Sort-Object Name
$images | ForEach-Object { "$($_.Name) - $($_.Length) bytes" } | Out-File "$PSScriptRoot\images_list.txt" -Encoding utf8
Write-Host "Total images: $($images.Count)"
