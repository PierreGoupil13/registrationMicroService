docker build -t password-manager-mariadb .
docker run -d --name password-manager-db -p 3308:3306 password-manager-mariadb
