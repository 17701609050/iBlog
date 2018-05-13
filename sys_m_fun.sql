/*
Navicat MySQL Data Transfer

Source Server         : icg
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : iblog

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2018-05-13 23:52:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_m_fun
-- ----------------------------
DROP TABLE IF EXISTS `sys_m_fun`;
CREATE TABLE `sys_m_fun` (
  `fun_id` int(11) NOT NULL AUTO_INCREMENT,
  `fun_code` varchar(16) DEFAULT NULL,
  `fun_name_cn` varchar(100) DEFAULT NULL,
  `fun_name_en` varchar(100) DEFAULT NULL,
  `fun_icon_url` varchar(150) DEFAULT NULL,
  `html_id` varchar(100) DEFAULT NULL,
  `fun_class` varchar(150) DEFAULT NULL,
  `remark` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`fun_id`),
  KEY `idx_fun_code` (`fun_code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_m_fun
-- ----------------------------
INSERT INTO `sys_m_fun` VALUES ('1', 'F0001', '新建', 'New', 'icon-pencil', '_btn_sys_fun_new', 'satblue', ' ');
INSERT INTO `sys_m_fun` VALUES ('2', 'F0002', '编辑', 'Edit', 'icon-edit', '_btn_sys_fun_edit', 'satgreen', ' ');
INSERT INTO `sys_m_fun` VALUES ('3', 'F0004', '删除', 'Delete', 'icon-trash', '_btn_sys_fun_delete', 'lightgrey', '物理删除');
INSERT INTO `sys_m_fun` VALUES ('4', 'F0005', '删除', 'Delete', 'icon-remove', '_btn_sys_fun_disable', 'button danger', '逻辑删除');
INSERT INTO `sys_m_fun` VALUES ('5', 'F0010', '高级检索', 'Advanced Search', 'icon-search', '_btn_sys_fun_search', 'teal', ' ');
INSERT INTO `sys_m_fun` VALUES ('6', 'F0012', '数据导出', 'Export', 'icon-share', '_btn_sys_fun_export', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('7', 'F0011', '数据导入', 'Import', 'icon-upload', '_btn_sys_fun_import', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('8', 'F0003', '预览', 'Preview', 'icon-remove', '_btn_sys_fun_preview', 'button success', ' ');
INSERT INTO `sys_m_fun` VALUES ('9', 'F0013', '下载', 'Download', 'icon-download-alt', '_btn_sys_fun_download', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('10', 'F0014', '复制', 'Copy', 'icon-copy', '_btn_sys_fun_copy', 'blue', ' ');
INSERT INTO `sys_m_fun` VALUES ('11', 'F0015', '粘贴', 'Paste', 'icon-edit', '_btn_sys_fun_paste', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('12', 'F0016', '创建', 'Create', 'icon-edit', '_btn_sys_fun_create', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('13', 'F0017', '更新', 'Update', 'icon-edit', '_btn_sys_fun_update', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('14', 'F0018', '日志', 'Log', 'icon-edit', '_btn_sys_fun_log', ' ', ' ');
INSERT INTO `sys_m_fun` VALUES ('15', 'F0100', 'Select Report', 'Select Report', 'icon-calendar', '_btn_sys_fun_select_guid', 'blue', ' ');
INSERT INTO `sys_m_fun` VALUES ('16', 'F0101', 'Edit Report', 'Edit Report', 'icon-edit', '_btn_sys_fun_edit_report', 'satgreen', ' ');
INSERT INTO `sys_m_fun` VALUES ('17', 'F0102', 'Send Report', 'Send Report', 'icon-envelope', '_btn_sys_fun_send_report', 'teal', ' ');
INSERT INTO `sys_m_fun` VALUES ('18', 'F0107', 'Export Report', 'Export Report', 'icon-share', '_btn_sys_fun_export_report', 'satgreen', '');
INSERT INTO `sys_m_fun` VALUES ('19', 'F0105', 'Subscribe', 'Subscribe', 'icon-rss', '_btn_sys_fun_subscribe', 'orange', ' ');
INSERT INTO `sys_m_fun` VALUES ('20', 'F0104', 'Data Upload', 'Data Upload', 'icon-cloud-upload', '_btn_sys_fun_excel_upload', 'satgreen', ' ');
INSERT INTO `sys_m_fun` VALUES ('21', 'F0020', 'Save', 'Save', 'icon-save', '_btn_sys_fun_save', 'blue', '');
INSERT INTO `sys_m_fun` VALUES ('22', 'F0019', 'Add', 'Add', 'icon-plus', '_btn_sys_fun_add', 'orange', ' ');
INSERT INTO `sys_m_fun` VALUES ('23', 'F0106', '高级操作', 'Advanced Operation', 'icon-wrench', '_btn_sys_fun_operation', 'red', ' ');
INSERT INTO `sys_m_fun` VALUES ('24', 'F0201', 'Download Template', 'Download Template', 'icon-cloud-download', '_btn_sys_fun_download_template', 'satgreen', ' ');
INSERT INTO `sys_m_fun` VALUES ('25', 'F0202', 'Ping', 'Ping', 'icon-exchange', '_btn_sys_fun_ping', 'brown', ' ');
INSERT INTO `sys_m_fun` VALUES ('26', 'F0210', 'Template Download', 'Template Download', 'icon-book', '_btn_sys_fun_template', 'orange', '');
INSERT INTO `sys_m_fun` VALUES ('27', 'F0103', 'Report Upload', 'Report Upload', 'icon-upload-alt', '_btn_sys_fun_validation_report_upload', 'darkblue', '');
INSERT INTO `sys_m_fun` VALUES ('28', 'F0205', 'Nightly build w/ Patches ', 'Nightly build w/ Patches ', 'icon-external-link', '_btn_sys_fun_view_patch', 'satgreen', '');
INSERT INTO `sys_m_fun` VALUES ('29', 'F0108', 'PnP Report Edit', 'PnP Report Edit', 'icon-edit', '_btn_sys_fun_pnp_edit_report', 'satgreen', '');
INSERT INTO `sys_m_fun` VALUES ('30', 'F0030', 'Sort', 'Sort', 'icon-sort', '_btn_sys_fun_sort', 'brown', '');
INSERT INTO `sys_m_fun` VALUES ('31', 'F0212', 'New Version Link', 'New Version Link', 'icon-link', '_btn_sys_fun_link', 'orange', '');
