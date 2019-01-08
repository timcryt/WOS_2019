#!/bin/sh

echo -e "import json\nmark=json.load(open('table.json','r'))\nprint(gen_text(mark,1000))" | cat text_generator.py /dev/stdin | python3
