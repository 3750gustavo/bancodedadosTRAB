create database bringmeaction
create database outro
create table teste(
ID integer primary key identity,
nome varchar (50)
)

begin transaction

insert into teste values('teste');
--insert into teste values (1,2);

if(@@ERROR >0)
begin
rollback transaction
end
else
begin
commit transaction
end

select * from teste

select * from sys.sql_logins

grant select on teste to vixe;
use bringmeaction