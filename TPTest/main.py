#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import AnalyseurWeb as aweb


url = 'www.google.com'
name = 'google.com'
def main() -> int:
    aweb.AnalyseurWeb.open_url(name,url)
    return (0)

if __name__ == "__main__":
    sys.exit(main())
