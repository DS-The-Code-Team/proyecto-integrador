INSERT INTO usuarios (id_usuario, cuil, nombre, apellido, correo, contrasena, pin, saldo, fecha_registro) VALUES
('1', '20348537808', 'Juan', 'Cabalango', 'juancabalango01@gmail.com', '12345', '345', 1000000.00,'2024-05-20 10:54:34'),
('2','23234567281', 'Ariel', 'Marquez',  'marquezariel@outlook.com', '37582', '582', 1000000.00, '2024-07-21 11:24:54'),
('3','27358394562', 'Marta', 'Albanesi', 'marta_albanesi@gmai.com', '843956', '956', 1000000.00, '2024-08-19 03:45:04'),
('4','20385475724', 'Fabricio', 'Tello',  'fabricio.tello@gmail.com', '18456', '456', 1000000.00, '2024-05-02 12:27:11'),
('5','27438574859', 'Elena', 'Murciel',  'elenamurciel.ok@outlook.com', '90453', '453', 1000000.00, '2024-02-16 07:07:07'),
('6','23248573012', 'Tamara', 'Camino',  'caminotamara02@gmail.com', '47538', '538', 1000000.00, '2024-03-04 02:43:12'),
('7', '23418483729', 'Roberto', 'Vega',  'vega_roberto@gmail.com', '84637', '637', 1000000.00, '2024-04-29 05:12:57'),
('8','27479227324', 'Lisa', 'Mandorian',  'lisamandorian2011@gmail.com', '37459', '459', 1000000.00, '2024-02-22 06:23:34'),
('9','20383446331', 'Federico', 'Prado',  'fedeprado@gmail.com', '85432', '432', 1000000.00, '2024-01-31 11:54:34'),
('10','23157383325', 'Ana', 'Lobos',  'ana_lobos.01@gmail.com', '47384', '384', 1000000.00, '2024-09-19 05:22:07');


INSERT INTO empresas (id_empresa, nombre_empresa) VALUES 
('1', 'Arcor'), 
('2', 'Google'), 
('3', 'Meta'), 
('4', 'Banco Macro'), 
('5', 'Libertad SRL'), 
('6', 'Grupo Financiero Galicia'), 
('7', 'Metrogas'), 
('8', 'Telecom Argentina'), 
('9', 'YPF'), 
('10', 'Grupo Superville');


INSERT INTO cotizacion (id_cotizacion, precio_compra, precio_venta, fecha_cotizacion) VALUES 
('1', '824.82', '822.82', '2024-10-25 11:10:45'),
('2', '934.35', '925.77', '2024-10-25 11:10:45'),
('3', '1134.23', '1124.56', '2024-10-25 11:10:45'),
('4', '2845.78', '2825.78', '2024-10-25 11:10:45'),
('5', '5678.55', '5658.35', '2024-10-25 11:10:45'),
('6', '10465.33', '10405.23', '2024-10-25 11:10:45'),
('7', '9234.44', '9212.34', '2024-10-25 11:10:45'),
('8', '67734.00', '67687.00', '2024-10-25 11:10:45'),
('9', '223.82', '213.82', '2024-10-25 11:10:45'),
('10', '7765.99', '7754.82', '2024-10-25 11:10:45');


INSERT INTO acciones (id_accion, id_empresa, id_cotizacion, nombre_accion, precio_historico, fecha_actualzacion)
VALUES 
('1' ,'1' ,'1' ,'Accion_Arcor', 800.00, '2024-10-20 11:11:59'),
('2' ,'2' ,'2' ,'Accion_Google', 900.00, '2024-10-20 11:11:59'),
('3' ,'3' ,'3' ,'Accion_Meta', 11000.00, '2024-10-20 11:11:59'),
('4' ,'4' ,'4' ,'Accion_BancoMacro', 28000.00, '2024-10-20 11:11:59'),
('5' ,'5' ,'5' ,'Accion_LibertadSRL', 5600.00, '2024-10-20 11:11:59'),
('6' ,'6' ,'6' ,'Accion_GrupoFinancieroGalicia', 10400.00, '2024-10-20 11:11:59'),
('7' ,'7' ,'7' ,'Accion_Metrogas', 9200.00, '2024-10-20 11:11:59'),
('8' ,'8' ,'8' ,'Accion_TelecomArgentina', 67600.00, '2024-10-20 11:11:59'),
('9' ,'9' ,'9' ,'Accion_YPF', 200.00, '2024-10-20 11:11:59'),
('10' ,'10' ,'10' ,'Accion_GrupoSuperville', 7700.00, '2024-10-20 11:11:59');


INSERT INTO transacciones (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion) VALUES
('1' ,'1' ,'1' ,'compra' , '9' , '824.82' ,'7423.38'),
('1' ,'2' ,'2' ,'compra' , '12', '934.35','11212.20'),
('3' ,'3' ,'3' ,'compra' , '24' , '1134.23', '27221.52'),
('3' ,'4' ,'4' ,'compra' , 35, '2845.78', '99602.30'),
('6' ,'5' ,'5' ,'compra' , 49, '5678.55', '278248.95');


INSERT INTO transacciones (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion) VALUES
('2' ,'6' ,'6' ,'venta', '12' , '10405.23', '124862.76'),
('2' ,'7' ,'7' ,'venta', '34' , '9212.34', '313219.56'),
('5' ,'8' ,'8' ,'venta' , '8', '67867.00', '542936.00'),
('7' ,'9' ,'9' ,'venta' , '17', '213.82', '3634.94'),
('9' ,'10' ,'10' ,'venta' , '22', '7754.82', '170606.04');

INSERT INTO portafolio (id_usuario, id_accion, id_cotizacion, cantidad_acciones, valor_comprometido, rendimiento_operacion) VALUES
('1', '1', '1', '9', '8000.00', '8465.00'),
('1', '2', '2','12', '12000.00', '384755.00'),
('1','3','3','10', '12000.00', '1823263.00'),
('1','4','4','33', '96000.00', '28324463.00'),
('1','5','5','46', '263000.00', '57383.00');
