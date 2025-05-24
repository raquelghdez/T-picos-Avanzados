/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.7.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: sistema_documentos
-- ------------------------------------------------------
-- Server version	11.7.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `alta_documentos`
--

DROP TABLE IF EXISTS `alta_documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `alta_documentos` (
  `id_altadocumento` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_documento` varchar(10) NOT NULL,
  `fecha_alta` datetime NOT NULL,
  PRIMARY KEY (`id_altadocumento`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_documento` (`id_documento`),
  CONSTRAINT `alta_documentos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `alta_documentos_ibfk_2` FOREIGN KEY (`id_documento`) REFERENCES `documentos` (`id_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alta_documentos`
--

LOCK TABLES `alta_documentos` WRITE;
/*!40000 ALTER TABLE `alta_documentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `alta_documentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alta_usuarios`
--

DROP TABLE IF EXISTS `alta_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `alta_usuarios` (
  `id_altausuario` int(11) NOT NULL,
  `id_usuario_directora` int(11) DEFAULT NULL,
  `id_usuario_nuevo` int(11) DEFAULT NULL,
  `fecha_altausuario` datetime DEFAULT NULL,
  PRIMARY KEY (`id_altausuario`),
  KEY `id_usuario_directora` (`id_usuario_directora`),
  KEY `id_usuario_nuevo` (`id_usuario_nuevo`),
  CONSTRAINT `alta_usuarios_ibfk_1` FOREIGN KEY (`id_usuario_directora`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `alta_usuarios_ibfk_2` FOREIGN KEY (`id_usuario_nuevo`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alta_usuarios`
--

LOCK TABLES `alta_usuarios` WRITE;
/*!40000 ALTER TABLE `alta_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `alta_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentos`
--

DROP TABLE IF EXISTS `documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentos` (
  `id_documento` varchar(10) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  `grupo` varchar(50) NOT NULL,
  `ciclo_escolar` varchar(50) NOT NULL,
  `ruta_archivo` varchar(255) NOT NULL,
  PRIMARY KEY (`id_documento`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`ciclo_escolar` regexp '^[0-9]{4}-[0-3]{1}$')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES
('AC1','Actas de Calificaciones','GAS7A','2025-1','C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/PRUEBA DEL PROYECTO/ACTAS CALIFICACIONES GAS7A 2025-1.pdf'),
('EX1','Extraordinarios','EDE1A','2025-1','C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/Präctica 6/Documentos digitalizados/EXTRAORDINARIO EDE1A 2025-1.pdf'),
('LA1','Listas de Asistencia','GAE1A','2025-1','C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/PRUEBA DEL PROYECTO/LISTA ASISTENCIA GAE1A 2025-1.pdf'),
('LA2','Listas de Asistencia','GAE1B','2023-1','C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/PRUEBA DEL PROYECTO/LISTA ASISTENCIA GAE1B 2023-1.pdf'),
('LA3','Listas de Asistencia','GAS1B','2024-1','C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/PRUEBA DEL PROYECTO/LISTA ASISTENCIA GAS1B 2024-1.pdf'),
('RC1','Recursamientos','PSE4A','2025-1','C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/Präctica 6/Documentos digitalizados/RECURSAMIENTO PSE4A 2025-1.pdf'),
('TS1','Títulos de Suficiencia','NUE9A','2023-3','C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/PRUEBA DEL PROYECTO/TITULO NUE9A 2023-3.pdf');
/*!40000 ALTER TABLE `documentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentos_seleccionado`
--

DROP TABLE IF EXISTS `documentos_seleccionado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentos_seleccionado` (
  `id_seleccion` int(11) NOT NULL,
  `grupo` varchar(50) NOT NULL,
  `ciclo_escolar` varchar(50) NOT NULL,
  `id_documento` varchar(10) NOT NULL,
  PRIMARY KEY (`id_seleccion`),
  KEY `id_documento` (`id_documento`),
  CONSTRAINT `documentos_seleccionado_ibfk_1` FOREIGN KEY (`id_documento`) REFERENCES `documentos` (`id_documento`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`ciclo_escolar` regexp '^[0-9]{4}-[0-3]{1}$')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos_seleccionado`
--

LOCK TABLES `documentos_seleccionado` WRITE;
/*!40000 ALTER TABLE `documentos_seleccionado` DISABLE KEYS */;
/*!40000 ALTER TABLE `documentos_seleccionado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intento_iniciosesion`
--

DROP TABLE IF EXISTS `intento_iniciosesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `intento_iniciosesion` (
  `id_intento` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_hora` datetime NOT NULL,
  `resultado` varchar(50) NOT NULL CHECK (`resultado` in ('Fallido','Exitoso')),
  `intentos_fallidos` int(11) DEFAULT 0 CHECK (`intentos_fallidos` <= 3),
  PRIMARY KEY (`id_intento`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `intento_iniciosesion_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intento_iniciosesion`
--

LOCK TABLES `intento_iniciosesion` WRITE;
/*!40000 ALTER TABLE `intento_iniciosesion` DISABLE KEYS */;
/*!40000 ALTER TABLE `intento_iniciosesion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisos`
--

DROP TABLE IF EXISTS `permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisos` (
  `id_permiso` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `tipo_accion` varchar(50) NOT NULL CHECK (`tipo_accion` = 'Alta Usuario'),
  PRIMARY KEY (`id_permiso`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `permisos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisos`
--

LOCK TABLES `permisos` WRITE;
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salir_sistema`
--

DROP TABLE IF EXISTS `salir_sistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `salir_sistema` (
  `id_salida` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) DEFAULT NULL,
  `fecha_salida` datetime DEFAULT NULL,
  `fecha_entrada` datetime DEFAULT NULL,
  PRIMARY KEY (`id_salida`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `salir_sistema_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salir_sistema`
--

LOCK TABLES `salir_sistema` WRITE;
/*!40000 ALTER TABLE `salir_sistema` DISABLE KEYS */;
INSERT INTO `salir_sistema` VALUES
(1,1,'2025-04-21 21:20:18',NULL),
(2,1,'2025-04-24 12:27:47',NULL),
(3,1,'2025-04-25 19:32:42',NULL),
(4,1,'2025-05-03 14:07:51',NULL),
(5,1,'2025-05-09 22:10:57','2025-05-09 22:10:51'),
(6,1,'2025-05-09 23:53:02','2025-05-09 23:53:01'),
(7,1,'2025-05-10 00:23:13','2025-05-10 00:23:09'),
(8,1,'2025-05-10 00:23:13','2025-05-10 00:23:09'),
(9,1,'2025-05-10 00:31:28','2025-05-10 00:31:25'),
(10,1,'2025-05-10 00:31:28','2025-05-10 00:31:25'),
(11,1,'2025-05-10 00:42:56','2025-05-10 00:42:54'),
(12,1,'2025-05-10 00:42:56','2025-05-10 00:42:55'),
(13,1,'2025-05-10 12:13:36','2025-05-10 12:12:30'),
(14,1,'2025-05-10 12:13:36','2025-05-10 12:12:30'),
(15,1,'2025-05-10 13:45:13','2025-05-10 13:44:51'),
(16,1,'2025-05-10 14:01:36','2025-05-10 14:00:58'),
(17,1,'2025-05-10 14:06:05','2025-05-10 14:05:58'),
(18,1,'2025-05-10 14:07:19','2025-05-10 14:07:14'),
(19,1,'2025-05-10 14:14:01','2025-05-10 14:13:46'),
(20,1,'2025-05-11 07:26:58','2025-05-11 07:14:05'),
(21,1,'2025-05-11 08:21:40','2025-05-11 07:27:31'),
(22,1,'2025-05-11 08:21:40','2025-05-11 07:27:31'),
(23,1,'2025-05-11 18:35:06','2025-05-11 17:28:25'),
(24,1,'2025-05-11 18:35:06','2025-05-11 17:28:26'),
(25,1,'2025-05-11 18:41:41','2025-05-11 18:41:07'),
(26,1,'2025-05-11 18:41:41','2025-05-11 18:41:07'),
(27,1,'2025-05-11 20:05:58','2025-05-11 19:01:34'),
(28,1,'2025-05-11 20:05:58','2025-05-11 19:01:34'),
(29,1,'2025-05-11 21:47:00','2025-05-11 21:45:54'),
(30,1,'2025-05-11 21:47:00','2025-05-11 21:45:54'),
(31,1,'2025-05-11 22:34:54','2025-05-11 22:06:09'),
(32,1,'2025-05-11 22:34:54','2025-05-11 22:06:10'),
(33,1,'2025-05-13 23:01:38','2025-05-13 23:01:30'),
(34,1,'2025-05-13 23:21:13','2025-05-13 23:20:15'),
(35,1,'2025-05-13 23:28:13','2025-05-13 23:28:06'),
(36,1,'2025-05-13 23:32:00','2025-05-13 23:31:21'),
(37,1,'2025-05-13 23:36:04','2025-05-13 23:34:55'),
(38,1,'2025-05-14 00:01:51','2025-05-13 23:38:34'),
(39,1,'2025-05-14 00:01:51','2025-05-13 23:44:56'),
(40,1,'2025-05-14 00:01:51','2025-05-14 00:01:31'),
(41,1,'2025-05-14 00:08:58','2025-05-14 00:06:22'),
(42,1,'2025-05-14 22:35:11','2025-05-14 22:34:09'),
(43,1,'2025-05-14 22:41:13','2025-05-14 22:35:30'),
(44,1,'2025-05-14 22:48:06','2025-05-14 22:41:33'),
(45,1,'2025-05-14 22:50:09','2025-05-14 22:48:32'),
(46,1,'2025-05-14 22:51:20','2025-05-14 22:50:26'),
(47,1,'2025-05-14 22:58:04','2025-05-14 22:51:50'),
(48,1,'2025-05-14 23:00:25','2025-05-14 22:58:27'),
(49,1,'2025-05-14 23:02:12','2025-05-14 23:00:43'),
(50,1,'2025-05-14 23:02:49','2025-05-14 23:02:28'),
(51,1,'2025-05-14 23:09:09','2025-05-14 23:08:58'),
(52,1,'2025-05-15 00:17:15','2025-05-14 23:13:38'),
(53,1,'2025-05-15 00:18:13','2025-05-15 00:17:46'),
(54,1,'2025-05-15 00:42:11','2025-05-15 00:24:30'),
(55,1,'2025-05-15 00:46:57','2025-05-15 00:44:50'),
(56,1,'2025-05-15 01:02:37','2025-05-15 00:49:59'),
(57,1,'2025-05-15 01:10:51','2025-05-15 01:05:43'),
(58,1,'2025-05-15 01:14:29','2025-05-15 01:11:55'),
(59,1,'2025-05-15 01:21:44','2025-05-15 01:19:10'),
(60,1,'2025-05-15 01:31:27','2025-05-15 01:22:41'),
(61,1,'2025-05-15 01:57:58','2025-05-15 01:31:48'),
(62,2,'2025-05-15 02:00:03','2025-05-15 01:59:02'),
(63,2,'2025-05-15 02:01:42','2025-05-15 02:00:48'),
(64,2,'2025-05-15 02:28:57','2025-05-15 02:28:55'),
(65,2,'2025-05-15 02:40:57','2025-05-15 02:40:55'),
(66,2,'2025-05-15 02:44:02','2025-05-15 02:43:59'),
(67,2,'2025-05-15 02:46:14','2025-05-15 02:46:12'),
(68,2,'2025-05-15 02:47:52','2025-05-15 02:47:51'),
(69,2,'2025-05-15 02:50:03','2025-05-15 02:50:01'),
(70,1,'2025-05-15 21:49:50','2025-05-15 21:42:54'),
(71,1,'2025-05-15 21:58:18','2025-05-15 21:58:17'),
(72,1,'2025-05-15 22:02:20','2025-05-15 22:02:19'),
(73,1,'2025-05-15 22:10:52','2025-05-15 22:10:50'),
(74,1,'2025-05-15 22:34:14','2025-05-15 22:34:12'),
(75,1,'2025-05-15 22:37:00','2025-05-15 22:36:57'),
(76,1,NULL,'2025-05-15 22:38:41'),
(77,1,NULL,'2025-05-15 22:44:41'),
(78,1,NULL,'2025-05-15 22:45:43'),
(79,1,NULL,'2025-05-15 22:48:51'),
(80,1,NULL,'2025-05-15 22:50:45'),
(81,1,NULL,'2025-05-15 22:55:44'),
(82,2,NULL,'2025-05-15 22:57:57'),
(83,1,NULL,'2025-05-15 23:07:34'),
(84,1,NULL,'2025-05-15 23:14:49'),
(85,1,NULL,'2025-05-15 23:15:48'),
(86,2,NULL,'2025-05-15 23:17:38'),
(87,2,NULL,'2025-05-15 23:20:41'),
(88,2,NULL,'2025-05-15 23:23:39'),
(89,1,NULL,'2025-05-15 23:27:30'),
(90,1,NULL,'2025-05-15 23:35:57'),
(91,1,NULL,'2025-05-15 23:46:15'),
(92,2,NULL,'2025-05-16 00:01:01'),
(93,1,NULL,'2025-05-16 00:08:40'),
(94,1,NULL,'2025-05-16 00:13:14'),
(95,1,NULL,'2025-05-16 00:14:09'),
(96,1,NULL,'2025-05-16 00:14:47'),
(97,1,NULL,'2025-05-16 00:18:44'),
(98,1,NULL,'2025-05-16 00:21:57'),
(99,1,NULL,'2025-05-16 00:23:30'),
(100,2,NULL,'2025-05-16 00:30:03'),
(101,1,NULL,'2025-05-16 00:34:08'),
(102,1,NULL,'2025-05-16 00:38:30'),
(103,1,NULL,'2025-05-16 00:40:09'),
(104,1,NULL,'2025-05-16 00:49:22'),
(105,2,NULL,'2025-05-16 00:49:46'),
(106,2,NULL,'2025-05-16 00:54:22'),
(107,2,NULL,'2025-05-16 00:59:58'),
(108,1,NULL,'2025-05-16 01:01:53'),
(109,2,NULL,'2025-05-16 01:16:26'),
(110,1,NULL,'2025-05-16 01:16:57'),
(111,1,NULL,'2025-05-16 01:19:15'),
(112,1,NULL,'2025-05-16 01:27:30'),
(113,2,NULL,'2025-05-16 01:28:25'),
(114,1,NULL,'2025-05-16 01:35:48'),
(115,1,NULL,'2025-05-16 01:38:51'),
(116,1,NULL,'2025-05-16 08:01:12'),
(117,2,NULL,'2025-05-16 08:14:39'),
(118,2,NULL,'2025-05-16 11:01:16'),
(119,2,NULL,'2025-05-16 19:56:55'),
(120,1,NULL,'2025-05-16 20:06:49'),
(121,1,NULL,'2025-05-16 20:25:33'),
(122,2,NULL,'2025-05-17 12:03:49'),
(123,1,NULL,'2025-05-17 12:33:33'),
(124,2,'2025-05-17 13:06:33','2025-05-17 13:06:28'),
(125,1,'2025-05-18 23:53:51','2025-05-18 23:53:40'),
(126,1,'2025-05-20 14:39:03','2025-05-20 14:34:45'),
(127,1,'2025-05-20 14:43:25','2025-05-20 14:40:41'),
(128,1,'2025-05-21 19:53:59','2025-05-21 19:52:33'),
(129,2,'2025-05-21 20:05:53','2025-05-21 20:02:36');
/*!40000 ALTER TABLE `salir_sistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `rol` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`nombre` regexp '^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$'),
  CONSTRAINT `CONSTRAINT_2` CHECK (`rol` in ('Directora','Auxiliar')),
  CONSTRAINT `CONSTRAINT_3` CHECK (`username` regexp '^[a-zA-Z0-9]+$'),
  CONSTRAINT `CONSTRAINT_4` CHECK (char_length(`password`) >= 8)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES
(1,'Raquel Garibaldo Hernández','Directora','al23760804@ite.edu.mx','RGH804','23760804'),
(2,'Cristina Ramírez Fernández','Auxiliar','cramirez@ite.edu.mx','CRF','IS4SSFBD'),
(3,'Diana Peralta Moreno','Auxiliar','auxdsae_ensenada@uva.edu.mx','DIANAP','diana123');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-05-21 20:15:12
