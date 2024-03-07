#! /bin/sh
# /usr/bin/env sh

HYPRGAMEMODE=$(hyprctl getoption animations:enabled | awk 'NR==2{print $2}')
if [ "$HYPRGAMEMODE" = 1 ] ; then
    hyprctl --batch "\
        keyword animations:enabled 0;\
        keyword decoration:drop_shadow 0;\
        keyword decoration:blur 0;\
        keyword general:gaps_in 10;\
        keyword general:gaps_out 20;\
        keyword general:border_size 6;\
        keyword decoration:rounding 0"
    exit
fi
hyprctl reload
