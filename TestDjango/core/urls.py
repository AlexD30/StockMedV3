from django.urls import path
from.views import Admin_General,Registro_Cuenta_Admin, ingresarSolictud,Ver_solicitud,limpiarListado,agregar_producto,Registro_Cuenta_Instructor,Admin_Taller, Eliminar_sector,Modificar_sector,Ver_sector,AceptarPostulacion,EvaluarPostulacion,registro,crear_Taller, home, Form_Inscripcion_Taller, Form_Instructor_Taller,Ins_Taller,Form_Evaluacion,crear_Material, Admin_Perfil, Admin_Muni, Admin_Postulacion, Admin_Pago, Admin_Cliente,Admin_Banner_Promocion,Admin_Instructor, Tus_Talleres,Modificar_Material,Eliminar_Material,Validar_Postulacion, Ver_Material, Admin_sectores, crear_sector, HistoricoSolicitud

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('Form_Inscripcion_Taller/', Form_Inscripcion_Taller, name="Form_Inscripcion_Taller"),
    path('Form_Instructor_Taller/', Form_Instructor_Taller, name="Form_Instructor_Taller"),
    path('PostularTaller/',Ins_Taller, name="Ins_Taller"),
    path('AdministradorTaller/',Admin_Taller, name="Admin_Taller"),
    path('Form_Evaluacion/',Form_Evaluacion, name="Form_Evaluacion"),
    path('AdministradorGeneral', Admin_General,name="Admin_General"),
    path('adminsectores', Admin_sectores, name="Admin_sectores"),
    path('crearTaller', crear_Taller,name="crear_Taller"),
    path('CrearMaterial', crear_Material,name="crear_Material"),
    path('CrearSector', crear_sector,name="crear_sector"),
    path('HistoricoSolicitud', HistoricoSolicitud,name="HistoricoSolicitud"),
    path('AdminPerfilesUsuarios', Admin_Perfil,name="Admin_Perfil"),
    path('AdminMunicipios', Admin_Muni,name="Admin_Muni"),
    path('AdminPago', Admin_Pago,name="Admin_Pago"),
    path('AdminPostulacion', Admin_Postulacion,name="Admin_Postulacion"),
    path('AdminClientes', Admin_Cliente,name="Admin_Cliente"),
    path('Admin_Instructor', Admin_Instructor,name="Admin_Instructor"),
    path('Admin_Banner', Admin_Banner_Promocion,name="Admin_Banner"),
    path('TusTalleres', Tus_Talleres,name="Tus_Talleres"),
    path('Modificar_Material/<id>/', Modificar_Material, name="Modificar_Material"),
    path('Eliminar_Material/<id>/',Eliminar_Material, name="form_borrar_producto"),
    path('EvaluarPostulacion/<id>/', EvaluarPostulacion,name="EvaluarPostulacion"),
    path('registro',registro, name="registro"),
    path('Validar_Postulacion/<id>/',Validar_Postulacion, name="Validar_Postulacion"),
    path('AceptarPostulacion/<id>/', AceptarPostulacion,name="AceptarPostulacion"),
    path('Ver_Material/<id>/', Ver_Material,name="Ver_Material"),
    path('Registro_Cuenta_Admin',Registro_Cuenta_Admin, name="Registro_Cuenta_Admin"),
    path('Registro_Cuenta_Instructor',Registro_Cuenta_Instructor, name="Registro_Cuenta_Instructor"),
    path('Ver_sector/<id>/', Ver_sector,name="Ver_sector"),
    path('Modificar_sector/<id>/', Modificar_sector, name="Modificar_sector"),
    path('Eliminar_sector/<id>/',Eliminar_sector, name="Eliminar_sector"),
    path('agregar_producto/<producto_id>/', agregar_producto, name="Add"),
    path('limpiarListado', limpiarListado, name="limpiarListado"),
    path('Ver_solicitud', Ver_solicitud,name="Ver_solicitud"),
    path('ingresarSolictud', ingresarSolictud,name="ingresarSolictud"),





]

