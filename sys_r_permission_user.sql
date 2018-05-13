/*
Navicat MySQL Data Transfer

Source Server         : icg
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : iblog

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2018-05-13 23:52:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_r_permission_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_r_permission_user`;
CREATE TABLE `sys_r_permission_user` (
  `user_name` varchar(50) NOT NULL DEFAULT '' COMMENT '用户名',
  `company_badge` varchar(50) DEFAULT NULL COMMENT '员工号',
  `user_role` text COMMENT '用户权限',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`user_name`),
  UNIQUE KEY `permission_user_name_index` (`user_name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_r_permission_user
-- ----------------------------
INSERT INTO `sys_r_permission_user` VALUES ('agrawalm', 'ManishAgrawal', 'fwr_team', '2016-10-24 16:37:49');
INSERT INTO `sys_r_permission_user` VALUES ('agrawalx', 'AshutoshXAgrawal', 'windows_team,fwv_team', '2016-10-25 01:25:43');
INSERT INTO `sys_r_permission_user` VALUES ('ajussila', 'AnnikkiJussila', 'windows_team,imaging_team', '2017-12-04 07:59:02');
INSERT INTO `sys_r_permission_user` VALUES ('akervine', 'akervineakervine', 'android_team', '2017-04-13 09:24:27');
INSERT INTO `sys_r_permission_user` VALUES ('arjunvex', 'ArjunVenugopal', 'fwr_team,fwv_team,anonymous', '2018-02-01 01:14:57');
INSERT INTO `sys_r_permission_user` VALUES ('ashustox', 'ashustoxashustox', 'windows_team,fwr_team,fwv_team', '2016-11-02 00:55:40');
INSERT INTO `sys_r_permission_user` VALUES ('atnaing', 'Aung TNaing', 'fwv_team', '2016-10-24 05:54:39');
INSERT INTO `sys_r_permission_user` VALUES ('bpuvvula', 'BhargavaPuvvula', 'sdk_team', '2016-10-18 09:00:40');
INSERT INTO `sys_r_permission_user` VALUES ('caolijix', 'LijiaX ACao', 'windows_team,linux_team,android_team,fwr_team,fwv_team,fwq_team,test_plan_group', '2017-11-20 05:40:26');
INSERT INTO `sys_r_permission_user` VALUES ('chuneuny', 'EmilyChun', 'windows_team,linux_team', '2016-11-03 04:22:00');
INSERT INTO `sys_r_permission_user` VALUES ('dmisra', 'DishaMisra', 'fwv_team', '2016-10-24 05:56:18');
INSERT INTO `sys_r_permission_user` VALUES ('enayak', 'ElloraNayak', 'windows_team,fwr_team,fwv_team', '2016-11-02 00:56:18');
INSERT INTO `sys_r_permission_user` VALUES ('ethenaff', 'ErwanLe Thenaff', 'imaging_team,anonymous,p2p', '2017-06-15 02:41:44');
INSERT INTO `sys_r_permission_user` VALUES ('evonckex', 'evonckexevonckex', 'sdk_team', '2016-10-21 06:33:40');
INSERT INTO `sys_r_permission_user` VALUES ('fanyang6', 'fanyang6fanyang6', 'android_team', '2016-12-01 02:18:30');
INSERT INTO `sys_r_permission_user` VALUES ('feifeizx', 'FeifeiXZhang', 'windows_team', '2017-12-25 06:07:02');
INSERT INTO `sys_r_permission_user` VALUES ('fengzhichao', 'ZhichaoXFeng', 'icgadmin', '2016-06-24 02:34:15');
INSERT INTO `sys_r_permission_user` VALUES ('gaoboxix', 'GaoboXXiao', 'icgadmin', '2018-02-14 05:10:10');
INSERT INTO `sys_r_permission_user` VALUES ('gaohongx', 'HongxiaXGao', 'android_team', '2017-05-11 08:24:42');
INSERT INTO `sys_r_permission_user` VALUES ('gengcaix', 'CaiyingXGeng', 'windows_team,fwr_team,test_plan_group,device_pit_group', '2017-12-18 07:42:03');
INSERT INTO `sys_r_permission_user` VALUES ('goudasx', 'SharanaXGouda', 'fwr_team,fwv_team', '2017-04-06 00:24:19');
INSERT INTO `sys_r_permission_user` VALUES ('guanxiux', 'XiujuanXGuan', 'linux_team', '2016-10-24 06:26:23');
INSERT INTO `sys_r_permission_user` VALUES ('haipingx', 'HaipingXYang', 'linux_team', '2017-11-10 03:07:12');
INSERT INTO `sys_r_permission_user` VALUES ('hcheng5x', 'HongxingXCheng', 'linux_team', '2017-03-24 08:06:17');
INSERT INTO `sys_r_permission_user` VALUES ('hzh111x', 'HuiXZhao', 'android_team', '2016-12-26 00:50:18');
INSERT INTO `sys_r_permission_user` VALUES ('jianme4x', 'JianmeiXBo', 'android_team', '2017-03-13 04:06:15');
INSERT INTO `sys_r_permission_user` VALUES ('jianwa1x', 'JianXWang', 'android_team', '2017-07-17 09:39:59');
INSERT INTO `sys_r_permission_user` VALUES ('jiminkix', 'JiminXKim', 'windows_team,linux_team', '2017-05-12 07:48:24');
INSERT INTO `sys_r_permission_user` VALUES ('jingwa5x', 'jingwa5xjingwa5x', 'windows_team', '2017-04-07 01:04:12');
INSERT INTO `sys_r_permission_user` VALUES ('jinjingx', 'jinjingxjinjingx', 'android_team', '2016-10-24 09:43:02');
INSERT INTO `sys_r_permission_user` VALUES ('jiyuanli', 'JiyuanLi', 'windows_team,linux_team,android_team', '2017-02-20 01:22:57');
INSERT INTO `sys_r_permission_user` VALUES ('jukkalau', 'JukkaLaukkanen', 'android_team,imaging_team', '2017-04-13 09:24:52');
INSERT INTO `sys_r_permission_user` VALUES ('junbiaox', 'JunbiaoXXu', 'windows_team', '2016-10-27 06:45:42');
INSERT INTO `sys_r_permission_user` VALUES ('kangxi1x', 'XinhongXKang', 'windows_team,linux_team,fwr_team', '2017-03-21 09:50:05');
INSERT INTO `sys_r_permission_user` VALUES ('kunhongx', 'KunhongXShen', 'windows_team', '2017-12-28 08:50:19');
INSERT INTO `sys_r_permission_user` VALUES ('lab_embt', 'lab_embt', 'windows_team,imaging_team', '2017-09-01 10:40:50');
INSERT INTO `sys_r_permission_user` VALUES ('lgeng1', 'RitaGeng', 'windows_team,linux_team,android_team,fwr_team,device_pit_group', '2017-12-12 03:34:24');
INSERT INTO `sys_r_permission_user` VALUES ('lijing2', 'Jing ALi', 'windows_team,linux_team,android_team,milestone_admin', '2018-01-03 05:22:44');
INSERT INTO `sys_r_permission_user` VALUES ('liliyuax', 'LiliXYuan', 'android_team', '2017-03-13 04:05:47');
INSERT INTO `sys_r_permission_user` VALUES ('linyefex', 'YefeiXLin', 'windows_team,linux_team', '2017-04-13 09:16:55');
INSERT INTO `sys_r_permission_user` VALUES ('lipingxx', 'lipingxxlipingxx', 'android_team', '2016-10-24 09:36:48');
INSERT INTO `sys_r_permission_user` VALUES ('liqifux', 'QifuXLi', 'windows_team', '2018-01-09 10:32:12');
INSERT INTO `sys_r_permission_user` VALUES ('liqiongw', 'liqiongwliqiongw', 'android_team', '2016-10-24 09:46:11');
INSERT INTO `sys_r_permission_user` VALUES ('lishua1x', 'ShuangXLi', 'windows_team', '2017-04-13 09:17:36');
INSERT INTO `sys_r_permission_user` VALUES ('liufen3x', 'FengXLiu', 'android_team,anonymous,test_plan_group,device_pit_group', '2018-01-24 08:03:32');
INSERT INTO `sys_r_permission_user` VALUES ('liuweizx', 'WeizhenXLiu', 'windows_team', '2017-12-28 08:50:05');
INSERT INTO `sys_r_permission_user` VALUES ('liuyin1x', 'YingjieXLiu', 'windows_team,android_team', '2017-12-05 05:42:05');
INSERT INTO `sys_r_permission_user` VALUES ('liyingax', 'liyingaxliyingax', 'windows_team,anonymous', '2018-02-09 06:59:17');
INSERT INTO `sys_r_permission_user` VALUES ('liyingyx', 'LiyingXYu', 'android_team', '2018-01-09 10:32:42');
INSERT INTO `sys_r_permission_user` VALUES ('lkanx', 'LiXKan', 'windows_team,linux_team,fwr_team', '2017-12-11 05:25:24');
INSERT INTO `sys_r_permission_user` VALUES ('lmoisio', 'LauraMoisio', 'windows_team,imaging_team', '2017-11-06 08:16:12');
INSERT INTO `sys_r_permission_user` VALUES ('lyue', 'lingyue', 'windows_team', '2016-10-26 09:18:05');
INSERT INTO `sys_r_permission_user` VALUES ('mamattil', 'Mikko AMattila', 'android_team,imaging_team,anonymous,test_plan_group,device_pit_group', '2018-02-01 09:11:58');
INSERT INTO `sys_r_permission_user` VALUES ('mengweix', 'WeiXMeng', 'linux_team,android_team,test_plan_group,device_pit_group', '2017-12-12 03:44:39');
INSERT INTO `sys_r_permission_user` VALUES ('mgotefox', 'ManishXGotefode', 'fwv_team', '2016-10-24 05:55:08');
INSERT INTO `sys_r_permission_user` VALUES ('mharkone', 'MaaritHarkonen', 'android_team,imaging_team', '2017-04-13 09:24:03');
INSERT INTO `sys_r_permission_user` VALUES ('mingluwx', 'MingluXWang', 'windows_team,linux_team,android_team,milestone_admin', '2017-12-11 09:13:58');
INSERT INTO `sys_r_permission_user` VALUES ('naveenjx', 'NaveenXJain', 'fwv_team', '2016-10-24 05:56:28');
INSERT INTO `sys_r_permission_user` VALUES ('nawaznx', 'NawazN', 'fwr_team,fwv_team,anonymous', '2018-02-01 01:14:34');
INSERT INTO `sys_r_permission_user` VALUES ('nwanx', 'NingXWan', 'windows_team', '2018-01-10 06:24:35');
INSERT INTO `sys_r_permission_user` VALUES ('nyang1', 'ningjianyang', 'windows_team,linux_team,android_team,fwr_team,fwv_team,imaging_team,sdk_team', '2016-12-02 06:22:17');
INSERT INTO `sys_r_permission_user` VALUES ('pasokanx', 'PartheebanXAsokan', 'fwr_team,fwv_team', '2016-10-27 05:34:30');
INSERT INTO `sys_r_permission_user` VALUES ('pbobdex', 'PankajXBobde', 'fwr_team', '2016-10-24 16:33:33');
INSERT INTO `sys_r_permission_user` VALUES ('pingyan1', 'pingyan1pingyan1', 'android_team', '2016-10-24 09:37:24');
INSERT INTO `sys_r_permission_user` VALUES ('pjiax', 'PeixiangXJia', 'windows_team,linux_team', '2017-07-20 05:50:41');
INSERT INTO `sys_r_permission_user` VALUES ('pmallirx', 'pmallirxpmallirx', 'fwv_team', '2016-10-24 05:54:55');
INSERT INTO `sys_r_permission_user` VALUES ('psule', 'psulepsule', 'fwv_team', '2016-10-24 05:55:50');
INSERT INTO `sys_r_permission_user` VALUES ('qduanx', 'QiujuXDuan', 'android_team,test_plan_group,device_pit_group', '2017-12-12 03:41:28');
INSERT INTO `sys_r_permission_user` VALUES ('qhan2', 'qhan2qhan2', 'android_team', '2016-10-24 09:44:48');
INSERT INTO `sys_r_permission_user` VALUES ('qianhu2x', 'QianXHuang', 'windows_team', '2018-01-08 03:40:11');
INSERT INTO `sys_r_permission_user` VALUES ('rakeshkj', 'rakeshkjrakeshkj', 'fwv_team', '2016-10-24 05:56:08');
INSERT INTO `sys_r_permission_user` VALUES ('rantingx', 'TingtingXRan', 'windows_team,linux_team', '2017-12-15 02:16:12');
INSERT INTO `sys_r_permission_user` VALUES ('rheuts', 'rheutsrheuts', 'sdk_team', '2016-10-21 06:32:38');
INSERT INTO `sys_r_permission_user` VALUES ('ruihongx', 'RuihongXLiu', 'windows_team', '2016-10-27 06:45:26');
INSERT INTO `sys_r_permission_user` VALUES ('rwangx', 'RuiXWang', 'android_team', '2016-10-24 09:36:15');
INSERT INTO `sys_r_permission_user` VALUES ('sambathx', 'SambathkumarXChandrasekaran', 'fwr_team', '2016-10-24 13:49:52');
INSERT INTO `sys_r_permission_user` VALUES ('shan3', 'ShupingHan', 'icgadmin,windows_team,linux_team,android_team,fwr_team,fwv_team,fwq_team,imaging_team,anonymous,sdk_team,test_plan_group,milestone_admin,device_pit_group', '2018-02-12 11:22:14');
INSERT INTO `sys_r_permission_user` VALUES ('shuminyx', 'ShuminXYi', 'android_team', '2016-10-24 09:37:46');
INSERT INTO `sys_r_permission_user` VALUES ('shuping.han', 'ShupingHan', 'icgadmin', '2016-04-27 07:52:38');
INSERT INTO `sys_r_permission_user` VALUES ('siweifex', 'SiweiXFeng', 'android_team', '2017-03-13 04:05:31');
INSERT INTO `sys_r_permission_user` VALUES ('sunjua1x', 'JuanjuanXSun', 'windows_team,linux_team', '2017-06-08 08:09:49');
INSERT INTO `sys_r_permission_user` VALUES ('sunlingx', 'LingX ASun', 'windows_team,android_team,device_pit_group', '2017-12-12 03:43:57');
INSERT INTO `sys_r_permission_user` VALUES ('sys_camsw', 'sys_camsw', 'icgadmin,windows_team,linux_team,android_team', '2017-08-18 07:51:08');
INSERT INTO `sys_r_permission_user` VALUES ('tingwanx', 'TingXWang', 'windows_team,fwr_team', '2018-01-08 03:39:40');
INSERT INTO `sys_r_permission_user` VALUES ('tsriniv', 'ThyagarajanSrinivasan', 'milestone_admin', '2018-01-03 05:23:25');
INSERT INTO `sys_r_permission_user` VALUES ('vkunnari', 'MikaKunnari', 'milestone_admin', '2018-01-03 05:23:13');
INSERT INTO `sys_r_permission_user` VALUES ('weij1x', 'weij1xweij1x', 'windows_team', '2017-12-21 01:50:00');
INSERT INTO `sys_r_permission_user` VALUES ('weilianx', 'LiangXWei', 'windows_team', '2018-01-09 10:33:05');
INSERT INTO `sys_r_permission_user` VALUES ('weizx', 'ZhenxiangXWei', 'windows_team', '2016-10-14 03:37:18');
INSERT INTO `sys_r_permission_user` VALUES ('wenjielx', 'WenjieX ALi', 'linux_team', '2017-10-20 05:40:15');
INSERT INTO `sys_r_permission_user` VALUES ('wjiang2x', 'WeiXJiang', 'linux_team', '2016-11-09 08:05:25');
INSERT INTO `sys_r_permission_user` VALUES ('wli58', 'Wei LLi', 'windows_team,linux_team,anonymous', '2018-02-01 05:37:22');
INSERT INTO `sys_r_permission_user` VALUES ('xchen85', 'Xi CChen', 'icg_dashboard_write,windows_team', '2016-10-14 03:35:36');
INSERT INTO `sys_r_permission_user` VALUES ('xgu17', 'XueyingGu', 'icgadmin,windows_team,linux_team', '2017-08-03 04:50:32');
INSERT INTO `sys_r_permission_user` VALUES ('xiangfax', 'xiangfaxxiangfax', 'windows_team', '2016-10-27 06:46:13');
INSERT INTO `sys_r_permission_user` VALUES ('xiaoshux', 'XiaoshuangXGuo', 'android_team', '2016-10-24 09:28:57');
INSERT INTO `sys_r_permission_user` VALUES ('xinche1x', 'XinXChen', 'windows_team', '2016-10-27 06:45:58');
INSERT INTO `sys_r_permission_user` VALUES ('xingbaox', 'XingbaoXWang', 'windows_team,linux_team,android_team,fwr_team,imaging_team,test_plan_group,device_pit_group', '2017-12-22 03:05:10');
INSERT INTO `sys_r_permission_user` VALUES ('xinlinmx', 'XinlinXMa', 'icgadmin,anonymous', '2018-01-19 03:49:28');
INSERT INTO `sys_r_permission_user` VALUES ('xuemeihx', 'XuemeiXHuang', 'linux_team', '2016-10-24 06:26:50');
INSERT INTO `sys_r_permission_user` VALUES ('yamano', 'YigalAmano', 'p2p', '2017-06-15 02:57:56');
INSERT INTO `sys_r_permission_user` VALUES ('yanchaog', 'YanchaoGong', 'windows_team,linux_team', '2017-02-15 05:38:08');
INSERT INTO `sys_r_permission_user` VALUES ('ydomoshn', 'ydomoshnydomoshn', 'p2p', '2017-06-15 03:05:19');
INSERT INTO `sys_r_permission_user` VALUES ('yhuang1x', 'YufangXHuang', 'windows_team', '2016-10-24 05:47:39');
INSERT INTO `sys_r_permission_user` VALUES ('youfazhx', 'YoufaXZhang', 'linux_team', '2016-10-24 04:19:09');
INSERT INTO `sys_r_permission_user` VALUES ('yuboli', 'YuboLi', 'icgadmin,windows_team', '2016-10-26 05:46:21');
INSERT INTO `sys_r_permission_user` VALUES ('yueshix', 'YueXShi', 'windows_team', '2016-11-11 09:50:09');
INSERT INTO `sys_r_permission_user` VALUES ('yunlong.hou', 'YunlongHuo', 'icgadmin', '2016-05-27 08:33:58');
INSERT INTO `sys_r_permission_user` VALUES ('yunlongh', 'YunlongHou', 'windows_team', '2017-06-06 11:10:05');
INSERT INTO `sys_r_permission_user` VALUES ('yuzha15x', 'yuzha15xyuzha15x', 'android_team', '2017-05-11 08:24:59');
INSERT INTO `sys_r_permission_user` VALUES ('zfen12x', 'ZhichaoXFeng', 'icgadmin,anonymous', '2016-11-07 06:08:43');
INSERT INTO `sys_r_permission_user` VALUES ('zhanlinx', 'zhanlinxzhanlinx', 'android_team', '2016-10-24 09:45:12');
INSERT INTO `sys_r_permission_user` VALUES ('zhichaofex', 'ZhichaoXFeng', 'icgadmin', '2016-05-27 08:33:37');
INSERT INTO `sys_r_permission_user` VALUES ('zhouha3x', 'HaiyanXZhou', 'windows_team', '2017-12-28 08:49:46');
INSERT INTO `sys_r_permission_user` VALUES ('zhoutiax', 'zhoutiaxzhoutiax', 'windows_team,anonymous', '2018-03-06 07:04:31');
INSERT INTO `sys_r_permission_user` VALUES ('zhugaofx', 'GaofengXZhu', 'windows_team,linux_team,android_team,anonymous', '2018-02-09 02:33:31');
INSERT INTO `sys_r_permission_user` VALUES ('zhujessx', 'WenjinXZhu', 'linux_team', '2017-03-24 08:06:01');
INSERT INTO `sys_r_permission_user` VALUES ('ziping', '', 'icgadmin,windows_team,linux_team,android_team,fwr_team,fwv_team,fwq_team,imaging_team,anonymous,sdk_team,p2p,test_plan_group,milestone_admin,device_pit_group', '2018-03-09 15:49:46');
INSERT INTO `sys_r_permission_user` VALUES ('zipinglx', 'ZipingXLv', 'icgadmin', '2018-03-01 07:59:37');
