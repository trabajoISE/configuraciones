#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Signature: Ingeniería de Servidores
# Assignement: Archivos de configuración en repositorio
# Module: update
# Author: Anonymous
# Date: 27/12/2013

import sys
import os

from subprocess import *

def update_service(service):
    """
    Función que actualiza un servicio recibido
    como argumento.
    Arguments:
    - `service`: servicio a actualizar
    """
    print "[OK] Realizando copia de seguridad"
    sp = Popen("cp %s %s.old" % (service[1], service[1]), stdout=PIPE,
                       stderr=PIPE, shell=True)
    out, err = sp.communicate()
    if len(err) == 0:
        print "[OK] %s guardado como %s.old" % (service[1], service[1])
    else:
        print "[Error] %s" % err
        sys.exit(-1)

    print "[OK] Copiando la nueva configuración"
    directorio, archivo = os.path.split(service[1])
    sp = Popen("cp ./services/%s/%s %s" % (service[0], archivo, service[1]),
               stdout=PIPE, stderr=PIPE, shell=True)
    out, err = sp.communicate()
    if len(err) == 0:
        print "[OK] %s actualizado" % service[1]
    else:
        print "[Error] %s" % err
        sys.exit(-1)


def main():
    # Lectura de la configuración local
    local_services = []
    with open("./services.local") as f:
        for line in f:
            service = line.split()
            local_services.append(service)

    # Comprobar todos los servicios del repositorio
    for repo_service in os.listdir("./services"):
        for service in local_services:
            # Si está en los servicios locales, actualizar
            if repo_service == service[0]:
                print "[OK] Servicio %s encontrado" % repo_service
                print "[OK] Se procede a la actualización de %s" % repo_service
                update_service(service)

if __name__ == '__main__': main()
