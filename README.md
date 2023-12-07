
# README: Database Systems Project Part 1

## Project Information

- **Authors:** Célie Pierre, Sarah Lawrence, Reihaneh Maarefdoust
- **Course:** COS 457 Database Systems
- **Project Part:** 1
- **Due Date:** October 16, 2023

## Pawnee Commons: Database for Creators and Fans of Parks and Recreation

### Introduction

This project focuses on designing an ER diagram for the database of "Pawnee Commons," a platform for creators and fans of the TV show "Parks and Recreation." The ER diagram includes entities, relationships, and the responsibilities of each team member.

### Entities

#### Episode

The entity Episode represents all episodes in the show and includes attributes such as description, title, original air date, and US viewers. Episode numbers overall are key attributes, derived attributes, and composite attributes, combining episode numbers used in each season and season numbers. The Episode entity establishes relationships with Person and Transcript.

#### Transcripts

The entity Transcripts represents character dialogues with attributes including line number and dialogue. Line number is a key and multivalued attribute, and dialogue is a multivalued attribute.

#### Person

The Person entity represents individuals involved in the show, including cast and crew. It includes a key attribute, Person ID; a composite attribute, Name (comprising first name, middle name, and last name); and a multivalued attribute, Job Title. The Person entity establishes relationships with Character and Episode.

#### Character

The entity Character represents the characters in the show. A person plays a character, and a person can play at least no characters and at most one character.

#### Viewers

Represents viewer information and is modeled as a weak entity. This allows for flexibility in handling more data from other databases.

### Relationships

#### Plays

The Plays relationship connects the Character entity to the Person entity. The cardinality is 1..1 for the Character entity to the Plays relationship, indicating that someone has to play a character. The cardinality is 0..1 for Plays relationship to the person because a person can play a character or not.

#### Views

The Views relationship connects the Episode entity to the Viewers entity. It's a total participation relationship, showing that every episode must have views. The cardinality is 1..1, indicating each episode has at least one view.

#### Works On

The Works On relationship connects the Person entity to the Episode entity, indicating what person worked on which episode. The cardinality is 1..N, meaning each person will work on at least one episode and at most all episodes.

#### Has

The Has relationship connects the Episode entity to the Transcript entity. It's a total participation relationship, indicating every episode has a transcript. The cardinality is 1..1, as each episode has at least one transcript.

#### Says

The Says relationship connects the Character entity to the Transcript entity, indicating a character might have a transcript. The cardinality is 0..N for Character entity to Says relationship, as there can be none to many characters saying a transcript. The cardinality is 1..N for Says relationship to the Transcript entity, as one character has to say the transcripts.

