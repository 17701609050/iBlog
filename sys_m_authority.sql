/*
Navicat MySQL Data Transfer

Source Server         : icg
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : iblog

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2018-05-13 23:52:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_m_authority
-- ----------------------------
DROP TABLE IF EXISTS `sys_m_authority`;
CREATE TABLE `sys_m_authority` (
  `role_code` varchar(16) NOT NULL,
  `menu_code` varchar(16) NOT NULL,
  `fun_codes` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`menu_code`,`role_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_m_authority
-- ----------------------------
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M01', ' ');
INSERT INTO `sys_m_authority` VALUES ('R0020', 'M01', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M02', null);
INSERT INTO `sys_m_authority` VALUES ('R0020', 'M02', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M0201', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M0202', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M0203', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M03', null);
INSERT INTO `sys_m_authority` VALUES ('R0020', 'M03', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M04', null);
INSERT INTO `sys_m_authority` VALUES ('R0001', 'M05', null);
