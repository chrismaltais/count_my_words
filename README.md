# Count My Words

A Flask app that calculates word-frequency pairs based on the text from a given URL.

First attempt at creating a staging/production workflow that allows changes to be made, helps client presentations, experiments, etc. - all within a sandboxed server without causing any changes to the live production site that users interact with.

Database migration is also explored - the importance of multistep rollout and how DB migration essentially acts as a "version control" 

PostgreSQL as the target database
SQLAlchemy as the DB access library
Alembic as the database migration toolkit