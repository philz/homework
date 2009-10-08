#!/usr/bin/python

DAMP = 0.85
ITERATIONS = 30

graph=dict(
  A=["B", "C", "D"], 
  B=["A", "E"], 
  C=[], 
  D=["F"],
  E=["A", "B", "C"],
  F=["A"],
  G=["C"]
)

page_ranks=dict()
for x in graph:
  page_ranks[x] = 1.0

for _ in range(ITERATIONS):
  print repr(page_ranks), sum(page_ranks.itervalues())
  new = dict()
  for node in graph:
    new[node] = (1.0-DAMP)
  for node, links in graph.iteritems():
    # If there are no outgoing links, distribute evenly
    # across all pages.
    if len(links) == 0:
      links = graph.keys()
    for link in links:
      new[link] += DAMP*page_ranks[node]/len(links)
  page_ranks = new

print repr(page_ranks), sum(page_ranks.itervalues())
