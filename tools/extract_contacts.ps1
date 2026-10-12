$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js")

$reg = [regex]'https://api\.whatsapp\.com[^\s"''\\]+|https://wa\.me/[^\s"''\\]+|instagram\.com/[^\s"''\\]+|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
$matches = $reg.Matches($content)
Write-Host "--- CONTACTS FOUND ---"
$matches | ForEach-Object { $_.Value } | Select-Object -Unique | ForEach-Object { Write-Host $_ }

$regAddress = [regex]'Av[^\."''\\]+Moema[^\."''\\]+'
$matchesAddr = $regAddress.Matches($content)
Write-Host "--- ADDRESS FOUND ---"
$matchesAddr | ForEach-Object { $_.Value } | Select-Object -Unique | ForEach-Object { Write-Host $_ }

$regHours = [regex]'(Ter[^\."''\\]+h|S[aá]b[^\."''\\]+h)'
$matchesHours = $regHours.Matches($content)
Write-Host "--- HOURS FOUND ---"
$matchesHours | ForEach-Object { $_.Value } | Select-Object -Unique | ForEach-Object { Write-Host $_ }
