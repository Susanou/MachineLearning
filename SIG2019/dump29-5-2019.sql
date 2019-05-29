-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: SIG
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `frequences`
--

DROP TABLE IF EXISTS `frequences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frequences` (
  `mot` int(11) DEFAULT NULL,
  `theme` int(11) DEFAULT NULL,
  `frequence` int(255) DEFAULT '1',
  KEY `mot_freq` (`mot`),
  KEY `theme_freq` (`theme`),
  CONSTRAINT `mot_freq` FOREIGN KEY (`mot`) REFERENCES `word` (`id`) ON DELETE CASCADE,
  CONSTRAINT `theme_freq` FOREIGN KEY (`theme`) REFERENCES `themes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frequences`
--

LOCK TABLES `frequences` WRITE;
/*!40000 ALTER TABLE `frequences` DISABLE KEYS */;
INSERT INTO `frequences` VALUES (117,7,4),(232,7,1),(233,7,1),(234,7,1),(235,7,1),(141,7,6),(242,7,1),(243,7,3),(244,7,1),(245,7,1),(246,7,2),(132,7,9),(247,7,1),(180,7,6),(248,7,1),(249,7,1),(250,7,2),(251,7,1),(211,7,2),(252,7,1),(253,7,8),(119,7,4),(254,7,4),(201,7,5),(255,7,1),(256,7,1),(140,7,1),(167,7,1),(257,7,1),(190,7,1),(258,7,1),(259,7,1),(260,7,1),(178,7,1),(261,7,1),(188,7,1),(262,7,1),(263,7,1),(264,7,1),(265,7,1),(266,7,2),(194,7,1),(267,7,1),(208,7,1),(268,7,1),(269,7,1),(270,7,1),(271,7,1),(272,7,1),(273,7,1),(274,7,1),(191,7,1),(111,7,1),(275,7,2),(126,7,1),(276,7,1),(277,7,1),(278,7,1),(279,7,1),(280,7,1),(144,7,1),(281,7,1),(168,7,1),(282,7,1),(283,7,1),(146,7,1),(147,7,1),(284,7,1),(285,7,1),(286,7,1),(287,7,1),(288,7,1),(289,7,1),(225,7,1),(290,7,1),(291,7,1),(142,7,2),(292,7,1),(293,7,1),(294,7,1),(295,7,1),(296,7,2),(297,7,1),(157,7,1),(158,7,1),(298,7,1),(299,7,1),(300,7,1),(301,7,1),(302,7,1),(303,7,2),(304,7,1),(215,7,2),(305,7,1),(306,7,2),(307,7,2),(308,7,1),(309,7,1),(310,7,2),(311,7,2),(312,7,1),(171,7,1),(172,7,1),(313,7,1),(314,7,1),(134,7,1),(315,7,1),(213,7,1),(316,7,1),(317,7,1),(318,7,1),(214,7,2),(319,7,1),(320,7,1),(321,7,1),(322,7,1),(323,7,1),(121,6,12),(107,6,6),(122,6,6),(123,6,4),(324,6,2),(125,6,2),(126,6,2),(127,6,2),(325,6,2),(129,6,6),(326,6,2),(308,6,8),(132,6,18),(133,6,4),(134,6,6),(135,6,2),(136,6,4),(137,6,2),(112,6,2),(138,6,2),(139,6,2),(140,6,2),(141,6,4),(142,6,4),(143,6,2),(144,6,2),(145,6,2),(146,6,6),(147,6,2),(148,6,2),(149,6,2),(150,6,2),(151,6,2),(152,6,2),(153,6,2),(154,6,2),(155,6,4),(156,6,2),(157,6,2),(158,6,2),(159,6,2),(327,6,2),(161,6,2),(162,6,2),(163,6,2),(164,6,2),(165,6,4),(166,6,2),(167,6,10),(168,6,2),(169,6,2),(170,6,2),(171,6,2),(172,6,2),(173,6,2),(174,6,2),(175,6,4),(117,6,10),(176,6,2),(328,6,2),(178,6,8),(179,6,2),(180,6,6),(329,6,2),(182,6,2),(183,6,2),(184,6,2),(185,6,2),(186,6,2),(187,6,2),(188,6,2),(189,6,2),(190,6,2),(111,6,4),(191,6,2),(192,6,2),(193,6,2),(194,6,2),(195,6,2),(196,6,2),(197,6,2),(198,6,2),(330,6,2),(200,6,2),(201,6,2),(202,6,2),(203,6,4),(204,6,2),(205,6,2),(206,6,2),(207,6,4),(208,6,2),(209,6,2),(210,6,2),(211,6,4),(331,6,2),(213,6,2),(214,6,2),(215,6,2),(317,6,2),(217,6,2),(113,6,2),(218,6,2),(219,6,2),(220,6,2),(221,6,2),(332,6,2),(223,6,2),(224,6,2),(225,6,2),(226,6,2),(227,6,2),(106,15,26),(107,15,11),(108,15,11),(109,15,11),(110,15,11),(111,15,11),(112,15,22),(113,15,22),(114,15,11),(115,15,11),(116,15,22),(117,15,11),(118,15,11),(119,15,11),(120,15,11);
/*!40000 ALTER TABLE `frequences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intervals`
--

DROP TABLE IF EXISTS `intervals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intervals` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `bottom` float DEFAULT NULL,
  `top` float DEFAULT NULL,
  `mot` int(255) DEFAULT NULL,
  `theme` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `mot_ic` (`mot`),
  KEY `theme_ic` (`theme`),
  CONSTRAINT `mot_ic` FOREIGN KEY (`mot`) REFERENCES `word` (`id`) ON DELETE CASCADE,
  CONSTRAINT `theme_ic` FOREIGN KEY (`theme`) REFERENCES `themes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intervals`
--

LOCK TABLES `intervals` WRITE;
/*!40000 ALTER TABLE `intervals` DISABLE KEYS */;
INSERT INTO `intervals` VALUES (1,0.078102,0.166029,106,15),(2,0.021923,0.081364,107,15),(3,0.021923,0.081364,108,15),(4,0.021923,0.081364,109,15),(5,0.021923,0.081364,110,15),(6,0.021923,0.081364,111,15),(7,0.062415,0.144157,112,15),(8,0.062415,0.144157,113,15),(9,0.021923,0.081364,114,15),(10,0.021923,0.081364,115,15),(11,0.062415,0.144157,116,15),(12,0.021923,0.081364,117,15),(13,0.021923,0.081364,118,15),(14,0.021923,0.081364,119,15),(15,0.021923,0.081364,120,15);
/*!40000 ALTER TABLE `intervals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `plain`
--

DROP TABLE IF EXISTS `plain`;
/*!50001 DROP VIEW IF EXISTS `plain`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `plain` AS SELECT 
 1 AS `Mot`,
 1 AS `Nom`,
 1 AS `Freq`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `themes`
--

DROP TABLE IF EXISTS `themes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `themes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mot_freq` (`nom`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `themes`
--

LOCK TABLES `themes` WRITE;
/*!40000 ALTER TABLE `themes` DISABLE KEYS */;
INSERT INTO `themes` VALUES (7,'pardon'),(6,'rancoeur'),(15,'test');
/*!40000 ALTER TABLE `themes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `total`
--

DROP TABLE IF EXISTS `total`;
/*!50001 DROP VIEW IF EXISTS `total`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `total` AS SELECT 
 1 AS `Theme`,
 1 AS `n`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `word`
--

DROP TABLE IF EXISTS `word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `word` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mot` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mot` (`mot`)
) ENGINE=InnoDB AUTO_INCREMENT=333 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word`
--

LOCK TABLES `word` WRITE;
/*!40000 ALTER TABLE `word` DISABLE KEYS */;
INSERT INTO `word` VALUES (132,'a'),(309,'aim'),(288,'ainsi'),(285,'alorplus'),(144,'ans'),(312,'arrêter'),(258,'aucun'),(276,'aussi'),(195,'autant'),(315,'autr'),(165,'avec'),(161,'avoir'),(218,'bénéfiqu'),(235,'bibliqu'),(116,'bien'),(198,'c'),(120,'ca'),(272,'capacité'),(305,'car'),(125,'causé'),(106,'ceci'),(208,'cela'),(140,'celui'),(287,'cessent'),(119,'cest'),(176,'chrche'),(316,'clle'),(187,'complicité'),(271,'compréhension'),(232,'connaît'),(219,'convient'),(323,'coupl'),(184,'crcle'),(145,'csse'),(162,'cœur'),(324,'damrtume'),(134,'dan'),(220,'débarrasser'),(252,'décid'),(289,'denvenimer'),(174,'désagréabl'),(138,'difficil'),(264,'dindulgnce'),(326,'dinjutics'),(294,'dit'),(268,'dmande'),(325,'doffnes'),(329,'doffnse'),(278,'douleur'),(172,'dstructrice'),(214,'du'),(279,'dun'),(124,'d’amrtume'),(130,'d’injutics'),(128,'d’offnes'),(181,'d’offnse'),(270,'effort'),(260,'égard'),(223,'émotionnel'),(154,'empoisonnent'),(178,'en'),(314,'entrer'),(107,'est'),(180,'et'),(267,'facil'),(262,'fair'),(168,'fait'),(295,'faut'),(281,'fin'),(322,'fondement'),(190,'garder'),(189,'généralement'),(148,'grand'),(227,'harmoniuse'),(204,'hont'),(313,'hotilités'),(226,'hureuse'),(211,'il'),(151,'imaginair'),(244,'jéus'),(251,'jou'),(110,'just'),(300,'justement'),(155,'la'),(317,'lamour'),(250,'lautr'),(318,'lécout'),(234,'lépisod'),(332,'léquilibr'),(247,'linsult'),(152,'lle'),(328,'loffenser'),(275,'loffnse'),(213,'logiqu'),(310,'lon'),(293,'lorsqulle'),(163,'lourd'),(153,'lui'),(216,'l’amour'),(222,'l’équilibr'),(177,'l’offenser'),(265,'mai'),(115,'march'),(303,'mérit'),(158,'mond'),(261,'mot'),(209,'mpêche'),(320,'mutuel'),(254,'n'),(224,'nécssaire'),(123,'négatif'),(284,'nempoisonnent'),(330,'nen'),(266,'nest'),(298,'nimport'),(207,'notr'),(167,'nou'),(170,'ntraîne'),(183,'ntre'),(199,'n’en'),(257,'offensé'),(182,'offnse'),(117,'on'),(297,'or'),(129,'ou'),(201,'pa'),(126,'par'),(307,'parc'),(215,'pardon'),(306,'pardonn'),(253,'pardonner'),(136,'parfoi'),(200,'parl'),(175,'partnaire'),(147,'pasés'),(135,'passé'),(186,'perd'),(137,'pesant'),(205,'peur'),(166,'poid'),(291,'populair'),(111,'pour'),(217,'pourtant'),(248,'préfèr'),(273,'prndre'),(196,'problèm'),(114,'programm'),(302,'prsonne'),(263,'pruve'),(149,'ptite'),(243,'qu'),(299,'quand'),(327,'quest'),(141,'qui'),(308,'quon'),(286,'quotidien'),(160,'qu’est'),(131,'qu’on'),(242,'racont'),(121,'rancœur'),(143,'rapplle'),(283,'ras'),(301,'rconnaître'),(206,'réaction'),(304,'recevoir'),(210,'réconcilier'),(225,'relation'),(150,'rélle'),(173,'rendent'),(246,'répondr'),(319,'respect'),(259,'ressentiment'),(179,'retour'),(221,'retrouver'),(188,'revient'),(245,'rfuse'),(256,'rigueur'),(192,'rumin'),(280,'rumination'),(142,'s'),(290,'sagsse'),(159,'sait'),(296,'savoir'),(122,'sentiment'),(277,'séviter'),(113,'si'),(191,'soi'),(203,'soit'),(321,'sont'),(331,'soppos'),(193,'souffr'),(169,'souffrir'),(127,'souvenir'),(171,'spiral'),(202,'suffisamment'),(139,'supporter'),(274,'sur'),(212,'s’oppos'),(282,'tabl'),(255,'tenir'),(109,'test'),(249,'tndre'),(233,'tou'),(194,'toujour'),(157,'tout'),(292,'tromp'),(108,'txte'),(133,'ubis'),(118,'va'),(269,'véritabl'),(311,'veut'),(146,'vexation'),(156,'vi'),(185,'vicieux'),(197,'vient'),(164,'vivr'),(112,'voir');
/*!40000 ALTER TABLE `word` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'SIG'
--

--
-- Dumping routines for database 'SIG'
--

--
-- Final view structure for view `plain`
--

/*!50001 DROP VIEW IF EXISTS `plain`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`fukurou`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `plain` AS select `word`.`mot` AS `Mot`,`themes`.`nom` AS `Nom`,`frequences`.`frequence` AS `Freq` from ((`word` join `themes`) join `frequences`) where ((`frequences`.`mot` = `word`.`id`) and (`frequences`.`theme` = `themes`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `total`
--

/*!50001 DROP VIEW IF EXISTS `total`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`fukurou`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `total` AS select `themes`.`nom` AS `Theme`,sum(`frequences`.`frequence`) AS `n` from (`themes` join `frequences` on((`frequences`.`theme` = `themes`.`id`))) group by `frequences`.`theme` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-29 13:23:39
