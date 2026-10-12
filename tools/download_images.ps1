$imgDir = "$PSScriptRoot\assets\images"
if (!(Test-Path $imgDir)) {
    New-Item -ItemType Directory -Path $imgDir -Force | Out-Null
}

$images = @(
    "attila-tattoo-1.png",
    "attila-tattoo-2.png",
    "attila-tattoo-3.png",
    "attila-tattoo-4.png",
    "attila-tattoo-5.png",
    "attila-tattoo-6.png",
    "attila-tattoo-7.jpg",
    "attila-tattoo-8.png",
    "attila-tattoo-9.png",
    "attila-tattoo-10.png",
    "attila-tattoo-11.png",
    "attila-tattoo-12.png",
    "attila-tattoo-13.png",
    "raffa-tattoo-1.jpeg",
    "raffa-tattoo-2.jpeg",
    "raffa-tattoo-3.jpeg",
    "raffa-tattoo-4.jpeg",
    "raffa-tattoo-5.jpeg",
    "raffa-tattoo-6.jpeg",
    "raffa-tattoo-7.jpeg",
    "raffa-tattoo-8.jpeg",
    "raffa-tattoo-9.jpeg",
    "raffa-tattoo-10.jpeg",
    "paulo-tattoo-1.jpeg",
    "paulo-tattoo-2.jpeg",
    "paulo-tattoo-3.jpeg",
    "paulo-tattoo-4.jpeg",
    "paulo-tattoo-5.jpeg",
    "paulo-tattoo-6.jpeg",
    "paulo-tattoo-7.jpeg",
    "paulo-tattoo-8.jpeg",
    "paulo-tattoo-9.jpeg",
    "paulo-tattoo-10.jpeg",
    "7cb3cbc8-e64a-4dbb-8c39-660798157d65.png",
    "686a2fa7-f6db-4d5e-a43d-a1ba6451fd9e.png",
    "992cd6c5-5939-4eb1-9173-1e98744b2961.png",
    "b1963cf0-15f1-43e2-9b1c-f9805c2bf130.png",
    "0193441e-8e26-45c7-bcaa-1b368286bbf3.png",
    "fc86e49e-c81d-422d-b7ee-a3d03f2cdfd8.png",
    "3bea76d9-d397-4724-ba5d-312b4f8493a1.png",
    "0eefaa63-bfce-498f-93e8-60caa96807ce.png",
    "3fcf11b0-9e74-4295-a797-23a2f7462c2a.png",
    "82525c7e-e818-4091-86c8-fbe4bb0fbbd7.png",
    "7fc48555-5fd3-4efb-ba9c-42799072308e.png",
    "4197f8d4-2c42-4603-8fdf-2bb67ecc0733.png",
    "0c10632c-300a-4e15-ab8c-b40648cb9520.png",
    "bb950bc8-7321-43d8-ae04-fd904214f933.png",
    "5a1ba445-a5db-4a32-b4d8-9f8c252d89e3.png",
    "c7901fe7-f56b-459a-ae6b-626f7e9ed2f9.png",
    "cf035543-5b33-4a33-8ec0-2cdf8c0bb111.png",
    "9e3ca254-4bf9-4f1c-ba4c-68db9894eb76.png",
    "e116c9dc-210a-40a9-aa81-8820207f210c.png",
    "6e1657a4-7bba-4bdd-9f33-a7e5573602a1.png",
    "d09ce1b5-67f7-472e-92fd-070f7a3cef81.png",
    "3aefd914-f60c-4d2e-9633-c83f1900b8fa.png",
    "7002e983-f599-464b-8ec4-2d1517414ee8.png",
    "a887ab2d-bdcc-4b7f-be87-4384b84ad27f.png",
    "ricardo-alonso-laser.png"
)

$downloadCount = 0
foreach ($img in $images) {
    $dest = "$imgDir\$img"
    if (!(Test-Path $dest)) {
        $url = "https://ledstattoo.com.br/lovable-uploads/$img"
        try {
            curl.exe -s -L "$url" -o "$dest"
            if ((Get-Item $dest).Length -gt 1000) {
                $downloadCount++
            } else {
                Remove-Item $dest -Force -ErrorAction SilentlyContinue
            }
        } catch {
            Write-Host "Failed $img"
        }
    } else {
        $downloadCount++
    }
}

Write-Host "Successfully retrieved $downloadCount valid images into assets\images"
