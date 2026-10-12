$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

# Find all occurrences of image filenames and their surrounding context
$imgFiles = Get-ChildItem "$PSScriptRoot\assets\images" | Select-Object -ExpandProperty Name

foreach ($f in $imgFiles) {
    $idx = $content.IndexOf($f)
    if ($idx -ge 0) {
        $start = [Math]::Max(0, $idx - 80)
        $len = [Math]::Min(250, $content.Length - $start)
        $snippet = $content.Substring($start, $len)
        Write-Host "FILE: $f -> $snippet`n"
    }
}
