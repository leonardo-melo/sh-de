-- Exercise data

INSERT INTO Scores (id, patient_id, scores, date) VALUES (1, 1323, '{"satisfaction": 9, "pain": 2, "fatigue": 2}', '2020-06-25');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (2, 9032, '{"satisfaction": 2, "pain": 7, "fatigue": 5}', '2020-06-30');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (3, 2331, '{"satisfaction": 7, "pain": 1, "fatigue": 1}', '2020-07-05');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (4, 2303, '{"satisfaction": 8, "pain": 9, "fatigue": 0}', '2020-07-12');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (5, 1323, '{"satisfaction": 10, "pain": 0, "fatigue": 0}', '2020-07-09');
INSERT INTO Scores (id, patient_id, scores, date) VALUES (6, 2331, '{"satisfaction": 8, "pain": 9, "fatigue": 5}', '2020-07-20');

-- Extra tests

-- INSERT INTO Scores (id, patient_id, scores, date) VALUES (7, 2331, '{"satisfaction": 9, "pain": 9, "fatigue": 5}', '2020-06-25');
-- INSERT INTO Scores (id, patient_id, scores, date) VALUES (8, 2331, '{"satisfaction": 2, "pain": 9, "fatigue": 5}', '2020-06-27');
-- INSERT INTO Scores (id, patient_id, scores, date) VALUES (9, 2309, '{"satisfaction": 2, "pain": 9, "fatigue": 5}', '2020-06-27');
-- INSERT INTO Scores (id, patient_id, scores, date) VALUES (10, 2310, '{"satisfaction": 2, "pain": 9, "fatigue": 5}', '2020-06-27');
-- INSERT INTO Scores (id, patient_id, scores, date) VALUES (11, 2311, '{"satisfaction": 2, "pain": 9, "fatigue": 5}', '2020-06-27');
-- INSERT INTO Scores (id, patient_id, scores, date) VALUES (12, 2312, '{"satisfaction": 2, "pain": 9, "fatigue": 5}', '2020-06-27');
-- delete from scores where id in (7,8,9,10,11,12);