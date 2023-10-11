#!/bin/bash

envname="cursedenv"

log() {
    echo "$*" >&2
}

if [[ ! -d "./${envname}" ]]; then
    python3 -m venv ${envname}
fi

source "${envname}/bin/activate"
log Building cursed_random...
python3 -m build

log Installing cursed_random using $(which pip)...
pip install dist/cursed_random-0.0.1-py3-none-any.whl --force-reinstall

log Packages successfully installed in environment
log All installed packages:
pip list
