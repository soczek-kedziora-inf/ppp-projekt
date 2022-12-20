CREATE TABLE user (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL
);
-- Można jeszcze jakas ta tabele nizej zmienic nwm
CREATE TABLE result (
  id TEXT PRIMARY KEY,
  createdOn DATE NOT NULL,
  classifiedAs TEXT NOT NULL,
  correct BOOLEAN ,
  userId TEXT NOT NULL,
  FOREIGN KEY(userId) REFERENCES user(id)
);