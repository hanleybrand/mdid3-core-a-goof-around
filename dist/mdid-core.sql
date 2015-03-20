DROP DATABASE mdidcore;
CREATE DATABASE mdidcore CHARACTER SET utf8;
 GRANT ALL PRIVILEGES ON mdidcore.* TO mdidcore@localhost
   IDENTIFIED BY 'mdidcore';
 UPDATE mysql.user SET Select_priv='Y',Insert_priv='Y',
   Update_priv='Y',Delete_priv='Y',Create_priv='Y',
   Drop_priv='Y',Index_priv='Y',Alter_priv='Y'
   WHERE Host='localhost' AND User='mdidcore';
 FLUSH PRIVILEGES;
