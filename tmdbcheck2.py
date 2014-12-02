# -*- coding: utf-8 -*-

from __future__ import print_function
import re
import os, sys
import json
import tmdbsimple as tmdb
import xml.etree.cElementTree as ET
from urllib import quote_plus


def execute_movie_search(filename):
    tmdb.API_KEY = '89c9a215e203bb2806265c9ae1762806'
    search = tmdb.Search()
    filename = quote_plus(filename.encode('utf-8'))
    return search.movie(query=filename, language='de')


def process_file(filename, max_hits=20):
    stop = False
    result = []
    print('\n=> Processing next file')
    while not stop:
        encoded_name = filename.encode('utf-8')
        search_result = execute_movie_search(filename)
        hits = search_result[u'total_results']
        if hits == 0:
            # no match!
            print('   no match for "{0}"'.format(encoded_name))
            filename = u' '.join( re.split('\.|\s|,|;|_|-', filename)[:-1])
            if len(filename) == 0:
                stop = True
        elif hits > max_hits:
            # too many ....
            print('   too many matches ({1}) for "{0}"'.format(encoded_name, hits))
            stop = True
        else:
            # match!
            print('   {1} matches for "{0}"'.format(encoded_name, search_result[u'total_results']))
			#root = ET.Element('root')
            elem = ET.Element('file')
            elem.set('name', filename)
            for hit in search_result[u'results']:
                sub_elem = ET.SubElement(elem, 'movie')
                for key in hit:
                    sub_sub_elem = ET.SubElement(sub_elem, key)
                    sub_sub_elem.text = unicode(hit[key])
                #print(hit[u'title'])
            result.append(elem)
            stop = True
    return result


MAX_HITS = 20
path = u'/volume1/video/filme'
if not os.path.exists(path):
    print('Invalid path "{0}"'.format(path))
    exit(1)

filme = os.listdir(path)
root = ET.Element("root")

for f in filme:
    result = process_file(f, MAX_HITS)
    if len(result) > 0:
        for elem in result:
            root.append(elem)

tree = ET.ElementTree(root)
tree.write("/volume1/web/filme.xml")
exit(0)
