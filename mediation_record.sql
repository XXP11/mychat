create table mediation_record
(
    message_id int auto_increment comment '唯一递增id'
        primary key,
    user_id    varchar(255)                       not null comment '当事人id',
    content    text                               null comment '聊天记录，json格式',
    timestamp  datetime default CURRENT_TIMESTAMP null comment '对话时间戳',
    is_success int                                null comment '调节分类预测：1-成功；0-失败'
);

INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (1, 'caoxu', '[]', '2024-03-02 01:50:12', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (2, 'caoxu', '[]', '2024-03-02 01:51:13', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (3, 'ligang', '[]', '2024-03-02 01:51:59', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (4, 'wangyue', '[]', '2024-03-02 01:53:56', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (5, 'wangyue', '[{"user": "应该是搞定了", "Assistant": ""}]', '2024-03-02 01:54:17', 1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (6, 'ligang', '[]', '2024-03-02 01:55:29', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (7, 'caoxu', '[{"user": "哈哈哈", "Assistant": ""}]', '2024-03-02 01:59:38', 1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (8, 'ligang', '[{"user": "", "Assistant": ""}, {"user": "哈哈哈", "Assistant": ""}]', '2024-03-03 19:56:04', 1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (9, 'caoxu', '[{"user": "", "Assistant": ""}, {"user": "111", "Assistant": ""}]', '2024-03-03 19:57:25', 0);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (10, '', '[]', '2024-03-03 19:58:29', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (11, 'caoxu', '[{"user": "", "Assistant": ""}]', '2024-03-03 20:18:32', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (12, 'caoxu', '[]', '2024-03-03 20:19:33', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (13, 'caoxu', '[]', '2024-03-03 20:24:36', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (14, 'caoxu', '[{"user": "", "Assistant": ""}, {"user": "111", "Assistant": ""}]', '2024-03-03 20:24:56', 0);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (15, '', '[]', '2024-03-03 21:37:59', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (16, 'ligang', '[{"user": "", "Assistant": ""}]', '2024-03-03 21:51:53', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (17, 'ligang', '[]', '2024-03-03 21:52:54', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (18, 'caoxu', '[{"user": "", "Assistant": ""}]', '2024-03-08 17:25:10', -1);
INSERT INTO users.mediation_record (message_id, user_id, content, timestamp, is_success) VALUES (19, 'wuyang', '[{"user": "", "Assistant": ""}, {"user": "我会还钱", "Assistant": "正在思考..."}]', '2024-04-15 09:23:02', 0);
