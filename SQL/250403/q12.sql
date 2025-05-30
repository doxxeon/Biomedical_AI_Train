-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.5.5-10.11.6-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int(8) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `publication_year` year(4) NOT NULL,
  `price` decimal(65,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



LOCK TABLES `books` WRITE;

INSERT INTO `books` VALUES (1,'Flames of Destiny','Zeus Hill',2021,122.00),(2,'Beyond the Horizon','Inez Bowen',2017,209.00),(3,'Hidden Shadows','Prescott Dotson',2002,107.00),(4,'The Secret Echo','Renee Shields',2018,243.00),(5,'Beneath Frozen Stars','Thane Bernard',2001,120.00),(6,'The Breaking Dawn','Wesley Boone',2024,45.00),(7,'Whispers of the Old City','Herman Ball',2011,158.00),(8,'The Last Promise','Mannix Chavez',2014,134.00),(9,'Silent Vengeance','Tamekah Carrillo',2005,246.00),(10,'Bound by Blood','Molly Leon',2024,63.00),(11,'Dance of the Dragons','Martin Mcbride',2024,135.00),(12,'Oceans of Magic','Louis Vinson',2019,285.00),(13,'Twisted Trust','Tara Underwood',2016,263.00),(14,'Vanishing Voices','Lani Velazquez',2021,204.00),(15,'The Midnight Secret','Elvis Noel',2009,271.00),(16,'The Forbidden Temple','Arthur Merritt',2005,111.00),(17,'Crimson Tides','Samson Yates',2011,291.00),(18,'Memories of the Forgotten','Gage Mooney',2003,247.00),(19,'The Mysterious Intruder','Fredericka Middleton',2018,294.00),(20,'Hollow Hearts','Dara Kerr',2022,55.00),(21,'Steps in the Dark','Jorden Bruce',2019,149.00),(22,'The Whispering Pines','Delilah Johnson',2010,44.00),(23,'Shattered Dreams','Kameko Mcdaniel',2009,239.00),(24,'The Glass Castle','Abel Mayer',2006,292.00),(25,'Wandering Souls','Amena Banks',2014,60.00),(26,'The Butterfly Effect','Michelle Davenport',2020,62.00),(27,'Wings of Despair','Zane Mccoy',2018,279.00),(28,'The Silver Lining','Edan Coffey',2013,47.00),(29,'To the Lifeline','Jillian Garza',2021,39.00),(30,'The Lost Key','Philip Combs',2019,50.00),(31,'Enchanted Island','Lacy Bean',2012,25.00),(32,'The Timeless Voyage','Beverly Schroeder',2022,60.00),(33,'Hidden Treasures','Odessa Ayala',2004,74.00),(34,'The Edge of Tomorrow','Teegan Huber',2015,142.00),(35,'Wars of the Underworld','Alden Leon',2023,148.00),(36,'The Last Symphony','Wesley Joseph',2004,248.00),(37,'The Final Element','Molly Pratt',2019,95.00),(38,'Echoes of the Abyss','Griffith Marsh',2021,34.00),(39,'The Timeless Clock','Suki Charles',2020,290.00),(40,'The Phantom\'s Shadow','Perry Anderson',2014,73.00),(41,'Lost in Translation','Ariana Rice',2003,32.00),(42,'The Sapphire Tear','Aimee Raymond',2016,76.00),(43,'A Thread of Hope','John Clay',2006,139.00),(44,'Forgotten Memories','Zena Strong',2014,88.00),(45,'The Broken Arrow','Chester Ramos',2015,12.00),(46,'The Emerald Eye','Aquila Sanders',2006,148.00),(47,'Veiled Truths','Upton Hicks',2002,31.00),(48,'The Phoenix Ascending','Jasper Morse',2017,242.00),(49,'Shadows of the Past','Ira Lowery',2013,94.00),(50,'Strangers at Dawn','Barbara Fleming',2006,242.00),(51,'The Diamond Deception','Gretchen Salinas',2019,132.00),(52,'The Winter Queen','Genevieve Meadows',2012,69.00),(53,'From Dust to Dawn','Boris Walter',2003,188.00),(54,'The Lost Prophecy','Audra Phelps',2013,114.00),(55,'Secrets of the Sand','Karleigh Mcdonald',2003,41.00),(56,'Tempest\'s Fury','Claire Willis',2004,299.00),(57,'The Indigo Inferno','Price Howell',2005,78.00),(58,'Fallen Angels','Kiayada Bray',2014,281.00),(59,'The King\'s Heir','Miranda Alvarez',2014,18.00),(60,'The Rusted Heart','Vera Hendrix',2020,210.00),(61,'The Hidden Gem','Chadwick Dominguez',2023,150.00),(62,'Celestial Awakenings','Karina Walls',2015,78.00),(63,'Darkness Falls','Briar Mcintyre',2019,292.00),(64,'Revival of the Fittest','Beau Mckenzie',2013,16.00),(65,'The Sapphire Star','Martha Gaines',2002,189.00),(66,'Into the Enchanted Forest','Bree Woodward',2009,125.00),(67,'The Quintessence Quandary','Ashely Murray',2010,137.00),(68,'Dance with Destiny','Edan Cotton',2006,76.00),(69,'The Spellbound Prince','Shad Mejia',2012,11.00),(70,'The Journey in the Dark','Eagan Padilla',2022,125.00),(71,'The Ember\'s Glow','Eagan Sawyer',2010,191.00),(72,'The Broken Mirror','Dahlia Watkins',2020,294.00),(73,'The Emerald Kingdom','Tara Gonzales',2017,92.00),(74,'Moonlit Secrets','Devin Zamora',2009,183.00),(75,'A Shot In The Dark','Prescott Zimmerman',2017,112.00),(76,'The Price of Freedom','Felicia Winters',2011,19.00),(77,'Through the Mirrored Gate','Ann Parker',2008,281.00),(78,'Haunting Whispers','Deirdre Atkinson',2013,206.00),(79,'Wanderer\'s Forest','Jennifer Coleman',2002,265.00),(80,'Threads of Fate','Zane Suarez',2009,201.00),(81,'The Last Whisper','Quamar Chambers',2022,298.00),(82,'Dances with Shadows','Shea Andrews',2013,154.00),(83,'The Haunting of the Lost','Daniel Frazier',2006,299.00),(84,'Bound by Fate','Wesley Bradshaw',2008,132.00),(85,'The Stolen Throne','Wade Chang',2005,190.00),(86,'Midnight\'s Fever','Jameson Mejia',2021,56.00),(87,'Ignite the Shadows','Isaiah Jackson',2011,137.00),(88,'The Void\'s Edge','Kristen Dillon',2016,76.00),(89,'The Crystal Shard','Halla O\'donnell',2007,95.00),(90,'The Eternity Key','Imani Snow',2015,37.00),(91,'Shadowed Corridors','Violet Wagner',2010,159.00),(92,'The Last Ember','David Rogers',2013,137.00),(93,'Infinity\'s End','Nasim Mcguire',2012,173.00),(94,'Shadows in the Snow','Zoe Barrett',2014,284.00),(95,'Taboo Truths','Dorian Harding',2016,58.00),(96,'Whispers from the Ashes','Naida Strong',2022,44.00),(97,'Beneath the Wandering Stars','Ifeoma Farrell',2022,223.00),(98,'The Flame\'s Promise','Ryder Emerson',2005,236.00),(99,'The Crimson Cross','Daphne Lewis',2024,40.00),(100,'The Pearl of Peril','Gavin Moss',2024,133.00);

UNLOCK TABLES;
SELECT MAX(price), MIN(price) FROM book WHERE publication_year BETWEEN 2001 AND 2003;