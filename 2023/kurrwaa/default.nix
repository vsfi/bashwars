with import <nixpkgs> { };
let
  my-python-packages = python-packages: [
    python-packages.pip
    python-packages.setuptools
    python-packages.click
    python-packages.virtualenv
  ];

  my-python = python310.withPackages my-python-packages;
in pkgs.mkShell {
  buildInputs = [ bashInteractive my-python python310Packages.setuptools ];
  shellHook = ''
    export PIP_PREFIX="$(pwd)/.local/_build/pip_packages"
    export PYTHONPATH="$(pwd)/.local/_build/pip_packages/lib/python3.10/site-packages:$PYTHONPATH"
    export PS1='\[\033[1;32m\][\[\033[1;31m\]ansible:\[\033[1;32m\]\W]\$\[\033[0m\] '
    export PATH=$PATH:$PIP_PREFIX/bin
    unset SOURCE_DATE_EPOCH

    virtualenv --no-setuptools $(pwd)/.local/.venv

    pip install --upgrade mimesis

  '';
}
