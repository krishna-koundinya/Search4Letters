# Search4Letters

A Python based web application to find occurrence of given letters in a given phrase.  
## Getting Started

Required: [Python 3.8](https://www.python.org/downloads/) and [MySQL](https://dev.mysql.com/downloads/mysql/) installed to run this application.  
Clone the repo and follow these steps to run the application.  
Install [Anaconda](https://www.anaconda.com/) ( Optional )  

### Creating a vitual environment (Optional)

Open conda prompt and cd to your project dirctory.  
Create a virtual environment (<> not included )

```
(base) your\project\directory> conda create -n <your_virtual_environment_name> python==3.8
```

Activate the virtual environment 

```
(base) your\project\directory> conda activate <your_virtual_environment_name>
```
Deactivate the environment using

```
(your_environment_name) your\project\directory> conda deactivate
```
### Installing Required Python Modules

Use the requirements.txt to install required modules
```
Search4Letters> pip install -r requirements.txt
```
### Installing MySQL

Use this [link](https://dev.mysql.com/downloads/mysql/) to install MySQL Server
### Troubleshooting MySQL for Windows

Create a folder named 'data' in C:\Program Files\MySQL\MySQL Server 8.0\  
Open command prompt and cd to C:\Program Files\MySQL\MySQL Server 8.0\bin\  
Run
```
> mysqld --initialize --console
```
Make necessary changes hereafter, like editing credentials.  
Edit 'user' and 'password' in vsearch4web.py
### Creating Database and table
Create a database named 'vsearchlogdb' using MySQL shell
```
MySQL | SQL> CREATE DATABASE vsearchlogdb;
```
Use 'vsearchlogdb' database
```
MySQL | SQL> USE vsearchlogdb;
```
Create a table named 'log' in 'vsearchlogdb' database
```
MySQL | SQL> create table log( id int auto_increment primary key,
                               ts timestamp default current_timestamp,
                               phrase varchar(128) not null,
                               letters varchar(32) not null,
                               ip varchar(16) not null,
                               browser_string varchar(256) not null,
                               results varchar(64) not null );
```
## Running the application
Run the application from Search4Letters folder
```
Search4Letters> python vsearch4web.py
```
## Output [Log]
![alt text](./images/log.jpg?raw=true)

## Built With

* [Flask](https://pypi.org/project/Flask/) - The web application framework
* [MySQL](https://www.mysql.com/) - Database

## References

* [Head First Python](https://www.oreilly.com/library/view/head-first-python/9781491919521/)
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [MySQL Documentation](https://dev.mysql.com/doc/)