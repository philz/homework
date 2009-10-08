#!/bin/bash
set -e
set -x

INPUT_DATA=$1

PREV=00
NEXT=01

function incr() {
  PREV=$(($PREV + 1))
  printf -v PREV_FILE "tmp-%03d" $PREV
  NEXT=$(($NEXT + 1))
  printf -v NEXT_FILE "tmp-%03d" $NEXT
}

incr
cat $INPUT_DATA > $NEXT_FILE
incr
cat $PREV_FILE | python extract_links.py map > $NEXT_FILE; incr
for x in `jot 10`; do
  cat $PREV_FILE | python calculate_pagerank.py map > $NEXT_FILE; incr
  cat $PREV_FILE | sort > $NEXT_FILE; incr
  cat $PREV_FILE | python calculate_pagerank.py reduce > $NEXT_FILE; incr
done
cat $PREV_FILE | python cleanup.py map > $NEXT_FILE; incr
cat $PREV_FILE | sort > $NEXT_FILE; incr
cat $PREV_FILE | python cleanup.py reduce > $NEXT_FILE; incr
