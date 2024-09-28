#
#  Script to make directory and new empty files for problem on Windows.

if (!$args[0]) {

    Write-Host 
    Write-Host 'New directory name not specified!'
    Write-Host 'Syntax: set_new_dir.ps1 ${dir_name}'
    Write-Host

    Exit 1

} else {

    $file_list = @("code.py", "test.py", "sample_dataset.txt",
                   "sample_output.txt", "dataset.txt", "output.txt")

    $problems = $null

    foreach ($file in Get-ChildItem -Path "problems") {
        if ($args[0] -in (Get-Content -Path (Join-Path "problems" $file))) {
            $problems = ($file -split "\.")[0]
            break
        }
    }

    if ($problems) {

        $problem_path = Join-Path $problems $args[0]

        if ( !(Test-Path $problem_path) ) {
            New-Item -Path $problem_path -ItemType "directory" | Out-Null
        }

        Set-Location $problem_path

        foreach ($file in $file_list) {
            if (!(Test-Path $file)) {
                New-Item -Path $file -ItemType "file" | Out-Null
            } else {
                Write-Host
                Write-Host "$file already exists!"
            }
        }

        Set-Location ../.. #  Powershell doesn't run scripts in subshell

    } else {

        Write-Host 
        Write-Host 'Problem name not found!'
        Write-Host

        Exit 1

    }

}