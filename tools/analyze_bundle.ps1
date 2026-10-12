$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

# Find React Router routes (e.g., path: "/...")
$routes = [regex]'path\s*:\s*["'']([^"'']+)["'']'
$rMatches = $routes.Matches($content) | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
Write-Host "Routes found:"
$rMatches | ForEach-Object { Write-Host $_ }

# Search for mentions of "Led"
$ledsMentions = [regex]'[^.?!;"]{0,60}Led[^.?!;"]{0,60}'
$lMatches = $ledsMentions.Matches($content) | ForEach-Object { $_.Value.Trim() } | Select-Object -Unique
Write-Host "`nSample Led mentions: $($lMatches.Count)"
$lMatches | Select-Object -First 15 | ForEach-Object { Write-Host $_ }
