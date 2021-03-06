CREATE TABLE BOOKS
(
  BOOK_ID INT NOT NULL,
  BOOK_NAME VARCHAR(50) NOT NULL,
  AUTHOR VARCHAR(30) NOT NULL,
  QUANTITY INT NOT NULL,
  PRIMARY KEY (BOOK_ID),
  UNIQUE (BOOK_NAME)
);

CREATE TABLE EMPLOYEE
(
  EMPLOYEE_ID INT NOT NULL,
  EMPLOYEE_NAME VARCHAR(30) NOT NULL,
  POST VARCHAR(20) NOT NULL,
  SALARY INT NOT NULL,
  PRIMARY KEY (EMPLOYEE_ID)
);

CREATE TABLE MEMBERS
(
  MEMBER_ID INT NOT NULL,
  MEMBER_NAME VARCHAR(30) NOT NULL,
  RESIDENTIAL_ADDRESS VARCHAR(50) NOT NULL,
  PHONE_NO VARCHAR(15) NOT NULL,
  EMAIL_ADDRESS VARCHAR(20) NOT NULL,
  PRIMARY KEY (MEMBER_ID)
);

CREATE TABLE ADMINISTRATION
(
  PASSWORD VARCHAR(30) NOT NULL,
  EMPLOYEE_ID INT NOT NULL,
  PRIMARY KEY (EMPLOYEE_ID),
  FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID)
);

CREATE TABLE ISSUED_BOOK
(
  ISSUE_NO INT NOT NULL,
  ISSUED_DATE DATE NOT NULL,
  BOOK_ID INT NOT NULL,
  MEMBER_ID INT NOT NULL,
  EMPLOYEE_ID INT NOT NULL,
  PRIMARY KEY (ISSUE_NO),
  FOREIGN KEY (BOOK_ID) REFERENCES BOOKS(BOOK_ID),
  FOREIGN KEY (MEMBER_ID) REFERENCES MEMBERS(MEMBER_ID),
  FOREIGN KEY (EMPLOYEE_ID) REFERENCES ADMINISTRATION(EMPLOYEE_ID)
);

CREATE TABLE RETURNED_BOOKS
(
  RETURN_NO INT NOT NULL,
  RETURNED_DATE DATE NOT NULL,
  ISSUE_NO INT NOT NULL,
  PRIMARY KEY (RETURN_NO),
  FOREIGN KEY (ISSUE_NO) REFERENCES ISSUED_BOOK(ISSUE_NO)
);