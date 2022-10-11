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

CREATE OR ALTER PROCEDURE updateImage @imageName varchar(40), @image text 
AS BEGIN
update images set image = @image, dateAdded = CURRENT_TIMESTAMP where imageName = @imageName;
END;
GO

CREATE OR ALTER PROCEDURE deleteImage @imageName varchar(40)
AS BEGIN
delete from images where imageName = @imageName;
delete from results where imageName = @imageName;
END;
GO

CREATE OR ALTER PROCEDURE addResults @imageName varchar(40), @results varchar(100) 
AS BEGIN
insert into results (imageName,results,dateModified) values (@imageName, @results, CURRENT_TIMESTAMP);
END;
GO

CREATE OR ALTER PROCEDURE updateResults @imageName varchar(40), @results varchar(100) 
AS BEGIN
update results set results = @results, dateModified = CURRENT_TIMESTAMP where imageName = @imageName;
END;
GO

/*
select * from images;
select * from results;
execute addImage @imageName = 'imagen de prueba 2',@image = 'asdfsdfgsdffaser12341';
execute updateImage @imageName = 'imagen de prueba 2',@image = 'imagen modificada';
execute deleteImage @imageName = 'imagen de prueba 2';
execute addResults @imageName = 'imagen de prueba 2',@results = 'esta feliz';
execute updateResults @imageName = 'imagen de prueba 2', @results ='esta triste';
*/