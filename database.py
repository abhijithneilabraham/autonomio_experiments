from sqlalchemy import create_engine, types
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.exc import DatabaseError
from sqlalchemy.schema import DropTable
import awswrangler as wr
import ast
import pandas as pd



class Database:
    """
    Fetches the query results from database.

    Attributes
    ----------
    data_dir: `str` or `pathlib.Path` object
            absolute path to folder containing all input files.
    schema_dir: `str` or `pathlib.Path` object
            path to folder containing `json` schemas of input files.
            If not specified, auto-generated schema will be used.

    Methods
    -------
    fetch_data(question, query, db_type, username='', password='', database='', host='', port='', drop_db=True)
        Function that fetches the data for the query from the database on local system.
    fetch_data_aws(question, query, db_type, username='', password='', database='', host='', port='', drop_db=True)
        Function that fetches the data for the query from the database on AWS.
    """
    def __init__(self, data_dir, schema_dir, aws_s3, access_key_id, secret_access_key):
        """
        Constructs all the necessary attributes for the database object.

        Attributes
        ----------
        data_dir: `str` or `pathlib.Path` object
                absolute path to folder containing all input files.
        schema_dir: `str` or `pathlib.Path` object
                path to folder containing `json` schemas of input files.
                If not specified, auto-generated schema will be used.
        data_process: `data_utils` class object
        nlp: `NLP` class object
        """
        self.data_dir = data_dir
        self.schema_dir = schema_dir
   
    def __create_db(self, db_url):
        """
        Create database if it doesn't exists.
        """
        try:
            engine = create_engine(db_url, echo=False)
            if not database_exists(engine.url):
                create_database(engine.url)
        except DatabaseError as e:
            import traceback
            traceback.print_exc()
            raise Exception("Check whether the server is running and the connection parameters are correct.")        
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise Exception("Some error occured while connecting to the database.")
        return engine

    def __drop_db(self, db_url):
        """
        Drop the database.
        """
        drop_database(db_url)

    def __delete_table(self, table_name):
        """
        Delete the table.
        """
        DropTable(table_name)

    # Function to load and fetch data from AWS storage.
    def write(self, data_frame,db_type, username='', password='', database='', host='', port='', drop_db=True):

        # dialect+driver://username:password@host:port/database
        if db_type == 'postgres':
            if port is None:    port = 5432     # use default port for postgres if it is None.
            engine = wr.db.get_engine(db_type="postgresql", host=host, port=port, database=database, user=username, password=password)
            # engine =wr.catalog.get_engine("aws-postgres-sql", db_type="postgresql", host=host, port=port, database=database, user=username, password=password)
        elif db_type == 'mysql':
            if port is None:    port = 3306
            engine = wr.db.get_engine(db_type="mysql", host=host, port=port, database=database, user=username, password=password)


        wr.db.to_sql(data_frame, engine, name="experiment_log", if_exists="add", index=False) 

        # answer = wr.db.read_sql_query(query, con=engine)
        # answer = answer.values.tolist()

        # return answer