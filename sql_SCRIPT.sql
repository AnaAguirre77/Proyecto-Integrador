SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema petShop
-- -----------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `petShop` DEFAULT CHARACTER SET utf8 ;
USE `petShop` ;

-- -----------------------------------------------------
-- Table `Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Proveedores` (
  `CUIT_Proveedor` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Telefono` INT NOT NULL,
  PRIMARY KEY (`CUIT_Proveedor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Categoria` (
  `ID_Categoria` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_Categoria`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Productos` (
  `Codigo_de_barras` INT NOT NULL,
  `Nombre` VARCHAR(30) NOT NULL,
  `Precio_Unitario` DECIMAL(10,2) NOT NULL,
  `Stock` INT NOT NULL,
  `ID_Categoria` INT NOT NULL,
  `Descripcion` VARCHAR(45) NOT NULL,
  `CUIT_Proveedor` INT NOT NULL,
  PRIMARY KEY (`Codigo_de_barras`),
  INDEX `fk_Productos_Proveedores_idx` (`CUIT_Proveedor` ASC),
  INDEX `fk_Productos_Categoria1_idx` (`ID_Categoria` ASC),
  CONSTRAINT `fk_Productos_Proveedores`
    FOREIGN KEY (`CUIT_Proveedor`)
    REFERENCES `Proveedores` (`CUIT_Proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Productos_Categoria1`
    FOREIGN KEY (`ID_Categoria`)
    REFERENCES `Categoria` (`ID_Categoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Ventas` (
  `ID_Venta` INT NOT NULL AUTO_INCREMENT,
  `Fecha` DATETIME NOT NULL,
  `Forma_Pago` VARCHAR(45) NULL,
  `Descuento` DECIMAL(5,2) NULL,
  `Total_Venta` DECIMAL(10,2) NOT NULL,
  `ID_Sucursal` INT NOT NULL,
  PRIMARY KEY (`ID_Venta`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Detalle_Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Detalle_Ventas` (
  `ID_Venta` INT NOT NULL,
  `Codigo_de_barras` INT NOT NULL,
  `Cantidad_Unidades` INT NOT NULL,
  `Precio_Unitario` DECIMAL(10,2) NOT NULL,
  `Descuento` DECIMAL(5,2) NULL,
  `Total_Item` DECIMAL(10,2) NOT NULL,
  INDEX `fk_Detalle_Ventas_Productos1_idx` (`Codigo_de_barras` ASC),
  INDEX `fk_Detalle_Ventas_Ventas1_idx` (`ID_Venta` ASC),
  PRIMARY KEY (`ID_Venta`, `Codigo_de_barras`),
  CONSTRAINT `fk_Detalle_Ventas_Productos1`
    FOREIGN KEY (`Codigo_de_barras`)
    REFERENCES `Productos` (`Codigo_de_barras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Detalle_Ventas_Ventas1`
    FOREIGN KEY (`ID_Venta`)
    REFERENCES `Ventas` (`ID_Venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Sucursales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sucursales` (
  `ID_Sucursal` INT NOT NULL AUTO_INCREMENT,
  `Ciudad` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  `Telefono` INT NOT NULL,
  `Email` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_Sucursal`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Producto_Sucursal_Stock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Producto_Sucursal_Stock` (
  `Codigo_de_barras` INT NOT NULL,
  `ID_Sucursal` INT NOT NULL,
  `Cantidad_Stock` INT NOT NULL,
  INDEX `fk_Producto_Sucursal_Stock_Sucursales1_idx` (`ID_Sucursal` ASC),
  INDEX `fk_Producto_Sucursal_Stock_Productos1_idx` (`Codigo_de_barras` ASC),
  PRIMARY KEY (`Codigo_de_barras`, `ID_Sucursal`),
  CONSTRAINT `fk_Producto_Sucursal_Stock_Sucursales1`
    FOREIGN KEY (`ID_Sucursal`)
    REFERENCES `Sucursales` (`ID_Sucursal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Sucursal_Stock_Productos1`
    FOREIGN KEY (`Codigo_de_barras`)
    REFERENCES `Productos` (`Codigo_de_barras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
