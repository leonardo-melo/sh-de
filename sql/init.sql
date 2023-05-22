CREATE TABLE Scores (
	id INT,
	patient_id INT,
	scores JSONB,
	date DATE
);

INSERT INTO Scores (id, patient_id, scores, date) VALUES (1, 1323, '{"satisfaction": 9, "pain": 2, "fatigue": 2}', '2020-06-25');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (2, 9032, '{"satisfaction": 2, "pain": 7, "fatigue": 5}', '2020-06-30');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (3, 2331, '{"satisfaction": 7, "pain": 1, "fatigue": 1}', '2020-07-05');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (4, 2303, '{"satisfaction": 8, "pain": 9, "fatigue": 0}', '2020-07-12');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (5, 1323, '{"satisfaction": 10, "pain": 0, "fatigue": 0}', '2020-07-09');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (6, 2331, '{"satisfaction": 8, "pain": 9, "fatigue": 5}', '2020-07-20');
