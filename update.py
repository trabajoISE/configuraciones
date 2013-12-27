#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Signature: Ingeniería de Servidores
# Assignement: Archivos de configuración en repositorio
# Module: update
# Author: Anonymous
# Date: 27/12/2013

import sys
import os

def main():
    for filename in os.listdir("./services"):
        print filename

if __name__ == '__main__': main()
