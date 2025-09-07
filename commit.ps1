param(
    [string]$Message = ""
)

# If no commit message provided, use default timestamp
if ([string]::IsNullOrEmpty($Message)) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Message = "Auto commit - $timestamp"
}

Write-Host "Starting auto Git commit process..." -ForegroundColor Green
Write-Host "Commit message: $Message" -ForegroundColor Cyan

try {
    # Get script directory and change to it
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    Set-Location $scriptDir
    
    # Call Python script
    python auto_commit.py $Message
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Commit completed successfully!" -ForegroundColor Green
    } else {
        Write-Host "Error occurred during commit process" -ForegroundColor Red
        exit $LASTEXITCODE
    }
}
catch {
    Write-Host "Exception occurred: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}