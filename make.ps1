pushd $PSScriptRoot

# Command file for Sphinx documentation
if ($null -eq $env:SPHINXBUILD) {
	$SPHINXBUILD="sphinx-build"
} else {
	$SPHINXBUILD=$env:SPHINXBUILD
}
if ($null -eq $env:SPHINXOPTS) {
	$SPHINXOPTS=""
} else {
	$SPHINXOPTS=$env:SPHINXOPTS
}

$SOURCEDIR="./"
$BUILDDIR="_build/"
$DOCSDIR="docs/"

& $SPHINXBUILD | Out-Null

if ($LASTEXITCODE -eq 9009) {
	Write-Host ""
	Write-Host "The 'sphinx-build' command was not found. Make sure you have Sphinx"
	Write-Host "installed, then set the SPHINXBUILD environment variable to point"
	Write-Host "to the full path of the 'sphinx-build' executable. Alternatively you"
	Write-Host "may add the Sphinx directory to PATH."
	Write-Host ""
	Write-Host "If you don't have Sphinx installed, grab it from"
	Write-Host "https://www.sphinx-doc.org/" -ForegroundColor DarkCyan
	Write-Host ""
	Exit 1
}

function Start-Sphinx {
	& sphinx-reload --build-dir $BUILDDIR ./ --watch index.rst ./**/*.rst ./**/*.md ./**/*.py
}

function Install-Pages {
	& $SPHINXBUILD -M clean $SOURCEDIR $BUILDDIR $SPHINXOPTS
	& Remove-Item -Recurse -Force $DOCSDIR
	& New-Item $DOCSDIR -ItemType "directory"
	& $SPHINXBUILD -M html $SOURCEDIR $BUILDDIR $SPHINXOPTS
	& robocopy ($BUILDDIR + "html") $DOCSDIR /e
}

switch ( $args ) {
	"start" { Start-Sphinx }
	"install" { Install-Pages }
	default {
		"$SPHINXBUILD -M $args $SOURCEDIR $BUILDDIR $SPHINXOPTS"
		& $SPHINXBUILD -M $args $SOURCEDIR $BUILDDIR $SPHINXOPTS
	}
}
popd
