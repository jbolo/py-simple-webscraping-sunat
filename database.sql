-- Host: localhost    Database: sunat

DROP TABLE IF EXISTS `padron_reducido_ruc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `padron_reducido_ruc` (
    `ruc`   varchar(20),
    `nombre`   varchar(100),
    `estado`   varchar(100),
    `condicion`   varchar(100),
    `ubigeo`   varchar(100),
    `tipo_via`   varchar(100),
    `nombre_via`   varchar(100),
    `codigo_zona`   varchar(100),
    `tipo_zona`   varchar(100),
    `numero`   varchar(100),
    `interior`   varchar(100),
    `lote`   varchar(100),
    `departamento`   varchar(100),
    `manzana`   varchar(100),
    `kilometro`   varchar(100),
    `adicional`   varchar(100)
);