# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe.build_exe
from modulefinder import Module
import glob, fnmatch
import sys, os, shutil
import operator
 
setup(name="Juego", 
 version="1.0", 
 description="Breve descripcion", 
 author="autor", 
 author_email="email del autor", 
 url="url del proyecto", 
 license="tipo de licencia", 
 scripts=["main.py"],
 console=["main.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)
