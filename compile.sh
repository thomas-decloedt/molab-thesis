#!/bin/sh

# Run the compilation commands
lualatex -shell-escape main \
&& biber main \
&& makeglossaries main \
&& lualatex -shell-escape main \
&& lualatex -shell-escape main

