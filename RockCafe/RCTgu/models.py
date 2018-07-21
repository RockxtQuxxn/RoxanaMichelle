from django.db import models

class Clientes(models.Model):
	nombre=models.CharField(max_length=50, help_text='Nombre del cliente')
	apellido=models.CharField(max_length=50, help_text='Apellido del cliente')

	def __str__(self):
		return self.nombre

class Empleados(models.Model):
	nombre_emp=models.CharField(max_length=50, help_text='Nombre del empleado')
	apellido_emp=models.CharField(max_length=50, help_text='Apellido del empleado')
	no_identidad=models.CharField(max_length=20, help_text='Numero de identidad del empleado')
	fecha_nac=models.CharField(max_length=20, help_text='Fecha de nacimiento del empleado')
	telefono=models.CharField(max_length=20, help_text='Numero telefonico del empleado')
	telefono_emerg=models.CharField(max_length=20, help_text='Telefono de emergencia')
	direccion=models.CharField(max_length=50, help_text='Direccion del empleado')

	def __str__(self):
		return self.nombre_emp

class Menu(models.Model):
	producto=models.CharField(max_length=50, help_text='Ingrese el producto')
	precio=models.CharField(max_length=50, help_text='Precio del producto')

	def __str__(self):
		return self.producto

class Proveedores(models.Model):
	empresa=models.CharField(max_length=50, help_text='Nombre de la empresa')
	telefono=models.CharField(max_length=50, help_text='Numero telefonico de la empresa')

	def __str__(self):
		return self.proveedores

class Inventario(models.Model):
	producto=models.CharField(max_length=50, help_text='Nombre del producto')
	cant_producto=models.CharField(max_length=50, help_text='Cantidad existente del producto')
	existe=models.BooleanField(default=True)

	def __str__(self):
		return self.producto