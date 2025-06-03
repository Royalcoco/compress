# Classify-Files.ps1

param(
    [string]$SourceDir = ".\\pages",
    [string]$BaseOutDir = ".\\classified"
)

$categories = @{
    "Frontend"    = @("html", "css", "javascript", "ui", "interface", "react", "vue")
    "Backend"     = @("api", "controller", "service", "database", "python", "node", "java", "logic")
    "Network"     = @("socket", "dns", "tcp", "udp", "ip", "firewall", "proxy", "port")
    "Architecture"= @("layer", "microservice", "monolith", "design", "scalability", "component", "pattern")
    "Interface"   = @("ux", "ui", "layout", "accessibility", "form", "interaction")
}

# Crée les dossiers cibles
$categories.Keys | ForEach-Object {
    $target = Join-Path $BaseOutDir $_
    if (-not (Test-Path $target)) {
        New-Item -ItemType Directory -Path $target | Out-Null
    }
}

# Traitement des fichiers
Get-ChildItem -Path $SourceDir -Filter "*.txt" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $moved = $false

    foreach ($category in $categories.Keys) {
        foreach ($keyword in $categories[$category]) {
            if ($content -match [regex]::Escape($keyword)) {
                $targetPath = Join-Path $BaseOutDir $category
                Copy-Item $_.FullName -Destination $targetPath
                Write-Host "📂 '$($_.Name)' -> $category"
                $moved = $true
                break
            }
        }
        if ($moved) { break }
    }

    if (-not $moved) {
        Write-Host "⚠️  Aucun mot-clé trouvé dans '$($_.Name)'"
    }
}
