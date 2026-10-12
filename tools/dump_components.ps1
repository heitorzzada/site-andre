$content = [System.IO.File]::ReadAllText("$PSScriptRoot\bundle.js", [System.Text.Encoding]::UTF8)

function DumpComponent($name) {
    Write-Host "`n=== DUMP COMPONENT $name ==="
    $regex = [regex]"function\s+$name\s*\("
    $m = $regex.Match($content)
    if (!$m.Success) {
        $regex = [regex]"const\s+$name\s*="
        $m = $regex.Match($content)
    }
    if ($m.Success) {
        $idx = $m.Index
        $len = [Math]::Min(2500, $content.Length - $idx)
        Write-Host $content.Substring($idx, $len)
    } else {
        Write-Host "Not found $name"
    }
}

DumpComponent "C3" # laser
DumpComponent "j3" # estetica
DumpComponent "n3" # orcamento
DumpComponent "r3" # contato
DumpComponent "OI" # o-estudio
DumpComponent "AV" # historia
