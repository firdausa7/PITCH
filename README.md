# PITCH
## By Firdausa Salat
## Description
This a web application that allows users to submit a pitch. Also, other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account.
## Screenshot
<img src="/home/firdausa/Desktop/PITCH/app/static/images/xxxx.png">

## User Stories
As a user I would like:
* to view the different categories.
* to see the pitches other people have posted.
* to submit a pitch in any category.
* to comment on the different pitches and leave feedback.
* to vote on the pitch and give it a downvote or upvote.

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/firdausa7/PITCH.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitch-world
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.6 manage.py server
  ```
5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology Used
* Python3.6
* Bootstrap
* Css
* Postgres Database
* Javascript
* Jquery

### License
MIT (c) 2017 **[Firdausa Salat](https://github.com/firdausa7)**