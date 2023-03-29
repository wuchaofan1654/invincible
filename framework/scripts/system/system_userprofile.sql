-- ----------------------------
-- 用户管理 初始化sql
-- Table structure for system_userprofile
-- ----------------------------

INSERT INTO `system_userprofile` (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, username, secret, email, mobile, avatar, name, gender, remark, user_type, create_datetime, update_datetime, dept_id, dept_belong_id, creator_id) VALUES (1, 'pbkdf2_sha256$150000$X0RG2idBumnn$TaMaXFquGzyDtytL3ofZG/sSN+1VR521A9xLkUPxYI4=', '2021-02-27 06:20:28.214775', 1, '', '', 1, 1, '2021-02-27 06:20:09.188689', 'admin', '3704adf3-380f-4c27-a8da-60420e8cb4ab', 'admin@qq.com', NULL, NULL, '管理员', '2', '1', 2, '2021-02-27 06:20:09.263192', '2021-02-27 09:14:30.009998', 1, 1, 1);
INSERT INTO `system_userprofile` (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, username, secret, email, mobile, avatar, name, gender, remark, user_type, create_datetime, update_datetime, dept_id, dept_belong_id, creator_id) VALUES (2, 'pbkdf2_sha256$150000$vWY1VIn7rEJz$qq2iiADgcGumy9kNU1FSBhktcimaudYICviCcOKzfKY=', NULL, 0, '', '', 0, 1, '2021-03-03 15:38:27.009893', 'dvadmin', 'b4c5d79a-f01c-4244-92f8-b5288eca1d50', NULL, NULL, NULL, '普通用户', '2', NULL, 0, '2021-03-03 15:38:27.010771', '2021-03-03 15:38:27.086069', 1, 1, 1);
-- ----------------------------
-- Table structure for system_userprofile_post
-- ----------------------------

INSERT INTO `system_userprofile_post` (id, userprofile_id, post_id) VALUES (1, 1, 1);
INSERT INTO `system_userprofile_post` (id, userprofile_id, post_id) VALUES (2, 2, 4);

-- ----------------------------
-- Table structure for system_userprofile_role
-- ----------------------------

INSERT INTO `system_userprofile_role` (id, userprofile_id, role_id) VALUES (1, 1, 1);
INSERT INTO `system_userprofile_role` (id, userprofile_id, role_id) VALUES (2, 2, 2);
