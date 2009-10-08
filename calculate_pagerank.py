#!/usr/bin/python

import common
import simplejson

DAMPING_FACTOR = 0.85

def map(line):
  title, data = line.split("\t", 1)

  # Load the data
  try:
    data = simplejson.loads(data)
  except:
    __import__("pdb").set_trace()
  links = data.get("links", [])
  page_rank = data.get("page_rank", 1) # Start with page rank 1 for all pages.

  # Send forth the original link data
  yield title, simplejson.dumps(dict(links=links))

  # And, for every link, redistribute page rank...
  num_links = len(links)
  # We should re-distribute the page rank of pages without links
  # to all other pages, but we don't bother, and lose page rank instead.
  if num_links > 0:
    page_rank_out = page_rank/float(num_links)
    for link in links:
      yield link, simplejson.dumps(dict(page_rank=page_rank_out))

def reduce(title, links_and_page_ranks):
  links = []
  page_rank = 1 - DAMPING_FACTOR # minimum page rank for every page
  for data in links_and_page_ranks:
    d = simplejson.loads(data)
    if "links" in d:
      links = d.get("links")
    page_rank += DAMPING_FACTOR * d.get("page_rank", 0.0)
  
  yield title, simplejson.dumps(dict(links=links, page_rank=page_rank))

if __name__ == "__main__":
  common.main(map, reduce)
