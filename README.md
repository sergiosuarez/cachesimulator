# cachesimulator
#### Proyecto final para la materia de sistemas operativos.

##### Inicio Rápido:
###### - Descargar el repositorio:
	git clone https://github.com/sergiosuarez/cachesimulator

###### - Instalar dependencias:
	cd cachesimulator
	sudo python setup.py
	chmod +x cacheSim.py

###### - Uso:
  ./cacheSim.py <archivo-con-cadena-de-referencia> <política de desalojo> <tamaño-de-caché>

###### - Políticas de desalojo disponibles:
  - LRU
  - FIFO
  - ÓPTIMO
  - CLOCK

###### - Ejemplo:
  ./cacheSim.py workload.txt LRU 50000
  
###### - Generar la gráfica:
  ./plot.py
  
  
