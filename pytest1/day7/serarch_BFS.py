#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:serarch_BFS.py
@time:2018-07-30-10-30
'''

from collections import deque
graph={}
graph["tanghulu"]=["alice","bob","claire"]
graph["alice"]=["peggy"]
graph["bob"]=["anuj","peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]


def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("%s is a mango seller!" %person)
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False
def person_is_seller(name):
    if name[-1]=='m':
        return True


search("tanghulu")
