#!/usr/bin/python

import common
import unittest
import re
import simplejson

TITLE = re.compile("<title>(.*)</title>")
TEXT = re.compile("<text>(.*)</text>")
LINK_BODY = re.compile("\[\[([^\[\]]+)\]\]")

def normalize_title(title):
  return title.replace(" ", "_")

def extract_title_and_text(line):
  t = TITLE.search(line)
  if t:
    title = normalize_title(t.groups()[0])
  else:
    title = None
  t = TEXT.search(line)
  if t:
    text = t.groups()[0]
  else:
    text = None
  return title, text

def extract_links(text):
  links = set()
  for body in LINK_BODY.finditer(text):
    link_body_text = body.groups()[0]
    # If there's an alias, strip it out
    link = link_body_text.split("|")[0]
    # If there's an anchor name, strip it out
    link = link.split("#")[0]
    # Ignore interwiki links
    if ":" in link:
      continue
    link = normalize_title(link)
    links.add(link)
  return list(links)

def map(line):
  title, text = extract_title_and_text(line)
  # Ignore "special" pages
  if ":" in title:
    return
  title = normalize_title(title)
  links = extract_links(text)
  yield title, simplejson.dumps(dict(links=links))

def reduce(word, counts):
  raise Exception("No reducer should be called.")

class ThisModuleTest(unittest.TestCase):
  def testExtractTitleAndText(self):
    data = "<page><title>yo foo</title><text>woot</text></page>"
    self.assertEquals( ("yo_foo", "woot"), extract_title_and_text(data) )
  def testExtractLinks(self):
    self.assertEquals(set(["a", "bc"]),
      set(extract_links("Bla bla [[a]], [[:interwiki:foo]], [[bc|def]]")))

if __name__ == "__main__":
  common.main(map, reduce)
