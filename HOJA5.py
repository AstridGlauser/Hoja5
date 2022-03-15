 #Astrid Glauser 
  #21299
import simpy
import random
import statistics
ram = 100
NoProcesos = 25
Intervalos = 10
velocidad = 3
def Proceso(env, RAM, velocidad, inicial, proceso_num):    
    global Totalidad
    global tarda
    yield env.timeout(inicial)
    Ingreso = round(env.now,4)
    cantproc = random.randint(1,10)
    cantidad = random.randint(1,10)
    completado = 0
    print("El proceso no. %d ingresa en %s ,necesita %d de RAM y tiene %s procesos" % (proceso_num,Ingreso,cantidad,cantproc))
    yield RAM.get(cantidad)
    while completado < cantproc:
        with CPUofComputer.request() as turno:
            yield turno
            print("El proceso no.%s ingresa en tiempo :%f " % (proceso_num,round(env.now,4)))
            if velocidad <=(cantproc - completado) :
                NoProce = velocidad
            else:
                NoProce = (cantproc - completado)
            print("El proceso no.% s necesita %f instrucciones para salir del CPU " % (proceso_num,NoProce))

            yield env.timeout(NoProce/velocidad)   
            completado += NoProce
            print("El proceso no. %s sale en  %f " % (proceso_num,round(env.now,4))) 
        wating = random.randint(1,2)
        if (completado < cantproc) and (wating == 1):
            with Waitt.request() as Waitts:
                print("El proceso no. %s  sale en %s " % (proceso_num,env.now))
                yield env.timeout(1)  
                yield Waitts
    yield RAM.put(cantidad)
    tarda.append(env.now - Ingreso)
    Totalidad += (env.now - Ingreso)
    
def momento(env, RAM, NoProcesos,Intervalos):
    for i in range(NoProcesos):
        inicial = random.expovariate(1 / Intervalos)
        env.process(Proceso(env, RAM, velocidad,inicial, i))

def tiempoPromedio(cantidad, cant,NoProcesos,tarda):
    promedio = (cantidad/cant)
    print("Promedio del tiempo %s" % promedio)
    desviacion(tarda)
    

def desviacion(tiempo):

    st_dev = statistics.pstdev(tiempo)
 
    print("Desviación estándar %s"% st_dev)
    
tarda = list()
Totalidad = 0     
env = simpy.Environment() #ambiente de simulacion
CPUofComputer= simpy.Resource(env,capacity = 2) #solo ha "1" CPUofComputer corriendo las instrucciones
random.seed(45)
RAM = simpy.Container(env, init = ram, capacity = ram)
Waitt = simpy.Resource (env, capacity=2)    

momento(env, RAM, NoProcesos,Intervalos)
env.run()
tiempoPromedio(Totalidad,NoProcesos,NoProcesos,tarda)
