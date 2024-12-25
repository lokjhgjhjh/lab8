CREATE TABLE Categories (
    CategoryID SERIAL PRIMARY KEY,
    CategoryName VARCHAR(50)
);

CREATE TABLE Posts (
    PostID SERIAL PRIMARY KEY,
    Title VARCHAR(100),
    Content TEXT,
    CategoryID INT,
    ImageURL VARCHAR(255),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
