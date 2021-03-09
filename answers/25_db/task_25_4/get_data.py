import sqlite3
import sys

from tabulate import tabulate


def print_data_in_rows(data, active=True):
    data = list(data)
    if data:
        print(
            "\n{active} entries:\n".format(active="Active" if active else "Inactive")
        )
        print(tabulate(data))


def get_data_by_key_value(db_name, key, value):
    keys = "mac ip vlan interface switch".split()
    if key not in keys:
        print("This parameter is not supported.")
        print("Valid parameter values: {}".format(", ".join(keys)))
        return
    conn = sqlite3.connect(db_filename)
    query = "select * from dhcp where {} = ? and active = ?".format(key)

    print("\nInformation about devices with the following parameters:", key, value)
    for active in (1, 0):
        result = conn.execute(query, (value, active))
        print_data_in_rows(result, active)
    conn.close()


def get_all_data(db_name):
    print("The dhcp table has the following entries:")
    query = "select * from dhcp where active = ?"
    conn = sqlite3.connect(db_name)
    for active in (1, 0):
        result = conn.execute(query, (active,))
        print_data_in_rows(result, active)
    conn.close()


def parse_args(db_name, args):
    if len(args) == 0:
        get_all_data(db_filename)
    elif len(args) == 2:
        key, value = args
        get_data_by_key_value(db_filename, key, value)
    else:
        print("Please enter two or zero arguments")


if __name__ == "__main__":
    db_filename = "dhcp_snooping.db"
    args = sys.argv[1:]
    parse_args(db_filename, args)
