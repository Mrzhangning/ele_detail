CREATE TABLE `ele_detail` (
  `poi_id` int(15) NOT NULL,
  `poi_name` varchar(100) NOT NULL,
  `poi_status` tinyint(4) DEFAULT NULL,
  `poi_addr` varchar(100) DEFAULT NULL,
  `poi_phone` VARCHAR(100) DEFAULT  NULL,
  `poi_rating` float DEFAULT NULL,
  `poi_open_hours` VARCHAR(50) DEFAULT  NULL,
  `poi_rating_count` INT(11) DEFAULT  NULL,
  `ord_num_month` int(11) DEFAULT NULL,
  `min_delivery_price` float DEFAULT NULL,
  `shipping_fee` float DEFAULT NULL,
  `avg_speed` int(11) DEFAULT NULL,
  `poi_notice` varchar(4000) DEFAULT NULL,
  `poi_img` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`poi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


