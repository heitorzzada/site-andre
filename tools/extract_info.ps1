$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

# Find all lovable-uploads or image URLs
$regex = [regex]'/(lovable-uploads/[a-zA-Z0-9_\-\.]+?\.(?:png|jpg|jpeg|webp|svg))'
$matches = $regex.Matches($content)
$imageUrls = $matches | ForEach-Object { $_.Value } | Select-Object -Unique

Write-Host "Total images found: $($imageUrls.Count)"
$imageUrls | ForEach-Object { Write-Host $_ }

# Find text mentions of pages/routes/services
$services = [regex]'(Tatuagem|Piercing|Remoção|Laser|Realismo|Fineline|Blackwork|Oriental|Old School|Geek)[^"\,\}\]]*'
$sMatches = $services.Matches($content) | ForEach-Object { $_.Value } | Select-Object -Unique
Write-Host "`nSample services/styles found: $($sMatches.Count)"
$sMatches | Select-Object -First 20 | ForEach-Object { Write-Host $_ }
