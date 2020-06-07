import sqlite3
import yaml
import os

from misc.setup_logger import logger


def read_config():
    """
    Loads data from config.yaml to cfg.
    :return: Configuration in Python readable format
    """
    with open("config.yaml", "r") as yamlfile:
        try:
            conf = yaml.safe_load(yamlfile)
        except yaml.YAMLError as exc:
            logger.info("Some error occurred while reading config.yaml - {}".format(exc))
    return conf


# Global variable cfg for configuration file
cfg = read_config()


def prepare_db():
    """
    Prepares the DB for a new run by clearing all data.
    :return: None
    """
    create_db()
    clear_db()


def create_db():
    """
    Create new DB
    :return: None
    """
    try:
        sqliteConn = connect_db()
        cursor = sqliteConn.cursor()
        create_table_query = """CREATE TABLE collection (
                    browser TEXT,
                    version TEXT,
                    screenshots INTEGER
                     );"""
        cursor.execute(create_table_query)
        sqliteConn.commit()
        cursor.close()
        logger.info("Successfully created DB.")
    except sqlite3.Error as error:
        logger.error("Error while connecting to the DB - {}".format(error))
    finally:
        disconnect_db(sqliteConn)


def clear_db():
    """
    Deletes all data from the DB
    :return: None
    """
    try:
        sqliteConn = connect_db()
        cursor = sqliteConn.cursor()
        delete_query = "DELETE FROM collection"
        cursor.execute(delete_query)
        sqliteConn.commit()
        cursor.close()
        logger.info("Successfully cleared DB from previous run.")
    except sqlite3.Error as error:
        logger.error("Error while connecting to the DB - {}".format(error))
    finally:
        disconnect_db(sqliteConn)


def connect_db():
    """
    Connect to the DB
    :return: None
    """
    try:
        sqliteConn = sqlite3.connect('tls_screenshots.db')
        return sqliteConn
    except sqlite3.Error as error:
        logger.error("Error while connecting to the DB - {}".format(error))


def disconnect_db(conn):
    """
    Disconnect from the DB if connection exists
    :param conn: DB connection
    :return: None
    """
    if conn:
        conn.close()


def insert_into_db(browser, version, screenshots):
    """
    Insert into DB
    :param browser: Browser
    :param version: Browser version
    :param screenshots: Number of screenshots collected
    :return: None
    """
    try:
        sqliteConn = connect_db()
        cursor = sqliteConn.cursor()
        insert_query = """INSERT INTO collection(browser, version, screenshots) 
                    VALUES ('{}', '{}', {});""".format(browser, version, screenshots)
        cursor.execute(insert_query)
        sqliteConn.commit()
        cursor.close()
        logger.info("Successfully inserted into DB.")
    except sqlite3.Error as error:
        logger.error("Error while inserting - {}".format(error))
    finally:
        disconnect_db(sqliteConn)


def update_db(browser, version):
    """
    Update DB
    :param browser: Browser
    :param version: Browser version
    :return: None
    """
    try:
        sqliteConn = connect_db()
        cursor = sqliteConn.cursor()
        update_query = """UPDATE collection 
                    SET screenshots = screenshots + 1 
                    WHERE browser = '{}' AND version = '{}'""".format(browser, version)
        cursor.execute(update_query)
        sqliteConn.commit()
        cursor.close()
        logger.info("Successfully updated DB.")
    except sqlite3.Error as error:
        logger.error("Error while updating - {}".format(error))
    finally:
        disconnect_db(sqliteConn)


def get_sum_from_db(screenshots=True):
    """
    Gets a number of screenhots/errors successfully collected
    :param screenshots: True if total number of collected screenshots is desired, False otherwise
    :return: None
    """
    try:
        sqliteConn = connect_db()
        if screenshots:
            screenshots_summary(sqliteConn)
            browsers_summary(sqliteConn)
            versions_summary(sqliteConn)
    except sqlite3.Error as error:
        print("Error while connecting to the DB - {}".format(error))
    finally:
        disconnect_db(sqliteConn)


def screenshots_summary(conn):
    """
    Creates and executes query to get all collected screenshots
    :param conn: DB connection
    :return: None
    """
    cursor = conn.cursor()
    total_query = "SELECT * FROM collection"
    cursor.execute(total_query)
    total = len(cursor.fetchall())

    get_query = "SELECT SUM(screenshots) FROM collection"
    cursor.execute(get_query)
    record = cursor.fetchone()[0]
    logger.info("{} screenshots collected out of {} possible.".format(record, total * get_cases_from_conf()))
    cursor.close()


def get_cases_from_conf():
    """
    Gets all cases which might be run from config.yaml file
    :return: Number of cases in config.yaml file
    """
    cases_in_conf = 0
    for count, case in enumerate(cfg.get("cases")):
        cases_in_conf = count + 1
    return cases_in_conf


def browsers_summary(conn):
    """
    Creates and executes query to get all browsers
    :param conn: DB connection
    :return: None
    """
    cursor = conn.cursor()
    brwosers_total = "SELECT COUNT(browser) FROM collection"
    cursor.execute(brwosers_total)
    record = cursor.fetchone()[0]
    logger.info("{} browsers processed.".format(record))
    cursor.close()


def versions_summary(conn):
    """
    Creates and executes query to get all browsers
    :param conn: DB connection
    :return: None
    """
    cursor = conn.cursor()
    brwosers_total = "SELECT COUNT(version) FROM collection"
    cursor.execute(brwosers_total)
    record = cursor.fetchone()[0]
    logger.info("{} browser versions processed.".format(record))
    output_collection(cursor)
    cursor.close()


def output_collection(cursor):
    """
    Writes the data from DB to a csv file.
    :param cursor: DB cursor
    :return: None
    """
    output = os.getcwd() + "\\db_output.csv"
    with open(output, 'w') as csv_file:
        for row in cursor.execute("SELECT * FROM collection"):
            for field in row:
                csv_file.write(str(field) + " ")
            csv_file.write("\n")
        csv_file.close()
