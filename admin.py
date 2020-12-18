#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import URLError,HTTPError
def admin():
    print("          Input URL Without https:// or http://")
    print()
    inp = input("Link :")
    sub = open("link.txt","r")
    while True:
        read = sub.readline()
        if not read:
            break
        link = "http://"+inp+"/"+read
        try:
            main = urlopen(link)
        except HTTPError as e:
            print("Not Found",link)
            continue
        except URLError as e:
            print("Not Found",link)
            continue
        else:
            print("Found ==>",link)
            with open("Admin_panel.txt","a") as Admin:
                Admin.write(link)

def Credit():
	 print ('''
	 "#####################################"
         "#  +++ Admin Panel Finder v 1 +++    #"
         "#     Script by MR M0HAM3D           #"
	 "#         N00B C0D3R                 #"
	 "######################################" ''' )

Credit()
admin()
