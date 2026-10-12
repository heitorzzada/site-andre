$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js")

# Let's search for Laser and Estetica texts
function SearchAround($term, $maxLen=1200) {
    Write-Host "`n=================== SEARCH: $term ==================="
    $idx = 0
    while (($idx = $content.IndexOf($term, $idx)) -ge 0) {
        $start = [Math]::Max(0, $idx - 100)
        $len = [Math]::Min($maxLen, $content.Length - $start)
        Write-Host "FOUND AT $idx :"
        Write-Host $content.Substring($start, $len)
        $idx += $term.Length + 1000
    }
}

SearchAround "Laser CO₂"
SearchAround "Remoção a Laser"
SearchAround "Tatuagem Estética Reparadora"
