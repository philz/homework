#!/usr/bin/env python2.4
import xml.parsers.expat
import sys

KEEP = set(["page", "title", "text"])
# Stack of where we are.
current = []

def start_element(name, attrs):
  current.append(name)
  if name in KEEP:
    sys.stdout.write("<%s>" % name)

def end_element(name):
  current.pop()
  if name in KEEP:
    sys.stdout.write("</%s>" % name)
  if name == "page":
    sys.stdout.write("\n")

def char_data(data):
  if current[-1] in KEEP:
    sys.stdout.write(data.replace("\n", " "))

p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data
p.returns_unicode = False

p.ParseFile(sys.stdin)
