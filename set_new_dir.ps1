#
#  Script to make directory and new empty files for problem on Windows.

if (!$args[0]) {

    Write-Host 
    Write-Host 'New directory name not specified!'
    Write-Host 'Syntax: set_new_dir.ps1 ${dir_name}'
    Write-Host

    Exit 1

} else {

    $file_list = @(".gitignore", "code.py", "test.py", "sample_dataset.txt",
                   "sample_output.txt", "dataset.txt", "output.txt")

    $gitignore_text = @("__pycache__/*", "sample_*")

    $problems = $null

    foreach ($file in Get-ChildItem -Path "problems") {
        if ($args[0] -in (Get-Content -Path (Join-Path "problems" $file))) {
            $problems = ($file -split "\.")[0]
            break
        }
    }

    #TODO: Move directory and files to problem directory
    if ($problems) {

        if ( !(Test-Path $args[0]) ) {
            New-Item -Path $args[0] -ItemType "directory" | Out-Null
        }

        Set-Location $args[0]

        foreach ($file in $file_list) {
            if (!(Test-Path $file)) {
                New-Item -Path $file -ItemType "file" | Out-Null
            } else {
                Write-Host
                Write-Host "$file already exists!"
            }
        }

        $gitignore_cont = Get-Content ".gitignore"

        foreach ($line in $gitignore_text) {
            if ( !($gitignore_cont -contains $line) ) {
                Out-File -FilePath ".gitignore" -Append -InputObject $line
            }
        }

        Set-Location .. #  Powershell doesn't run scripts in subshell

    } else {

        Write-Host 
        Write-Host 'Problem name not found!'
        Write-Host
    }

}