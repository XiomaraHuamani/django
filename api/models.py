# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    dni_empleado = models.IntegerField(blank=True, null=True)
    nombres = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=30, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    id_tienda = models.ForeignKey('Tiendas', models.DO_NOTHING, db_column='id_tienda', blank=True, null=True)
    nombre_tienda = models.CharField(max_length=45, blank=True, null=True)
    id_cargo = models.ForeignKey('TipoEmpleados', models.DO_NOTHING, db_column='id_cargo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados2022'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    codigo = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    precio_venta = models.IntegerField(blank=True, null=True)
    precio_costo = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'
        unique_together = (('id_producto', 'nombres'),)


class RegistroClienteTienda(models.Model):
    id_cli = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=15)
    dni_cli = models.IntegerField()
    nombres_cli = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30, blank=True, null=True)
    distrito = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_cliente_tienda'
        unique_together = (('id_cli', 'tipo_pago', 'dni_cli', 'nombres_cli'),)


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=45, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Tiendas(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre_tienda = models.CharField(max_length=45)
    nombre_dueño = models.CharField(max_length=45, blank=True, null=True)
    fecha_alquiler = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey('TipoCategorias', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiendas'
        unique_together = (('id_tienda', 'nombre_tienda'),)


class TipoCategorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_categorias'


class TipoEmpleados(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_empleados'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    dni = models.IntegerField(blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=40, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    distrito = models.CharField(max_length=30, blank=True, null=True)
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
        unique_together = (('id_usuario', 'nombres'),)


class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    monto = models.FloatField(blank=True, null=True)
    monto_total = models.FloatField(blank=True, null=True)
    id_cli = models.ForeignKey(RegistroClienteTienda, models.DO_NOTHING, db_column='id_cli', blank=True, null=True)
    nombres_cli = models.CharField(max_length=30, blank=True, null=True)
    dni_cli = models.IntegerField(blank=True, null=True)
    tipo_pago = models.CharField(max_length=15, blank=True, null=True)
    numero_boleta = models.CharField(max_length=45, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    ruc = models.IntegerField(blank=True, null=True)
    igb = models.IntegerField(blank=True, null=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    nombres = models.CharField(max_length=20, blank=True, null=True)
    id_tienda = models.ForeignKey(Tiendas, models.DO_NOTHING, db_column='id_tienda', blank=True, null=True)
    nombre_tienda = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
