insert into apex_data(code, name) values ('ROLE', 'Anonymous');
insert into apex_data(code, name) values ('ROLE', 'User');
insert into apex_data(code, name) values ('ROLE', 'Admin');
insert into apex_data(code, name) values ('ROLE', 'SuperAdmin');

insert into apex_data(code, name) values ('MENU', 'Admin Dashboard');
insert into apex_data(code, name) values ('MENU', 'Dashboard');
insert into apex_data(code, name) values ('MENU', 'App Data');
insert into apex_data(code, name) values ('MENU', 'Consumer');
insert into apex_data(code, name) values ('MENU', 'Branches');
insert into apex_data(code, name) values ('MENU', 'Profiles');
insert into apex_data(code, name) values ('MENU', 'Reports');
insert into apex_data(code, name) values ('MENU', 'Settings');
insert into apex_data(code, name) values('MENU', 'Menu Access');

insert into vendor(id, title, name) values('DFF', 'DFFTech', 'DFF Tech');
insert into address(id) values('DFF_MAIN_BRANCH');
INSERT INTO branch (id, name, vid, is_main, address_id ) VALUES ('DFF_MAIN_BRANCH','DL Tech', 'DFF', true, 'DFF_MAIN_BRANCH');

insert into img( id)  values('SUPPORT_DFF_IMG');
insert into address(id) values('SUPPORT_DFF_ADDRESS');

INSERT INTO profile (id, name, email, mobile, password, role, branch_id, img_id, address_id, vid)
    VALUES ('SUPPORT_DFF_USER','Support User','support@dfftech.com','123456789', '1234', 'SuperAdmin',  'DFF_MAIN_BRANCH', 'SUPPORT_DFF_IMG', 'SUPPORT_DFF_ADDRESS', 'DFF');


insert into apex_report (id, name, report_url)  values('consumer', 'Consumers Report', 'consumer');

insert into apex_report_data(id, name, status, apex_report_id) values('consumer_consumer', 'consumer', true, 'consumer');
insert into apex_report_data(id, name, status, apex_report_id) values('consumer_fromdate', 'fromDate', true, 'consumer');
insert into apex_report_data(id, name, status, apex_report_id) values('consumer_todate', 'toDate', true, 'consumer');
