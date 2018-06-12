# isd-tp3
Un estudio de SDNs y OpenFlow, mediante Mininet, Pox y otras herramientas fantásticas.

## Cómo levantar la topología simple
```
sudo mn --custom custom_topo.py --topo simple,3 --mac --arp --switch ovsk --controller remote
```
**Observaciones:**
1. Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
2. Luego de especificar el tipo de topología en --topo (en este caso 'simple'), se debe ingresar una coma seguido de la cantidad de switches que se desea crear (sin espacios)

## Cómo levantar la topología compleja o en rombo
```
sudo mn --custom custom_topo.py --topo diamond,3,4 --mac --arp --switch ovsk --controller remote
```
**Observaciones:**
1. Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
2. Luego de especificar el tipo de topología en --topo (en este caso 'diamond'), se debe ingresar una coma seguido de la cantidad de niveles que se desea crear y otra coma seguido de la cantidad de hosts (sin espacios)

## Cómo utilizar el controlador
