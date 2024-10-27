
-- Insertar un usuario
INSERT INTO usuarios (cuil, nombre, apellido, correo, contrasena, pin, saldo)
VALUES ('20304050607', 'test', '01', 'test@test.com', '12345', '123', 1000000.00);


INSERT INTO broker (broker_name, broker_comision) VALUES 
('ARGbroker', 1.5);


INSERT INTO empresas (nombre_empresa) VALUES ('emp_A'), ('emp_B'), ('emp_C'), ('emp_D'), ('emp_E'), ('emp_F'), ('emp_G'), ('emp_H'), ('emp_I'), ('emp_J');


INSERT INTO cotizacion (precio_compra, precio_venta) VALUES 
(100.00, 110.00),
(200.00, 220.00),
(300.00, 330.00),
(400.00, 440.00),
(500.00, 550.00),
(600.00, 660.00),
(700.00, 770.00),
(800.00, 880.00),
(900.00, 990.00),
(1000.00, 1100.00);


INSERT INTO acciones (id_empresa, id_cotizacion, nombre_accion, precio_historico)
VALUES 
(1, 1, 'Accion_A', 100.00),
(2, 2, 'Accion_B', 200.00),
(3, 3, 'Accion_C', 300.00),
(4, 4, 'Accion_D', 400.00),
(5, 5, 'Accion_E', 500.00),
(6, 6, 'Accion_F', 600.00),
(7, 7, 'Accion_G', 700.00),
(8, 8, 'Accion_H', 800.00),
(9, 9, 'Accion_I', 900.00),
(10, 10, 'Accion_J', 1000.00);


INSERT INTO transacciones (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion) VALUES
(1, 1, 1, 'compra', 10, 100.00, 1000.00),
(1, 2, 2, 'compra', 20, 200.00, 4000.00),
(1, 3, 3, 'compra', 30, 300.00, 9000.00),
(1, 4, 4, 'compra', 40, 400.00, 16000.00),
(1, 5, 5, 'compra', 50, 500.00, 25000.00);


INSERT INTO transacciones (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion) VALUES
(1, 6, 6, 'venta', 60, 600.00, 36000.00),
(1, 7, 7, 'venta', 70, 700.00, 49000.00),
(1, 8, 8, 'venta', 80, 800.00, 64000.00),
(1, 9, 9, 'venta', 90, 900.00, 81000.00),
(1, 10, 10, 'venta', 100, 1000.00, 100000.00);

INSERT INTO portafolio (id_usuario, id_accion, id_cotizacion, cantidad_acciones, valor_comprometido, rendimiento_operacion) VALUES
(1, 1, 1, 10, 1000.00, 0.00),
(1, 2, 2, 20, 4000.00, 0.00),
(1, 3, 3, 30, 9000.00, 0.00),
(1, 4, 4, 40, 16000.00, 0.00),
(1, 5, 5, 50, 25000.00, 0.00);