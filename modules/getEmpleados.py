# devuelve un listado con el nombre, apellidos, y email 
# de los empleados cuyo  jefe tiene un codigo de jefe igual  a 7 

import storage.empleado as em

def getAllNombreApellidoemail(codigo):
    NombreApellidoemail = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            NombreApellidoemail.append(
                {
                    "nombre": val.get("nombre"),
                    "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return NombreApellidoemail

# devuelve el nombre, puesto, apellido y email del jefe de la empresa 
import storage.empleado as em 

def getAllNombrePuestoApellidoEmailJefe():
    NombrePuestoApellidoEmailJefe = []
    for val in em.empleados:
        if(val.get("codigo_jefe")) == None:
            NombrePuestoApellidoEmailJefe.append(      
                {                  
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")})',
                "email": val.get("email"),
                "jefe": val.get("jefe") 
                }
            )
        return NombrePuestoApellidoEmailJefe
        
     


            
        