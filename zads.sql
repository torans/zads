create database crawed;
use crawed;
CREATE TABLE `zreading` (
  `title` varchar(100) NOT NULL,
  `author` varchar(50) NOT NULL,
  `pub_date` varchar(30) DEFAULT NULL,
  `types` varchar(50) DEFAULT NULL,
  `tags` varchar(50) DEFAULT NULL,
  `view_counts` varchar(20) DEFAULT '0',
  `content` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;