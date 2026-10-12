$rootDir = Split-Path $PSScriptRoot -Parent
$htmlPath = Join-Path $rootDir "index.html"
$cssPath = Join-Path $rootDir "css\style.css"
$jsAppPath = Join-Path $rootDir "js\app.js"
$jsGalleryPath = Join-Path $rootDir "js\gallery-data.js"

$html = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)
$css = [System.IO.File]::ReadAllText($cssPath, [System.Text.Encoding]::UTF8)
$jsApp = [System.IO.File]::ReadAllText($jsAppPath, [System.Text.Encoding]::UTF8)
$jsGallery = [System.IO.File]::ReadAllText($jsGalleryPath, [System.Text.Encoding]::UTF8)

Write-Host "=== VERIFICAÇÃO DE INTEGRIDADE DO PROJETO STUDIO OLIVEIRA ==="

# 1. Checar referências a imagens locais
$imgMatches = [regex]::Matches($html, 'assets/images/[a-zA-Z0-9_\-\.]+?\.(?:png|jpg|jpeg|webp|svg)')
$galleryMatches = [regex]::Matches($jsGallery, 'assets/images/[a-zA-Z0-9_\-\.]+?\.(?:png|jpg|jpeg|webp|svg)')

$allImgs = @()
foreach ($m in $imgMatches) { $allImgs += $m.Value }
foreach ($m in $galleryMatches) { $allImgs += $m.Value }
$allImgs = $allImgs | Select-Object -Unique

Write-Host "Imagens referenciadas: $($allImgs.Count)"
$missingCount = 0
foreach ($img in $allImgs) {
    $fullPath = Join-Path $rootDir ($img.Replace('/', '\'))
    if (![System.IO.File]::Exists($fullPath)) {
        Write-Host "ALERTA: Imagem ausente: $img"
        $missingCount++
    }
}
if ($missingCount -eq 0) {
    Write-Host "SUCESSO: Todas as $($allImgs.Count) imagens existem no disco e estão válidas!"
}

# 2. Checar presença de proprietários
$hasAndre = $html.Contains("André de Oliveira")
$hasJoao = $html.Contains("João Pedro Santos Barbosa")
Write-Host "Proprietário André de Oliveira presente: $hasAndre"
Write-Host "Proprietário João Pedro Santos Barbosa presente: $hasJoao"

# 3. Checar ausência da antiga equipe
$teamMembers = @("Attila Lira", "Raffa Lourenço", "Paulo Lourenço", "Ricardo Alonso", "Nossa Equipe", "Nossos Tatuadores")
foreach ($member in $teamMembers) {
    $foundInHtml = $html.IndexOf($member, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
    $foundInApp = $jsApp.IndexOf($member, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
    $foundInGallery = $jsGallery.IndexOf($member, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
    if ($foundInHtml -or $foundInApp -or $foundInGallery) {
        Write-Host "FALHA: Antiga menção encontrada: $member"
    } else {
        Write-Host "OK: '$member' removido de todas as áreas públicas."
    }
}

# 4. Checar preservação histórica
$hasSergio = $html.Contains("Sérgio Led")
$has1982 = $html.Contains("1982")
Write-Host "Histórico 1982 preservado: $has1982"
Write-Host "Fundador Sérgio Led's mencionado como marco histórico: $hasSergio"

# 5. Checar contatos e WhatsApp
$hasWhatsapp = $jsApp.Contains("5511944863323") -and $html.Contains("94486-3323")
$hasAddress = $html.Contains("Avenida Ibirapuera, 3478")
Write-Host "WhatsApp oficial 5511944863323 configurado: $hasWhatsapp"
Write-Host "Endereço em Moema configurado: $hasAddress"
