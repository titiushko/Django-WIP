# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Archivero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ArchivoResultadoExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArchivo', models.CharField(max_length=20)),
                ('ubicacionArchivo', models.FileField(upload_to='archivos/resultados_examenes')),
                ('descripcionArchivo', models.TextField(blank=True, max_length=50, null=True)),
                ('fechaRegistro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoAlergia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('reaccion', models.CharField(max_length=20)),
                ('tratamiento', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoDepartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDepartamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoEnfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEnfermedad', models.CharField(max_length=20)),
                ('descripcionEnfermedad', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoEspecialidadEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoEspecialidad', models.CharField(max_length=50)),
                ('descripcionEspecialidad', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoMedicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMedicamento', models.CharField(max_length=50)),
                ('modoUso', models.TextField(blank=True, max_length=100, null=True)),
                ('efectosSecundarios', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoMunicipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMunicipio', models.CharField(max_length=50)),
                ('CatalogoDepartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoDepartamento')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoTipoClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoClinica', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoTipoExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreExamen', models.CharField(max_length=20)),
                ('descripcionExamen', models.CharField(blank=True, max_length=50, null=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('CatalogoTipoClinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoTipoClinica')),
            ],
        ),
        migrations.CreateModel(
            name='ConstanciaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dirigidaA', models.CharField(max_length=100)),
                ('motivoConstancia', models.TextField()),
                ('fechaEmisionConstancia', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaConsulta', models.DateField()),
                ('motivo', models.TextField(max_length=100)),
                ('sintomatologia', models.TextField(max_length=200)),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('diagnostico', models.TextField(max_length=200)),
                ('fechaProximaConsulta', models.DateField(blank=True, null=True)),
                ('CatalogoEnfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoEnfermedad')),
                ('Clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalleDireccion', models.TextField(max_length=100)),
                ('CatalogoDepartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoDepartamento')),
                ('CatalogoMunicipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoMunicipio')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField()),
                ('tiempoServicio', models.IntegerField()),
                ('jVPM', models.IntegerField(blank=True, null=True)),
                ('CatalogoEspecialidadEmpleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoEspecialidadEmpleado')),
                ('Clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaElaboracion', models.DateField()),
                ('Archivero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Archivero')),
                ('CatalogoAlergia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoAlergia')),
                ('Clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='IncapacidadMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEmpresa', models.CharField(max_length=50)),
                ('tipoRiesgo', models.CharField(choices=[('Enfermedad comun', 'Enfermedad comun'), ('Accidente', 'Accidente'), ('Maternidad', 'Maternidad')], max_length=20)),
                ('tipoIncapacidad', models.CharField(choices=[('Inicial', 'Inicial'), ('Prorroga', 'Prorroga')], max_length=50)),
                ('motivoIncapacidad', models.TextField()),
                ('diasIncapacidad', models.IntegerField()),
                ('fechaInicioIncapacidad', models.DateField()),
                ('fechaFinIncapacidad', models.DateField()),
                ('fechaEmisionIncapacidad', models.DateField()),
                ('Consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenExamenMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSolicitudExamen', models.DateField()),
                ('estadoOrden', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Procesando', 'Procesando'), ('Finalizado', 'Finalizado')], max_length=10)),
                ('CatalogoTipoExamen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoTipoExamen')),
                ('Consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoSangre', models.CharField(choices=[('A+', 'Tipo A+'), ('B+', 'Tipo B+'), ('AB+', 'Tipo AB+'), ('O+', 'Tipo O+'), ('A-', 'Tipo A-'), ('B-', 'Tipo B-'), ('AB-', 'Tipo AB-'), ('O-', 'Tipo O-')], max_length=3)),
                ('fechaNacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('estadoCivil', models.CharField(choices=[('S', 'Soltero/a'), ('C', 'Casado/a'), ('V', 'Divorciado/a')], max_length=2)),
                ('ocupacion', models.CharField(choices=[('Empleado Publico', 'Empleado Publico'), ('Empleado Privado', 'Empleado Privado'), ('Desempleado', 'Desempleado')], max_length=50)),
                ('Clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primerNombre', models.CharField(max_length=20)),
                ('segundoNombre', models.CharField(max_length=20)),
                ('tercerNombre', models.CharField(blank=True, max_length=20, null=True)),
                ('primerApellido', models.CharField(max_length=20)),
                ('segundoApellido', models.CharField(max_length=20)),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('dui', models.CharField(max_length=10)),
                ('telefonoFijo', models.CharField(blank=True, max_length=15, null=True)),
                ('telefonoMovil', models.CharField(blank=True, max_length=15, null=True)),
                ('correoElectronico', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecetaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEmisionReceta', models.DateField()),
                ('observacionesReceta', models.TextField(blank=True, max_length=100, null=True)),
                ('Consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='RecetaMedicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosis', models.TextField(max_length=100)),
                ('CatalogoMedicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoMedicamento')),
                ('RecetaMedica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.RecetaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenciaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicioSolicitado', models.CharField(max_length=20)),
                ('institucionRemitida', models.CharField(max_length=50)),
                ('hallazgosMedicos', models.TextField(blank=True, null=True)),
                ('impresionDiagnostica', models.TextField(blank=True, null=True)),
                ('doctorReferenciado', models.CharField(max_length=50)),
                ('motivoReferencia', models.TextField(blank=True, null=True)),
                ('fechaEmisionRef', models.DateField()),
                ('Consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaResultado', models.DateField()),
                ('descripcionResultado', models.TextField(blank=True, max_length=100, null=True)),
                ('CatalogoTipoExamen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoTipoExamen')),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Empleado')),
                ('Expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente')),
            ],
        ),
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presionArterial', models.CharField(max_length=10)),
                ('frecCardiaca', models.IntegerField()),
                ('frecRespiratoria', models.IntegerField()),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('fechaMedicion', models.DateField()),
                ('notas', models.TextField(blank=True, max_length=50, null=True)),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Empleado')),
                ('Expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('horaInicio', models.DateTimeField()),
                ('fechaFin', models.DateField()),
                ('horaFin', models.DateTimeField()),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='ContactoEmergencia',
            fields=[
                ('relacion', models.CharField(choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Hijo', 'Hijo'), ('Hermano', 'Hermano'), ('Otro', 'Otro')], max_length=20)),
                ('Persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='expediente.Persona')),
            ],
            bases=('expediente.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='Direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Direccion'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='Persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expediente.Persona'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Paciente'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='Persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expediente.Persona'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Empleado'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente'),
        ),
        migrations.AddField(
            model_name='constanciamedica',
            name='Consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Consulta'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='Direccion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expediente.Direccion'),
        ),
        migrations.AddField(
            model_name='archivoresultadoexamen',
            name='ResultadoExamen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.ResultadoExamen'),
        ),
        migrations.AddField(
            model_name='archivero',
            name='Clinica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Clinica'),
        ),
        migrations.AddField(
            model_name='archivero',
            name='Empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Empleado'),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='CatalogoEnfermedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.CatalogoEnfermedad'),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='Expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente'),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='Expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente'),
        ),
    ]
