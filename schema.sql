drop table if exists entries;

create table responses (
  id integer PRIMARY KEY,
  user_id text not null,
  email text not null UNIQUE,
  first_name text not null,
  last_name text not null,
  travel boolean,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

create table users (
    id integer primary key,
    email text not null UNIQUE,
    user_password text not null,
    first_name text not null,
    last_name text not null,
    date_of_birth DATETIME,
    organization text,
    resume_link text UNIQUE,
    github_link text UNIQUE,
    linkedin_link text UNIQUE,
    score integer,
    status integer,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (id) REFERENCES responses (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
);