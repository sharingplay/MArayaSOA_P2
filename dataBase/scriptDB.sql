--Table creation
Create table images(
	imageName varchar(40), 
	dateAdded timestamp, 
	image bytea,
	primary key (imageName));
	
Create table results(
	imageName varchar(40),
	results varchar (100),
	dateModified timestamp,
	primary key (imageName));

alter table images 
add constraint unique_Name
unique (imageName);

alter table results 
add constraint unique_NameResults
unique (imageName);

--Functions
CREATE OR REPLACE FUNCTION addImage (image_name varchar(40), image_data bytea) RETURNS void AS $$
insert into images (imageName, dateAdded,image)
values (image_name, CURRENT_TIMESTAMP,image_data);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION updateImage (image_name varchar(40), image_data varchar(100)) RETURNS void AS $$
update images
set imageName = image_name, dateAdded = CURRENT_TIMESTAMP
where imageName = image_name;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION deleteImage (image_name varchar(40)) RETURNS void AS $$
delete from images where imageName = image_name;
delete from results where imageName = image_name;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION addResults (image_name varchar(40), image_results varchar(100)) RETURNS void AS $$
insert into results (imageName, results, dateModified)
values (image_name, image_results, CURRENT_TIMESTAMP);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION updateResults (image_name varchar(40), image_results varchar(100)) RETURNS void AS $$
update results
set results = image_results, dateModified = CURRENT_TIMESTAMP
where imageName = image_name;
$$ LANGUAGE sql;


