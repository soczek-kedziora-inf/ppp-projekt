CREATE TABLE user (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL
);
-- Można jeszcze jakas ta tabele nizej zmienic nwm
-- tu dałem inta primary key, żeby go autoinkrementować
CREATE TABLE results (
  id INTEGER PRIMARY KEY ,
  createdOn DATETIME NOT NULL,
  originalFilename TEXT NOT NULL,
  classifiedAs TEXT NOT NULL,
  correct BOOLEAN ,
  userId TEXT NOT NULL,
  FOREIGN KEY(userId) REFERENCES user(id)
);