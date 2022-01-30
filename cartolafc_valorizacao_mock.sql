CREATE DATABASE  IF NOT EXISTS `cartolafc` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cartolafc`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: cartolafc
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `valorizacao_mock`
--

DROP TABLE IF EXISTS `valorizacao_mock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valorizacao_mock` (
  `id` int NOT NULL AUTO_INCREMENT,
  `local_id` varchar(200) DEFAULT NULL,
  `atletas_nome` varchar(200) DEFAULT NULL,
  `atletas_slug` varchar(200) DEFAULT NULL,
  `atletas_apelido` varchar(200) DEFAULT NULL,
  `atletas_foto` varchar(200) DEFAULT NULL,
  `atletas_atleta_id` varchar(200) DEFAULT NULL,
  `atletas_rodada_id` varchar(200) DEFAULT NULL,
  `atletas_clube_id` varchar(200) DEFAULT NULL,
  `atletas_posicao_id` varchar(200) DEFAULT NULL,
  `atletas_status_id` varchar(200) DEFAULT NULL,
  `atletas_pontos_num` varchar(200) DEFAULT NULL,
  `atletas_preco_num` varchar(200) DEFAULT NULL,
  `atletas_variacao_num` varchar(200) DEFAULT NULL,
  `atletas_media_num` varchar(200) DEFAULT NULL,
  `atletas_clube_id_full_name` varchar(200) DEFAULT NULL,
  `ANO` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valorizacao_mock`
--

LOCK TABLES `valorizacao_mock` WRITE;
/*!40000 ALTER TABLE `valorizacao_mock` DISABLE KEYS */;
INSERT INTO `valorizacao_mock` VALUES (1,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','1',NULL,'gol',NULL,'0','5',NULL,'0',NULL,'2019'),(2,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','3',NULL,'gol',NULL,'5.2','8.79',NULL,'3.15',NULL,'2018'),(3,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','2',NULL,'gol',NULL,'0','9.71',NULL,'1.1',NULL,'2018'),(4,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','4',NULL,'gol',NULL,'16.4','12.65',NULL,'7.57',NULL,'2018'),(5,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','3',NULL,'gol',NULL,'0','5',NULL,'0',NULL,'2019'),(6,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','4',NULL,'gol',NULL,'1','3.96',NULL,'1',NULL,'2019'),(7,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','2',NULL,'gol',NULL,'0','5',NULL,'0',NULL,'2019'),(8,NULL,'Diego Alves Carreira',NULL,NULL,NULL,'38509','1',NULL,'gol',NULL,'1.1','9.71',NULL,'1.1',NULL,'2018'),(9,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','4',NULL,'tec',NULL,'4.3','10.28',NULL,'3.58',NULL,'2019'),(10,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','3',NULL,'tec',NULL,'1.79','9.85',NULL,'3.34',NULL,'2019'),(11,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','2',NULL,'tec',NULL,'5.45','10.39',NULL,'4.53',NULL,'2018'),(12,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','1',NULL,'tec',NULL,'3.61','10.06',NULL,'3.61',NULL,'2018'),(13,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','4',NULL,'tec',NULL,'4.75','10.8',NULL,'4.41',NULL,'2018'),(14,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','2',NULL,'tec',NULL,'2.98','10.48',NULL,'4.12',NULL,'2019'),(15,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','3',NULL,'tec',NULL,'3.85','10.21',NULL,'4.3',NULL,'2018'),(16,NULL,'Abel Carlos da Silva Braga',NULL,NULL,NULL,'40006','1',NULL,'tec',NULL,'5.26','10.59',NULL,'5.26',NULL,'2019'),(17,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','3',NULL,'tec',NULL,'1.35','13.31',NULL,'4.37',NULL,'2018'),(18,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','3',NULL,'tec',NULL,'5.94','11.07',NULL,'4',NULL,'2019'),(19,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','4',NULL,'tec',NULL,'4.76','11.16',NULL,'4.19',NULL,'2019'),(20,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','1',NULL,'tec',NULL,'4.53','11.47',NULL,'4.53',NULL,'2019'),(21,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','1',NULL,'tec',NULL,'7.29','15.36',NULL,'7.29',NULL,'2018'),(22,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','2',NULL,'tec',NULL,'4.47','14.75',NULL,'5.88',NULL,'2018'),(23,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','2',NULL,'tec',NULL,'1.53','10.27',NULL,'3.03',NULL,'2019'),(24,NULL,'Renato Portaluppi',NULL,NULL,NULL,'41929','4',NULL,'tec',NULL,'9.02','15.21',NULL,'5.53',NULL,'2018'),(25,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','1',NULL,'lat',NULL,'3.4','5.83',NULL,'3.4',NULL,'2019'),(26,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','4',NULL,'lat',NULL,'6','11.27',NULL,'7.83',NULL,'2019'),(27,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','4',NULL,'lat',NULL,'0','11.7',NULL,'4.4',NULL,'2018'),(28,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','2',NULL,'lat',NULL,'13','14.11',NULL,'6.75',NULL,'2018'),(29,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','1',NULL,'lat',NULL,'0.5','12.06',NULL,'0.5',NULL,'2018'),(30,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','2',NULL,'lat',NULL,'14.1','11.32',NULL,'8.75',NULL,'2019'),(31,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','3',NULL,'lat',NULL,'-0.3','11.7',NULL,'4.4',NULL,'2018'),(32,NULL,'Fagner Conserva Lemos',NULL,NULL,NULL,'42500','3',NULL,'lat',NULL,'0','11.32',NULL,'8.75',NULL,'2019'),(33,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','2',NULL,'zag',NULL,'-0.3','4.14',NULL,'0.1',NULL,'2018'),(34,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','1',NULL,'zag',NULL,'4','6.24',NULL,'4',NULL,'2019'),(35,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','2',NULL,'zag',NULL,'8','9.14',NULL,'6',NULL,'2019'),(36,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','4',NULL,'zag',NULL,'6','4.91',NULL,'1.33',NULL,'2018'),(37,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','1',NULL,'zag',NULL,'0.5','5.86',NULL,'0.5',NULL,'2018'),(38,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','4',NULL,'zag',NULL,'0','8.82',NULL,'4.5',NULL,'2019'),(39,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','3',NULL,'zag',NULL,'-0.9','3.28',NULL,'-0.23',NULL,'2018'),(40,NULL,'Ernando Rodrigues Lopes',NULL,NULL,NULL,'49651','3',NULL,'zag',NULL,'6','9.93',NULL,'6',NULL,'2019'),(41,NULL,'Everton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','3',NULL,'mei',NULL,'0','13.93',NULL,'4.5',NULL,'2019'),(42,NULL,'Everton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','4',NULL,'mei',NULL,'-0.3','11.83',NULL,'2.9',NULL,'2019'),(43,NULL,'Éverton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','4',NULL,'mei',NULL,'9.8','4.72',NULL,'2.87',NULL,'2018'),(44,NULL,'Everton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','2',NULL,'mei',NULL,'0.6','13.93',NULL,'4.5',NULL,'2019'),(45,NULL,'Éverton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','3',NULL,'mei',NULL,'4.6','2.47',NULL,'-0.6',NULL,'2018'),(46,NULL,'Éverton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','1',NULL,'mei',NULL,'-5.8','2.89',NULL,'-5.8',NULL,'2018'),(47,NULL,'Everton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','1',NULL,'mei',NULL,'8.4','15.54',NULL,'8.4',NULL,'2019'),(48,NULL,'Éverton Augusto de Barros Ribeiro',NULL,NULL,NULL,'51772','2',NULL,'mei',NULL,'0','2.89',NULL,'-5.8',NULL,'2018'),(49,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','1',NULL,'zag',NULL,'0','16',NULL,'0',NULL,'2019'),(50,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','2',NULL,'zag',NULL,'8.3','18.02',NULL,'9.2',NULL,'2018'),(51,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','4',NULL,'zag',NULL,'3.6','11.15',NULL,'2.3',NULL,'2019'),(52,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','4',NULL,'zag',NULL,'6','18.22',NULL,'7.67',NULL,'2018'),(53,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','1',NULL,'zag',NULL,'10.1','16.6',NULL,'10.1',NULL,'2018'),(54,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','2',NULL,'zag',NULL,'1.5','12.23',NULL,'1.5',NULL,'2019'),(55,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','3',NULL,'zag',NULL,'6.3','17.78',NULL,'8.23',NULL,'2018'),(56,NULL,'Réver Humberto Alves Araújo',NULL,NULL,NULL,'52253','3',NULL,'zag',NULL,'1.8','11.14',NULL,'1.65',NULL,'2019'),(57,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','3',NULL,'gol',NULL,'3.7','5.75',NULL,'1.7',NULL,'2019'),(58,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','4',NULL,'gol',NULL,'-4','3.82',NULL,'0.28',NULL,'2019'),(59,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','1',NULL,'gol',NULL,'4.1','12.47',NULL,'4.1',NULL,'2018'),(60,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','2',NULL,'gol',NULL,'1','10.35',NULL,'2.55',NULL,'2018'),(61,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','3',NULL,'gol',NULL,'7.7','11.57',NULL,'4.27',NULL,'2018'),(62,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','2',NULL,'gol',NULL,'3.4','5.41',NULL,'0.7',NULL,'2019'),(63,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','1',NULL,'gol',NULL,'-2','6.24',NULL,'-2',NULL,'2019'),(64,NULL,'Victor Leandro Bagy',NULL,NULL,NULL,'52950','4',NULL,'gol',NULL,'-4.3','9.04',NULL,'2.13',NULL,'2018'),(65,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','1',NULL,'zag',NULL,'0.4','14.15',NULL,'0.4',NULL,'2019'),(66,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','3',NULL,'zag',NULL,'8.7','15.63',NULL,'6.57',NULL,'2019'),(67,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','2',NULL,'zag',NULL,'2.1','5.86',NULL,'2.4',NULL,'2018'),(68,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','3',NULL,'zag',NULL,'0','5.86',NULL,'2.4',NULL,'2018'),(69,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','2',NULL,'zag',NULL,'10.6','14.95',NULL,'5.5',NULL,'2019'),(70,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','4',NULL,'zag',NULL,'9.6','16.62',NULL,'7.33',NULL,'2019'),(71,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','4',NULL,'zag',NULL,'15.8','9.69',NULL,'6.87',NULL,'2018'),(72,NULL,'Anderson Vital da Silva',NULL,NULL,NULL,'60819','1',NULL,'zag',NULL,'2.7','5.99',NULL,'2.7',NULL,'2018'),(73,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','2',NULL,'gol',NULL,'1','7.54',NULL,'1.5',NULL,'2019'),(74,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','1',NULL,'gol',NULL,'5.2','7.72',NULL,'5.2',NULL,'2018'),(75,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','2',NULL,'gol',NULL,'0','7.72',NULL,'5.2',NULL,'2018'),(76,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','1',NULL,'gol',NULL,'2','9.02',NULL,'2',NULL,'2019'),(77,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','4',NULL,'gol',NULL,'4','8.29',NULL,'2.88',NULL,'2019'),(78,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','3',NULL,'gol',NULL,'0','7.72',NULL,'5.2',NULL,'2018'),(79,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','3',NULL,'gol',NULL,'4.5','8.11',NULL,'2.5',NULL,'2019'),(80,NULL,'Marcelo Lomba do Nascimento',NULL,NULL,NULL,'68872','4',NULL,'gol',NULL,'0','7.72',NULL,'5.2',NULL,'2018'),(81,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','1',NULL,'ata',NULL,'0.4','6.48',NULL,'0.4',NULL,'2018'),(82,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','3',NULL,'ata',NULL,'0.5','1.87',NULL,'0.3',NULL,'2019'),(83,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','1',NULL,'ata',NULL,'-1.6','2.36',NULL,'-1.6',NULL,'2019'),(84,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','2',NULL,'ata',NULL,'-2.4','3.66',NULL,'-1',NULL,'2018'),(85,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','3',NULL,'ata',NULL,'0.7','3.44',NULL,'-0.43',NULL,'2018'),(86,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','4',NULL,'ata',NULL,'-1.2','1.33',NULL,'-0.08',NULL,'2019'),(87,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','4',NULL,'ata',NULL,'1.7','3.63',NULL,'0.1',NULL,'2018'),(88,NULL,'Rodrigo Pimpão Viana',NULL,NULL,NULL,'68901','2',NULL,'ata',NULL,'2','2.11',NULL,'0.2',NULL,'2019'),(89,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','3',NULL,'lat',NULL,'10.8','10.43',NULL,'7.5',NULL,'2018'),(90,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','1',NULL,'lat',NULL,'0.6','8.74',NULL,'0.6',NULL,'2019'),(91,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','2',NULL,'lat',NULL,'-1.1','6.02',NULL,'-0.25',NULL,'2019'),(92,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','2',NULL,'lat',NULL,'9.4','8.15',NULL,'5.85',NULL,'2018'),(93,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','1',NULL,'lat',NULL,'2.3','5.03',NULL,'2.3',NULL,'2018'),(94,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','4',NULL,'lat',NULL,'0','6.02',NULL,'-0.25',NULL,'2019'),(95,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','4',NULL,'lat',NULL,'9','11.73',NULL,'7.88',NULL,'2018'),(96,NULL,'Renê Rodrigues Martins',NULL,NULL,NULL,'78445','3',NULL,'lat',NULL,'0','6.02',NULL,'-0.25',NULL,'2019'),(97,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','1',NULL,'mei',NULL,'5.5','8.61',NULL,'5.5',NULL,'2018'),(98,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','1',NULL,'mei',NULL,'3.8','10.96',NULL,'3.8',NULL,'2019'),(99,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','3',NULL,'mei',NULL,'1.2','8.4',NULL,'1.67',NULL,'2019'),(100,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','2',NULL,'mei',NULL,'2.9','8.83',NULL,'4.2',NULL,'2018'),(101,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','3',NULL,'mei',NULL,'0','8.83',NULL,'4.2',NULL,'2018'),(102,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','2',NULL,'mei',NULL,'0','9.03',NULL,'1.9',NULL,'2019'),(103,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','4',NULL,'mei',NULL,'0','7.66',NULL,'1.25',NULL,'2019'),(104,NULL,'Jean Mota Oliveira de Sousa',NULL,NULL,NULL,'78548','4',NULL,'mei',NULL,'11.4','11.02',NULL,'6.6',NULL,'2018'),(105,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','1',NULL,'ata',NULL,'0','22',NULL,'0',NULL,'2019'),(106,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','3',NULL,'ata',NULL,'3.2','16.88',NULL,'4.5',NULL,'2019'),(107,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','2',NULL,'ata',NULL,'5.8','18.43',NULL,'5.8',NULL,'2019'),(108,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','3',NULL,'ata',NULL,'0.8','16.07',NULL,'6.23',NULL,'2018'),(109,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','2',NULL,'ata',NULL,'-0.9','17.41',NULL,'8.95',NULL,'2018'),(110,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','4',NULL,'ata',NULL,'6.8','17.3',NULL,'5.27',NULL,'2019'),(111,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','1',NULL,'ata',NULL,'18.8','17.77',NULL,'18.8',NULL,'2018'),(112,NULL,'Nicolás Federico López Alonso',NULL,NULL,NULL,'84709','4',NULL,'ata',NULL,'0','16.07',NULL,'6.23',NULL,'2018'),(113,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','3',NULL,'mei',NULL,'9.7','9.43',NULL,'4.7',NULL,'2019'),(114,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','1',NULL,'mei',NULL,'0','10',NULL,'0',NULL,'2019'),(115,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','1',NULL,'mei',NULL,'0','3',NULL,'0',NULL,'2018'),(116,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','2',NULL,'mei',NULL,'0','3',NULL,'0',NULL,'2018'),(117,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','2',NULL,'mei',NULL,'-0.3','7.1',NULL,'-0.3',NULL,'2019'),(118,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','3',NULL,'mei',NULL,'0','3',NULL,'0',NULL,'2018'),(119,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','4',NULL,'mei',NULL,'0','3',NULL,'0',NULL,'2018'),(120,NULL,'Alex Paulo Menezes Santana',NULL,NULL,NULL,'85465','4',NULL,'mei',NULL,'10','10.78',NULL,'6.47',NULL,'2019'),(121,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','3',NULL,'ata',NULL,'10.9','16.99',NULL,'7.07',NULL,'2019'),(122,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','3',NULL,'ata',NULL,'0','13.16',NULL,'7.5',NULL,'2018'),(123,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','1',NULL,'ata',NULL,'10.6','16.37',NULL,'10.6',NULL,'2019'),(124,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','2',NULL,'ata',NULL,'-0.3','14.78',NULL,'5.15',NULL,'2019'),(125,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','4',NULL,'ata',NULL,'0.6','15.03',NULL,'5.45',NULL,'2019'),(126,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','2',NULL,'ata',NULL,'5','13.16',NULL,'7.5',NULL,'2018'),(127,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','1',NULL,'ata',NULL,'10','11.71',NULL,'10',NULL,'2018'),(128,NULL,'Everton Sousa Soares',NULL,NULL,NULL,'86757','4',NULL,'ata',NULL,'18.4','16.92',NULL,'11.13',NULL,'2018'),(129,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','1',NULL,'mei',NULL,'9.9','17.15',NULL,'9.9',NULL,'2018'),(130,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','3',NULL,'mei',NULL,'0','15.74',NULL,'6',NULL,'2018'),(131,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','3',NULL,'mei',NULL,'0','13.75',NULL,'6.55',NULL,'2019'),(132,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','4',NULL,'mei',NULL,'0','13.75',NULL,'6.55',NULL,'2019'),(133,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','2',NULL,'mei',NULL,'2.1','15.74',NULL,'6',NULL,'2018'),(134,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','1',NULL,'mei',NULL,'1.5','11.45',NULL,'1.5',NULL,'2019'),(135,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','4',NULL,'mei',NULL,'13.2','17.55',NULL,'8.4',NULL,'2018'),(136,NULL,'Giorgian Daniel de Arrascaeta Benedetti',NULL,NULL,NULL,'87863','2',NULL,'mei',NULL,'11.6','13.75',NULL,'6.55',NULL,'2019'),(137,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','3',NULL,'zag',NULL,'-1.6','10.13',NULL,'2.17',NULL,'2018'),(138,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','4',NULL,'zag',NULL,'0.6','9.77',NULL,'3.63',NULL,'2019'),(139,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','1',NULL,'zag',NULL,'9.2','13.92',NULL,'9.2',NULL,'2018'),(140,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','3',NULL,'zag',NULL,'7.1','11.03',NULL,'5.15',NULL,'2019'),(141,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','2',NULL,'zag',NULL,'-1.1','11.92',NULL,'4.05',NULL,'2018'),(142,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','1',NULL,'zag',NULL,'0','12',NULL,'0',NULL,'2019'),(143,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','2',NULL,'zag',NULL,'3.2','10.07',NULL,'3.2',NULL,'2019'),(144,NULL,'Igor Rabello da Costa',NULL,NULL,NULL,'89493','4',NULL,'zag',NULL,'4.2','11',NULL,'2.68',NULL,'2018'),(145,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','3',NULL,'tec',NULL,'5.25','9.85',NULL,'4.85',NULL,'2018'),(146,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','2',NULL,'tec',NULL,'1.35','9.08',NULL,'4.65',NULL,'2018'),(147,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','1',NULL,'tec',NULL,'7.95','8.92',NULL,'7.95',NULL,'2018'),(148,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','1',NULL,'tec',NULL,'2.65','7.39',NULL,'2.65',NULL,'2019'),(149,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','2',NULL,'tec',NULL,'5.16','8.35',NULL,'3.91',NULL,'2019'),(150,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','3',NULL,'tec',NULL,'2.62','8.11',NULL,'3.48',NULL,'2019'),(151,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','4',NULL,'tec',NULL,'5.85','9.07',NULL,'4.07',NULL,'2019'),(152,NULL,'Odair Hellmann',NULL,NULL,NULL,'92273','4',NULL,'tec',NULL,'1.75','9.47',NULL,'4.08',NULL,'2018'),(153,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','2',NULL,'lat',NULL,'1.1','9.73',NULL,'4.7',NULL,'2018'),(154,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','1',NULL,'lat',NULL,'8.3','9.85',NULL,'8.3',NULL,'2018'),(155,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','2',NULL,'lat',NULL,'0','8.68',NULL,'0',NULL,'2019'),(156,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','3',NULL,'lat',NULL,'3.9','8.82',NULL,'1.95',NULL,'2019'),(157,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','1',NULL,'lat',NULL,'0','12',NULL,'0',NULL,'2019'),(158,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','4',NULL,'lat',NULL,'-0.2','8.95',NULL,'3.08',NULL,'2018'),(159,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','4',NULL,'lat',NULL,'-0.8','7.54',NULL,'1.03',NULL,'2019'),(160,NULL,'Iago Amaral Borduchi',NULL,NULL,NULL,'97868','3',NULL,'lat',NULL,'3.1','9.72',NULL,'4.17',NULL,'2018');
/*!40000 ALTER TABLE `valorizacao_mock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-29 22:33:12
