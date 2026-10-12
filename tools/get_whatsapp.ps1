$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js")
$idx = $content.IndexOf("api.whatsapp.com")
if ($idx -ge 0) {
    $start = [Math]::Max(0, $idx - 500)
    $len = [Math]::Min(1000, $content.Length - $start)
    Write-Host "--- AROUND WHATSAPP ---"
    Write-Host $content.Substring($start, $len)
}
