/*
 Navicat Premium Data Transfer

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 29/03/2021 21:06:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for config
-- ----------------------------
DROP TABLE IF EXISTS `config`;
CREATE TABLE `config`  (
  `config_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `config_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `config_value` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`config_id`) USING BTREE,
  UNIQUE INDEX `config_name`(`config_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of config
-- ----------------------------
INSERT INTO `config` VALUES (1, 'Telegram_Bot_Token', '');
INSERT INTO `config` VALUES (2, 'Proxy', 'socks5://127.0.0.1:1080');

-- ----------------------------
-- Table structure for push
-- ----------------------------
DROP TABLE IF EXISTS `push`;
CREATE TABLE `push`  (
  `push_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '接收人ID',
  `push_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '接收人名称',
  `email_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '邮箱地址',
  `phone_number` char(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '手机号',
  `serverchan_key` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'ServerChande的KEY',
  `tg_chat_id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'Telegram Chat ID',
  PRIMARY KEY (`push_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of push
-- ----------------------------
INSERT INTO `push` VALUES (1, 'test', 'foo@bar.com', NULL, NULL, NULL);

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task`  (
  `task_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '任务ID',
  `task_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '任务名',
  `module_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '模块名',
  `enabled` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no' COMMENT '启用状态(no/yes)',
  `task_status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '任务状态',
  `last_run` datetime(6) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '任务最后运行时间',
  `latest_version` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '最新版本号',
  `release_date` datetime(6) NULL DEFAULT NULL COMMENT '更新日期',
  `push_to` int(10) NOT NULL DEFAULT 1 COMMENT '推送目标ID',
  `use_proxy` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT 'no' COMMENT '是否使用代理(no/yes)',
  PRIMARY KEY (`task_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task
-- ----------------------------
INSERT INTO `task` VALUES (1, 'AX86U官方固件', 'AX86U_official_firmware', 'yes', 'success', '2021-03-29 21:05:21.592231', '3.0.0.4.386.42095', '2021-03-18 00:00:00.000000', 1, 'no');
INSERT INTO `task` VALUES (2, 'AX86U官方源码', 'AX86U_official_sourcecode', 'no', 'error', '2021-03-29 21:05:22.264688', '3.0.0.4.384.9318', '2020-11-26 00:00:00.000000', 1, 'no');
INSERT INTO `task` VALUES (3, 'TrueNas Releases', 'TrueNas_releases', 'yes', 'success', '2021-03-29 21:05:33.283866', '202102231319', '2021-02-23 13:19:00.000000', 1, 'yes');
INSERT INTO `task` VALUES (4, '完美解码', 'Pure_codec', 'yes', 'success', '2021-03-29 21:05:24.797803', '20210320', '2021-03-20 00:00:00.000000', 1, 'no');
INSERT INTO `task` VALUES (6, 'AC86U koolshare固件', 'AC86U_koolshare_firmware', 'yes', 'success', '2021-03-29 21:05:26.489272', '386_40451', '2021-01-14 00:00:00.000000', 1, 'no');
INSERT INTO `task` VALUES (7, 'AX86U koolshare ML改版固件', 'AX86U_koolshare_merlin_firmware', 'yes', 'success', '2021-03-29 21:05:28.602786', '386_1_2', '2021-02-13 00:00:00.000000', 1, 'no');
INSERT INTO `task` VALUES (8, 'MikroTik SwitchOS', 'MikroTik_SwitchOS', 'yes', 'success', '2021-03-29 21:05:34.866171', '2.12', '2021-03-19 00:00:00.000000', 1, 'yes');

SET FOREIGN_KEY_CHECKS = 1;
