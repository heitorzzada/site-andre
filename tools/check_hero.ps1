$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)
$f = "686a2fa7-f6db-4d5e-a43d-a1ba6451fd9e.png"
$idx = $content.IndexOf($f)
if ($idx -ge 0) {
    $start = [Math]::Max(0, $idx - 100)
    $len = [Math]::Min(300, $content.Length - $start)
    Write-Host $content.Substring($start, $len)
}
