create table log_data ( data text, updated_on datetime default now() );

create table apex_data (
    name varchar(30) not null,
    code varchar(30) not null,
    status boolean not null default true
);
alter table apex_data add constraint apex_data_uq_name_code unique( name, code);


create table vendor (
    id varchar(50) primary key,
    name varchar(50) not null,
    title varchar(100) not null,
    logo longtext,
    status boolean not null default true
);

create table apex_report (
	 id varchar(30) primary key,
	 name varchar(99) not null,
	 report_url varchar(99) not null
);

create table apex_report_data (
	 id varchar(30) primary key,
	 name varchar(99) not null,
	 status boolean not null default true,
	 apex_report_id varchar(30) not null
);
alter table apex_report_data add constraint apex_report_data_fk_apex_report_id foreign key (apex_report_id) references apex_report(id);

create table access_menu(
    id varchar(99) primary key,
    name varchar(50) not null,
    menu varchar(50) not null,
    role varchar(30) not null,
    vid varchar(50) not null,
    active boolean default true not null,
    priority int not null default 999,
    updated_by varchar(30) default 'system',
    updated_on timestamp default now()
);


create table app_data(
    id varchar(30) primary key,
    name varchar(50) not null,
    code varchar(50) not null,
    active boolean not null default true,
    vid varchar(50) not null,
    updated_by varchar(30) not null default 'system',
    updated_on timestamp not null default now()
);
alter table app_data add constraint app_data_uq_name_code_vid unique(name, code, vid);

create table address (
    id varchar(30) primary key,
    lane varchar(99),
    city varchar(30),
    state varchar(30),
    country varchar(30) default 'India',
    zipcode int(8)
);

create table branch(
    id varchar(30) primary key,
    name varchar(30) not null,
    phone varchar(20),
    mobile varchar(30),
    email varchar(50),
    pan varchar(30),
    tan varchar(30),
    gstin varchar(30),
    lat varchar(99),
    lng varchar(99),
    address_id varchar(30) not null,
    is_main boolean not null default false,
    active boolean not null default true,
    vid varchar(50) not null,
    updated_by varchar(30) default 'system',
    updated_on timestamp default now()
);
alter table branch add constraint branch_fk_address_id foreign key (address_id) references address(id);

create table img (
     id varchar(30) primary key,
     name varchar(99) default 'upload',
     src longtext
);

create table profile (
    id varchar(30) primary key,
    name varchar(50) not null default 'Anonymous',
    mobile varchar(15) not null,
    email varchar(99),
    aadhar varchar(99),
    password varchar(30) not null default '1234',
    token varchar(30),
    role varchar(30) not null default 'Anonymous',
    address_id varchar(30) not null,
    branch_id varchar(30) not null,
    img_id varchar(30) not null,
    active boolean not null default true,
    vid varchar(50) not null,
    created_by varchar(30) not null default 'system',
    created_on timestamp not null default now(),
    updated_by varchar(30) not null default 'system',
    updated_on timestamp not null default now()
);
alter table profile add constraint profile_fk_address_id foreign key (address_id) references address(id);
alter table profile add constraint profile_fk_img_id foreign key (img_id) references img(id);
alter table profile add constraint profile_fk_branch_id foreign key (branch_id) references branch(id);


create table consumer(
    id varchar(30) primary key,
    name varchar(30) not null,
    mobile varchar(20) not null,
    email varchar(99),
    aadhar varchar(20),
    img_id varchar(30) not null,
    address_id varchar(30) not null,
    active boolean not null default true,
    vid varchar(50) not null,
    created_on timestamp not null default now(),
    updated_by varchar(30) not null default 'system',
    updated_on timestamp not null default now()
);
alter table consumer add constraint consumer_fk_address_id foreign key (address_id) references address(id);
alter table consumer add constraint consumer_fk_img_id foreign key (img_id) references img(id);
