package main

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"log"
)

func Syncdata() {
	// 参考 https://github.com/go-sql-driver/mysql#dsn-data-source-name 获取详情
	dsn := "root:123456@tcp(*.*.*.*:3306)/concurrency?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	db.Exec("UPDATE gin_01_count SET count = count + 1 WHERE id = 1")
	sqlDB, err := db.DB()
	if err != nil {
		log.Fatalf("Error getting SQL database connection: %v", err)
	}
	defer sqlDB.Close()
}
