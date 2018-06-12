# Trabajo Práctico 3 -- Introducción a los Sistemas Distribuidos (FIUBA)
Un estudio de SDNs y OpenFlow, mediante Mininet, Pox y otras herramientas fantásticas.

## Cómo levantar la topología simple
```
$ sudo mn --custom custom_topo.py --topo simple,3 --mac --arp --switch ovsk --controller remote
```
**Observaciones:**
1. Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
2. Luego de especificar el tipo de topología en --topo (en este caso 'simple'), se debe ingresar una coma seguido de la cantidad de switches que se desea crear (sin espacios).

**Resultado esperado:**
> Al ejecutar el comando se debe crear una topología con la cantidad de switches pasados por parámetro conectados entre sí en forma de cadena y con 2 hosts de conectados a cada extremo de la topología.

## Controlador para la topología simple
Copiar los archivos 'topo2_ctl.py', 'custom_l2_learning.py' y 'custom_firewall.py' (módulos que son utilizados por 'topo2_ctl.py') que se encuentran en el directorio pox/ext, al directorio de mismo nombre en la distribución de pox que se tenga instalada. Luego ejecutar pox desde el directorio que desee y pasar como parámetro el nombre del controlador invocante (topo2_ctl).
```
$ pox/pox.py topo2_ctl
```
**Adicionalmente se pueden agregar parámetros para modificar el nivel de log**
```
$ pox/pox.py topo2_ctl log.level --DEBUG --packet=ERROR
```

## Cómo levantar la topología compleja o en rombo
```
$ sudo mn --custom custom_topo.py --topo diamond,3,4 --mac --arp --switch ovsk --controller remote
```
**Observaciones:**
1. Luego de --custom se debe ingresar el path completo desde el directorio actual al directorio donde se encuentra custom_topo.py
2. Luego de especificar el tipo de topología tras --topo (en este caso 'diamond'), se debe ingresar una coma seguido de la cantidad de niveles que se desea crear y otra coma seguido de la cantidad de hosts (sin espacios).

**Resultado esperado:**
> Al ejecutar el comando se debe crear una topología con la cantidad de niveles pasados por parámetro conectados entre sí en forma de rombo y con la cantidad de hosts pasados como parámetro igualmente distribuidos y conectados a cada extremo de la topología.

## Controlador para la topología compleja
Copiar los archivos 'custom_spanning_tree.py', 'custom_l2_learning.py'(módulo que es utilizado por 'custom_spanning_tree.py') que se encuentran en el directorio pox/ext, al directorio de mismo nombre en la distribución de pox que se tenga instalada. Luego ejecutar pox desde el directorio que desee y pasar como parámetro el nombre del controlador invocante (custom_spanning_tree).
```
$ pox/pox.py custom_spanning_tree
```
**Adicionalmente se pueden agregar parámetros para modificar el nivel de log**
```
$ pox/pox.py custom_spanning_tree log.level --DEBUG --packet=ERROR
```
