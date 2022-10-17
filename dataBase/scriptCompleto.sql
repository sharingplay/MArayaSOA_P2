Create table images(
	imageName varchar(40), 
	dateAdded datetime, 
	image text,
	primary key (imageName));

Create table results(
	imageName varchar(40),
	results varchar (100),
	dateModified datetime,
	primary key (imageName));

alter table images 
add constraint unique_Name
unique (imageName);

alter table results 
add constraint unique_NameResults
unique (imageName);

--Functions
DELIMITER &&
CREATE PROCEDURE addImage(in image_Name varchar(40), in image_data text)
BEGIN
insert into images(imageName,dateAdded,image) values (image_Name, CURRENT_TIMESTAMP, image_data);
END&&

DELIMITER &&
CREATE PROCEDURE viewImages()
BEGIN
SELECT * FROM images;
END&&

DELIMITER &&
CREATE PROCEDURE updateImage (in image_Name varchar(40), in image_data text)
BEGIN
update images set image = image_data, dateAdded = CURRENT_TIMESTAMP where imageName = image_Name;
END&&

DELIMITER &&
CREATE PROCEDURE deleteImage (in image_Name varchar(40))
BEGIN
delete from images where imageName = image_Name;
delete from results where imageName = image_Name;
END&&

DELIMITER &&
CREATE PROCEDURE addResults (in image_Name varchar(40), in image_results varchar(100))
BEGIN
insert into results (imageName,results,dateModified) values (image_Name, image_results, CURRENT_TIMESTAMP);
END&&

DELIMITER &&
CREATE PROCEDURE viewResults()
BEGIN
select * from results;
END&&

DELIMITER &&
CREATE PROCEDURE viewImageResults(in image_Name varchar(40))
BEGIN
select results.results from results where imageName = image_Name;
END&&

DELIMITER &&
CREATE PROCEDURE updateResults (in image_Name varchar(40), in image_results varchar(100)) 
BEGIN
update results set results = image_results, dateModified = CURRENT_TIMESTAMP where imageName = image_Name;
END&&

/*
select * from images;
select * from results;
execute addImage @imageName = 'imagen de prueba 2',@image = 'asdfsdfgsdffaser12341';
execute updateImage @imageName = 'imagen de prueba 2',@image = 'imagen modificada';
execute deleteImage @imageName = 'imagen de prueba 2';
execute addResults @imageName = 'imagen de prueba 2',@results = 'esta feliz';
execute updateResults @imageName = 'imagen de prueba 2', @results ='esta triste';
*/