#!/usr/bin/python

import common
import simplejson

FORMATTING_MULTIPLIER = 10000

def map(line):
  title, data = line.split("\t")
  page_rank = simplejson.loads(data).get("page_rank")
  yield "%010d" % int(page_rank*10000), title

def reduce(page_rank, titles):
  yield page_rank, str(titles)


def emit(key, value):
  """
  Emits a key->value pair.  Key and value should be strings.
  """
  print "\t".join( (key, value) )

if __name__ == "__main__":
  common.main(map, reduce)
