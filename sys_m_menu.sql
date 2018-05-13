/*
Navicat MySQL Data Transfer

Source Server         : icg
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : iblog

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2018-05-13 23:52:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_m_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_m_menu`;
CREATE TABLE `sys_m_menu` (
  `menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_code` varchar(16) DEFAULT NULL,
  `menu_name_cn` varchar(100) DEFAULT NULL,
  `menu_name_en` varchar(100) DEFAULT NULL,
  `menu_url` varchar(150) DEFAULT NULL,
  `parent_code` varchar(16) DEFAULT NULL,
  `menu_icon_url` varchar(150) DEFAULT NULL,
  `menu_class` varchar(150) DEFAULT NULL,
  `menu_type` int(11) DEFAULT '0' COMMENT '0:main menu,1: sub menu',
  `menu_style` varchar(255) DEFAULT NULL,
  `menu_mark` varchar(25) DEFAULT NULL,
  `menu_config` text,
  `menu_tag` varchar(255) DEFAULT NULL,
  `menu_order_num` int(111) DEFAULT NULL COMMENT 'same level order number',
  `recommended` int(11) DEFAULT '0' COMMENT '0: not recommend 1:recommend',
  `fun_codes` varchar(300) DEFAULT NULL,
  `visible` int(11) DEFAULT '1' COMMENT '0:unvisible,1:visible',
  `remark` varchar(300) DEFAULT NULL,
  `auto_expire` int(11) DEFAULT NULL,
  `effective_time_interval` int(11) DEFAULT NULL,
  `last_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`menu_id`),
  UNIQUE KEY `idx_menu_code` (`menu_code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3760 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_m_menu
-- ----------------------------
INSERT INTO `sys_m_menu` VALUES ('3752', 'M01', '主页', 'home', '/home', null, null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3753', 'M02', '博客', 'blog', '#', null, null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3754', 'M0201', '学习', 'study', '/blog/study/', 'M02', null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3755', 'M0202', '随笔', 'essay', '/blog/essay/', 'M02', null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3756', 'M0203', '吐槽', 'kidding', '/blog/kidding/', 'M02', null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3757', 'M03', '个人简介', 'profile', '/profile/', '', null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3758', 'M04', '管理', 'admin', '/admin/', '', null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
INSERT INTO `sys_m_menu` VALUES ('3759', 'M05', '订阅', 'RSS', '/feed/main.xml/', '', null, null, '0', null, null, null, null, null, '0', null, '1', null, null, null, null);
