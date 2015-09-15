# cachesimulator
#### Proyecto final para la materia de sistemas operativos.

##### Inicio Rápido:
###### - Descargar el repositorio:
	git clone https://github.com/sergiosuarez/cachesimulator

###### - Instalación:
	cd cachesimulator
	sudo python setup.py
	chmod +x cacheSim.py

###### - Dependencias:	
	python-numpy
	python-scipy
	python-matplotlib
	
###### - Uso:
	./cacheSim.py <archivo-con-cadena-de-referencia> <política de desalojo> <tamaño-de-caché>

###### - Políticas de desalojo disponibles:
	- LRU
	- FIFO
	- ÓPTIMO
	- CLOCK

###### - Ejemplo:
	./cacheSim.py workload.txt LRU 50000
  

###### - Ejemplo para el algoritmo optimo:
	./optimo.py workload.txt 50000
  
  
###### - Generar la gráfica:
	./plot.py

###### - Para compilar:
	python2 -O -m py_compile cacheSim.py

###### - Para ejecutar el compilado:
	chmod +x cachesim.pyo
	time python2 cacheSim.pyo workload.txt lru 50000
