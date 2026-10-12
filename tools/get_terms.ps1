$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

function SearchTerm($term, $maxLen=800) {
    Write-Host "`n=== SEARCH: $term ==="
    $idx = 0
    $count = 0
    while (($idx = $content.IndexOf($term, $idx, [System.StringComparison]::OrdinalIgnoreCase)) -ge 0) {
        $start = [Math]::Max(0, $idx - 50)
        $len = [Math]::Min($maxLen, $content.Length - $start)
        Write-Host "MATCH $count (idx $idx):"
        Write-Host $content.Substring($start, $len)
        $idx += $term.Length + 500
        $count++
        if ($count -ge 3) { break }
    }
}

SearchTerm "laser"
SearchTerm "piercing"
SearchTerm "historia"
SearchTerm "estudio"
