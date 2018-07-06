/*
Navicat MySQL Data Transfer

Source Server         : icg
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : iblog

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2018-05-13 23:52:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_m_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_m_role`;
CREATE TABLE `sys_m_role` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_code` varchar(16) DEFAULT NULL,
  `role_name_cn` varchar(100) DEFAULT NULL,
  `role_name_en` varchar(100) DEFAULT NULL,
  `role_icon_url` varchar(150) DEFAULT NULL,
  `role_class` varchar(150) DEFAULT NULL,
  `interface_name` varchar(150) DEFAULT NULL,
  `remark` longtext,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_m_role
-- ----------------------------
INSERT INTO `sys_m_role` VALUES ('1', 'R0001', 'Super Admin', 'Super Admin', ' ', ' ', 'icgadmin', '{}');
INSERT INTO `sys_m_role` VALUES ('2', 'R0020', 'Anonymous', 'Anonymous', ' ', ' ', 'anonymous', '{\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('3', 'R0013', 'Windows Team', 'Windows Team', ' ', ' ', 'windows_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0108,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0105,F0108,F0205\",\"/project_status/customer_tpt/windows/\":\"F0100,F0020\",\"/project_status/customer_tpt/android/\":\"F0100\",\"/project_status/customer_tpt/linux/\":\"F0100\",\"(.+)-WIN\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('4', 'R0014', 'Linux Team', 'Linux Team', ' ', ' ', 'linux_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0105,F0205\",\"/project_status/customer_tpt/windows/\":\"F0100\",\"/project_status/customer_tpt/android/\":\"F0100\",\"/project_status/customer_tpt/linux/\":\"F0100,F0020\",\"(.+)-Linux\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('5', 'R0015', 'Android Team', 'Android Team', ' ', ' ', 'android_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0205\",\"/validation/(.+)\\\\?platform=IPU3-KBL-Chrome&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0205\",\"/validation/(.+)\\\\?platform=IPU5-GLV_A-FWR&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0105,F0205\",\"/project_status/customer_tpt/windows/\":\"F0100,F0020\",\"/project_status/customer_tpt/android/\":\"F0100,F0020, F0103,F0105,F0205\",\"/project_status/customer_tpt/linux/\":\"F0100\",\"(.+)-Android\":\"\",\"(.+)-Chrome\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('6', 'R0016', 'FWR Team', 'FWR Team', ' ', ' ', 'fwr_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0105,F0205\",\"(.+)-FWR\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('7', 'R0017', 'FWV Team', 'FWV Team', ' ', ' ', 'fwv_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0101,F0102,F0103,F0104,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0205\",\"(.+)-FWV\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('8', 'R0018', 'FWQ Team', 'FWQ Team', ' ', ' ', 'fwq_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0101,F0102,F0103,F0104,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0205\",\"(.+)-FWQ\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('9', 'R0019', 'Imaging Team', 'Imaging Team', ' ', ' ', 'imaging_team', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0101,F0102,F0103,F0104,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0101,F0102,F0103,F0104,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0205\",\"ImagingTools\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('10', 'R0021', 'SDK Team', 'SDK Team', ' ', ' ', 'sdk_team', '{\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0101,F0102,F0103,F0104,F0205\",\"/project_status/customer_tpt/windows/\":\"F0100,F0020\",\"/project_status/customer_tpt/android/\":\"F0100\",\"/project_status/customer_tpt/linux/\":\"F0100\",\"SDK\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('11', 'R0022', 'P2P', 'P2P', ' ', ' ', 'p2p', '{\"P2P\":\"\",\"IPU6\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('12', 'R0023', 'Windows Team', 'Test Plan Group', ' ', ' ', 'test_plan_group', '{\"/validation/(.+)\\\\?platform=(.+)&sub_platform=IMAGING-\":\"F0100,F0102,F0103,F0205\",\"/validation/(.+)\\\\?platform=(.+)-WIN&\":\"F0100,F0101,F0102,F0103,F0104,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Linux&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-Android&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWQ&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWV&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=(.+)-FWR&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=IQStudio&\":\"F0100,F0102,F0103,F0105,F0205\",\"/validation/(.+)\\\\?platform=SDK&\":\"F0100,F0102,F0103,F0105,F0205\",\"/project_status/customer_tpt/windows/\":\"F0100,F0020\",\"/project_status/customer_tpt/android/\":\"F0100\",\"/project_status/customer_tpt/linux/\":\"F0100\",\"(.+)-WIN\":\"\",\"TestPlatform\":\"\"}');
INSERT INTO `sys_m_role` VALUES ('13', 'R0024', ' ', 'Milestone Admin', ' ', ' ', 'milestone_admin', '{}');
INSERT INTO `sys_m_role` VALUES ('14', 'R0025', 'Anonymous', 'Device PIT Group', ' ', ' ', 'device_pit_group', '{\"TestPlatform\":\"\"}');