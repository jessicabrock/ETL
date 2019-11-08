### Python ETL

<ul>
    <li>Custom ETL (Extraction Translation Load) using Python 3.x</li>
    <li>Needs to be tested for large data volume, your mileage may vary</li>
    <li>No implied warranties, use at your own risk</i>
</ul>

## File Structure
<pre>
etl
    |__main.py          # entry point for the etl process
    |__.env             # stores datawarehouse name
    |__db_connection.py # connection strings for source db and datawarehouse
    |__sql_queries.py   # sql queries
    |__etl.py           # performs db connection and run sql queries
</pre>

## Data sources
<pre>
Song data is from Million Song dataset https://millionsongdataset.com
Log data is from Event Simulator https://github.com/Interana/eventsim
</pre>

## Setup

You will need the postgresql database installed.

pip install the following modules:

pip install pipenv<br/>
pipenv install psycopg2-binary psycopg2 pandas pytest --dev<br/>
pipenv shell<br/>

You can now run the app from your app environment

## TODO
