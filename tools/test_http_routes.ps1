$urls = @(
    "http://localhost:8080/",
    "http://localhost:8080/index.html",
    "http://localhost:8080/css/style.css",
    "http://localhost:8080/js/app.js",
    "http://localhost:8080/js/gallery-data.js",
    "http://localhost:8080/assets/images/686a2fa7-f6db-4d5e-a43d-a1ba6451fd9e.png",
    "http://localhost:8080/assets/images/paulo-tattoo-1.jpeg",
    "http://localhost:8080/assets/images/raffa-tattoo-1.jpeg",
    "http://localhost:8080/assets/images/attila-tattoo-1.png",
    "http://localhost:8080/assets/images/992cd6c5-5939-4eb1-9173-1e98744b2961.png",
    "http://localhost:8080/robots.txt",
    "http://localhost:8080/sitemap.xml"
)

Write-Host "=== TESTE DE ROTAS HTTP NO SERVIDOR LOCAL ==="

$allOk = $true
foreach ($url in $urls) {
    try {
        $req = [System.Net.WebRequest]::Create($url)
        $req.Timeout = 4000
        $res = $req.GetResponse()
        $status = [int]$res.StatusCode
        $type = $res.ContentType
        $len = $res.ContentLength
        $res.Close()
        Write-Host "[PASS] $url -> Status: $status | Type: $type | Size: $len bytes"
    } catch {
        Write-Host "[FAIL] $url -> Error: $_"
        $allOk = $false
    }
}

if ($allOk) {
    Write-Host "SUCCESS: Todas as rotas retornaram 200 OK!"
} else {
    Write-Host "WARNING: Alguma rota falhou."
}
