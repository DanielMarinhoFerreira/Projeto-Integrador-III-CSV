# Projeto-Integrador-III 

Especificações :
  Esse projeto tem o intuito de realiza analises dos datasets disponibilizado pelo site 'kaggle' 
  - https://www.kaggle.com/datasets/mateusdmachado/csgo-professional-matches

## Requisitos necessarios para rodar o projeto 
 
- [Criar ambiente Virtual](#ambiente)
- [Instalação requirements.txt](#requirements)
- [Instalação  MySql](#MySql)
- [Criar tabela no Banco](#SQL)
- [configurar (db.env)](#connetion)
- [DataSet do zip](#DataSet)
- [Load File](#LoadFile)
  
  
<a name="ambiente"></a>
## Criar Ambiente Virtual

 - utilizar comando abaixo para criar ambiente
```py -m venv env ```

 - ativação da ambiente virtual 
``` env\Scripts\activate.bat ```
  
  - Para mais informações:
  [documentation https://docs.python.org/3/library/venv.html]
    
<a name="requirements"></a>
## Instalação requirements.txt

  obs.: Obrigatório realizar esse processo. 

 ``` pip install -r requirements.txt ```

 - Pra mais informações
  [Documentation https://pypi.org/project/requests/]

<a name="MySql"></a>
## Instalação  MySql


Pra mais informações 
 - Documentation https://dev.mysql.com/doc/refman/8.0/en/general-installation-issues.html
 - Como obter o MySQL https://dev.mysql.com/doc/refman/8.0/en/getting-mysql.html
 
 <a name="SQL"></a>
 ## Criar tabela no Banco
 
 Usar o arquivo create_tables, dentro da pasta sql, para criar as tabelas necessárias para receber os dados do csv.
 
 <a name="DataSet"></a>
 ## DataSet no zip
 
 É necessário colocar os arquivos .csv que estão compactados para fazer o load file dentro do bd, pois foram tratados especificamente para este caso, mas mantendo os mesmos dados.
 Obs.: Não será possível usar o dataset do link.

<a name="LoadFile"></a>
## Load File

Para realizar o Load File, é preciso:

- Colocar os arquivos .csv no caminho 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/', pois o MySQL tem uma trava de segurança para arquivos de outros diretórios.
- Rodar o load_files, que conta na mesma pasta sql do create_tables.
