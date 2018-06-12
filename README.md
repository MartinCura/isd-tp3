# isd-tp3
Un estudio de SDNs y OpenFlow, mediante Mininet, Pox y otras herramientas fantásticas.

## Cómo levantar la topología simple
```
sudo mn --custom custom_topo.py --topo simple,3 --mac --arp --switch ovsk --controller remote`
```
**Observaciones:**
Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
Luego de especificar el tipo de topología en --topo (en este caso 'simple'), se debe ingresar una coma seguido de la cantidad de switches que se desea crear (sin espacios)

## Cómo levantar la topología compleja o en rombo


