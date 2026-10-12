$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

# Find texts around /laser and /estetica
function PrintSection($route) {
    Write-Host "`n=== ROUTE $route ==="
    $idx = $content.IndexOf("path:`"$route`"")
    if ($idx -lt 0) { $idx = $content.IndexOf("path:`"$route`")") }
    if ($idx -lt 0) { $idx = $content.IndexOf($route) }
    if ($idx -ge 0) {
        $start = [Math]::Max(0, $idx - 50)
        $len = [Math]::Min(1500, $content.Length - $start)
        Write-Host $content.Substring($start, $len)
    }
}

PrintSection "/laser"
PrintSection "/estetica"
PrintSection "/o-estudio"
PrintSection "/orcamento"
PrintSection "/contato"
