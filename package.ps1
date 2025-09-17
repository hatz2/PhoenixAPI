# Script to upload a new version of the package

# Move to the python dir
Set-Location python

# Delete old package files
Remove-Item -r dist/*

# Generate new files
py -m build

# Upload files
py -m twine upload dist/*