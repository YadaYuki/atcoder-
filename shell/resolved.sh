# #!/bin/sh

poetry run python $AC_ROOT/shell/resolve.py $(git symbolic-ref --short HEAD) $1