CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    height DECIMAL(5,2),
    weight DECIMAL(5,2),
    age INT,
    gender VARCHAR(10),
    activity_level VARCHAR(20)
);

CREATE TABLE Foods (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    calories DECIMAL(8,2),
    protein DECIMAL(8,2),
    fat DECIMAL(8,2),
    carbs DECIMAL(8,2)
);

CREATE TABLE Meals (
    meal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    food_id INT,
    quantity DECIMAL(8,2),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (food_id) REFERENCES Foods(food_id)
);

CREATE TABLE Workouts (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    exercise_type VARCHAR(50),
    duration INT,
    calories_burned DECIMAL(8,2),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Foods (name, calories, protein, fat, carbs) VALUES
('Gà luộc', 165, 31, 3.6, 0),
('Cơm trắng', 130, 2.7, 0.3, 28),
('Bông cải xanh', 35, 2.8, 0.4, 7);