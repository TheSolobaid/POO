#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
import os
import re
import pickle as pkl

class AnalyseurWeb:
    histo = {}
    @classmethod
    def __check_machine_name(url) -> bool :
        if re.search(r"^[w]{3}\.[a-zA-Z]*\.[a-zA-Z]{2,3}$", url):
            return True

    def historique(url):
        if url in AnalyseurWeb.histo:
            AnalyseurWeb.histo[url]+=1
        else:
            AnalyseurWeb.histo[url]=1


    def open_url(self, machine_name):
        isopen = False
        isopen = self.__check_machine_name(machine_name)
        if isopen :
            url = str('http://'+machine_name)
            sock = urlopen(url)
            AnalyseurWeb.historique(url)
            page = sock.read()
            sock.close()
            return page.decode("utf-8")
        else :
            return ""
    def save_historique():
        with open('historique.pkl', 'wb') as file:
            pkl.dump(AnalyseurWeb.histo, file)      
    #def trois_sites():        
    #def nbr_css():
    #def get_langage():
        
        
        
