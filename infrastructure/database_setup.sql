-- Create Application Database
CREATE DATABASE IF NOT EXISTS app;

-- => Create tables

-- User table
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Project table
CREATE TABLE IF NOT EXISTS project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    project_description TEXT NOT NULL,
    project_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    project_updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- DailyTasks table
CREATE TABLE IF NOT EXISTS daily_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id FOREIGN KEY REFERENCES user(id),
    project_id FOREIGN KEY REFERENCES project(id),
    date TEXT NOT NULL,
    task TEXT NOT NULL,
    time_spent DECIMAL(5, 2) NOT NULL,
    added_to_jira BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- TimeSheetRecords table
CREATE TABLE IF NOT EXISTS time_sheet_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id FOREIGN KEY REFERENCES user(id),
    project_id FOREIGN KEY REFERENCES project(id),
    start_time DECIMAL(5, 2) NOT NULL,
    end_time DECIMAL(5, 2) NOT NULL,
    actual_duration DECIMAL(5, 2) NOT NULL,
    date TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
