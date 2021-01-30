#!/usr/bin/env python3

import sys
import yaml

def pdfinfo2mkdocs(pdfinfo: dict):
    map_pdf2mkdocs = {
        'Title': 'site_name',
        'Author': 'site_author',
    }
    mkdocs = {
        'copyright': pdfinfo['Author'],
        'theme': {
            'language': 'pt',
            'name': 'material',
        }
    }
    for kpdf,kmkdocs in map_pdf2mkdocs.items():
        if kpdf in pdfinfo:
            mkdocs[kmkdocs] = pdfinfo[kpdf]

    return mkdocs    
    
def main():
    info = yaml.load(open('info.yaml', 'r', encoding='utf-8'), Loader=yaml.SafeLoader)
    mkdocs = pdfinfo2mkdocs(info)
    yaml.dump(mkdocs, open('mkdocs.yml', 'w', encoding='utf-8'))

if __name__ == '__main__':
    main()
