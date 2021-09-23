create table countries
(
  country_id serial primary key,
  country_code varchar not null,
  name_label varchar not null
);

insert into countries(country_code, name_label) values
  ('JP', '日本'),
  ('US', 'アメリカ'),
  ('IT', 'イタリア')
;