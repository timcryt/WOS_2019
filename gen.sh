#!/bin/sh

xd -d corpus.xz
mv corpus turgenev.txt

echo -e "import json\nmark=gen_mark_from_file(open('turgenev.txt','r'), 12, 6)\njson.dump(mark,open('table.json','w'))" | cat mark_generator.py /dev/stdin | python3
