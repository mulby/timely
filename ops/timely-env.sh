#!/bin/bash

SCRIPT_ROOT=$(readlink -f $(dirname $(readlink -f "$0")))
. $SCRIPT_ROOT/enter.sh
$@
. $SCRIPT_ROOT/exit.sh
