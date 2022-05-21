CREATE DATABASE musicpro;

USE musicpro;

CREATE TABLE instrumento(
    id_instrumento int NOT NULL AUTO_INCREMENT,
    nombre varchar(100) NOT NULL,
    stock int NOT NULL,
    precio int NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    id_almacen int,
    PRIMARY KEY (id_instrumento, id_almacen)
);
CREATE TABLE almacen(
    id_almacen int NOT NULL AUTO_INCREMENT,
    nombre_almacen varchar(100) NOT NULL,
    tipo_estructura varchar(100)NOT NULL,
    PRIMARY KEY (id_almacen)
);
CREATE TABLE tipo_instrumento (
    id_tipo int NOT NULL AUTO_INCREMENT,
    descripcion varchar(100) NOT NULL,
    PRIMARY KEY(id_tipo)
);

ALTER TABLE instrumento
ADD CONSTRAINT FK_instrumentoalmacen
FOREIGN KEY (id_almacen) REFERENCES almacen(id_almacen);


INSERT INTO instrumento(nombre, stock, precio, id_almacen) VALUES('Guitarra', 50,250000, 1), ('Amplificador', 200,189000, 1);
INSERT INTO tipo_instrumento(descripcion) VALUES('Instrumentos de cuerda'), ('Instrumentos de percusion');
INSERT INTO almacen(nombre_almacen, tipo_estructura) VALUES('Vina del mar', 'Sucursal'), ('Santiago','Sucursal'), ('Bodega central','Bodega');