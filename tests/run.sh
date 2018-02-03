#!/bin/bash

for file in ./scripts/*; do
    [ -f "$file" ] && [ -x "$file" ] && mplisp "$file"
done
