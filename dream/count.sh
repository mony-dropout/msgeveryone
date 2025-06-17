#!/bin/bash
i=0
find . -name "*" -exec ((i++)) \;
echo i