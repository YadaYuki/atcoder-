# #!/bin/sh

dir=$(dirname $(which $0))
poetry run python ${dir}/resolve.py $(git symbolic-ref --short HEAD) $1