$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

# Find contacts
$contacts = [regex]'(\(?11\)?\s*9?\d{4,5}[-\s]?\d{4}|contato@[^\s"]+|https://api\.whatsapp\.com[^\s"]+|https://wa\.me/[^\s"]+|instagram\.com/[^\s"]+)'
$cMatches = $contacts.Matches($content) | ForEach-Object { $_.Value } | Select-Object -Unique
Write-Host "Contacts and links:"
$cMatches | ForEach-Object { Write-Host $_ }

# Find paragraphs or headings in Portuguese
$ptStrings = [regex]'"([A-ZÁÉÍÓÚÂÊÔÃÕÇ][^"]{20,250})"'
$pMatches = $ptStrings.Matches($content) | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
Write-Host "`nSample text segments (first 40):"
$pMatches | Select-Object -First 40 | ForEach-Object { Write-Host " - $_" }
