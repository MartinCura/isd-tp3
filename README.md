# isd-tp3
Un estudio de SDNs y OpenFlow, mediante Mininet, Pox y otras herramientas fantásticas.

## Cómo levantar la topología simple
```
sudo mn --custom custom_topo.py --topo simple,3 --mac --arp --switch ovsk --controller remote
```
**Observaciones:**
1. Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
2. Luego de especificar el tipo de topología en --topo (en este caso 'simple'), se debe ingresar una coma seguido de la cantidad de switches que se desea crear (sin espacios)

## Controlador para la topología simple
Desde el directorio root del repositorio (o carpeta de archivos del TP), ejecutar el siguiente comando para levantar el controlador para la topología simple:
```
pox/pox.py topo2_ctl
```
**Adicionalmente se pueden agregar parámetros para modificar el nivel de log**
```
pox/pox.py topo2_ctl log.level --DEBUG --packet=ERROR
```

## Cómo levantar la topología compleja o en rombo
```
sudo mn --custom custom_topo.py --topo diamond,3,4 --mac --arp --switch ovsk --controller remote
```
**Observaciones:**
1. Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
2. Luego de especificar el tipo de topología en --topo (en este caso 'diamond'), se debe ingresar una coma seguido de la cantidad de niveles que se desea crear y otra coma seguido de la cantidad de hosts (sin espacios)

## Controlador para la topología compleja
Desde el directorio root del repositorio (o carpeta de archivos del TP), ejecutar el siguiente comando para levantar el controlador para la topología simple:
```
pox/pox.py custom_spanning_tree
```
**Adicionalmente se pueden agregar parámetros para modificar el nivel de log**
```
pox/pox.py custom_spanning_tree log.level --DEBUG --packet=ERROR

