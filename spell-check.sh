#!/bin/sh

textidote --check en --firstlang nl --dict dict.txt --output html --remove-macros "gls,glspl,glsentryshort,glsentryshortpl,glsentrylong,glsentrylongpl,glsentryfull,glsentryfullpl,mintinline,mint" --remove "minted,listing" main.tex > report.html

