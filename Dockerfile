# Use the official MariaDB image as the base image
FROM mariadb:latest

# Set environment variables for MariaDB configuration
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=password_manager
ENV MYSQL_USER=db_user
ENV MYSQL_PASSWORD=db_password

# Expose the MySQL port
EXPOSE 3306
