import urllib.request

urls = [
    'http://localhost:8080/',
    'http://localhost:8080/sobre/',
    'http://localhost:8080/servico/listar/',
    'http://localhost:8080/tatuagem/listar/',
    'http://localhost:8080/categoria/listar/',
    'http://localhost:8080/estilo/listar/',
    'http://localhost:8080/entrar/',
    'http://localhost:8080/cadastrar/',
    'http://localhost:8080/admin/login/',
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            print(f"[OK] {url} -> {resp.status} (bytes: {len(content)})")
    except Exception as e:
        print(f"[FAIL] {url} -> {e}")
