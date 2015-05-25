create table Aluno(
curso varchar(20),
nome varchar(20),
matricula Integer,
telefone varchar(20)
id Integer,
);

create table Atividade(
nome varchar(20),
descricao varchar(50),
Pontuação float
id Integer,
);

Create sequence id_aluno;
Alter table Aluno alter column id set DEFAULT nextval ('id');

Create sequence id_atividade;
Alter table Atividade alter column id set DEFAULT nextval ('id');
