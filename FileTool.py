# Yemeksepeti Homework 2
# Instructor: İbrahim Ediz
# Student: Seyit İlktürk

import csv
import json


class FileTool:
    final_list = list()
    temp_dict = dict()
    temp_list = list()

    def __init__(self, path_, fields_):
        self.path_ = path_
        self.fields_ = fields_

        # Opening CSV file and copying all values to final list in which we manage data.

        with open(self.path_, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONE, skipinitialspace=True)

            for line in csv_reader:
                self.final_list.append(line)

    # Generate JSON or CSV file after managing data is done.

    def generate(self, output, output_filepath):
        output = str(output).lower()

        # Exporting JSON file
        if output == "json":

            for item in self.final_list[1:]:
                self.temp_list.append(dict(zip(self.fields_, item)))

            with open(output_filepath, "w") as write_file:
                json.dump(self.temp_list, write_file, indent=4)

        # Exporting CSV File
        elif output == "csv":
            with open(output_filepath, 'w') as output_file:
                csv_writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, escapechar='', quotechar='')

                for line in self.final_list:
                    csv_writer.writerow(line)

    def menu(self):
        while 1:
            checker = 0
            print("-------- MENU --------")
            print("TO SEARCH\t =>\t :search")
            print("TO REMOVE\t =>\t :remove")
            print("TO ADD\t\t =>\t :add")
            print("TO UPDATE\t =>\t :update")
            print("TO QUIT\t\t =>\t :q")
            print("----------------------")

            cmd = input("COMMAND: ").lower()
            if cmd == ":q":
                print("Bye!")
                return 0
            elif cmd == ":search":
                search_value = input("Enter a keyword that you're looking for: ")
                quoted_search_value = '"' + search_value + '"'

                for item in self.final_list:
                    if search_value in item or quoted_search_value in item:
                        self.temp_dict = dict(zip(self.fields_, item))
                        print("----- RESULTS ----")
                        for key, value in self.temp_dict.items():
                            print(key, ":", value)
                        checker = 1

                if checker == 0:
                    print("Ne record is found.")

            elif cmd == ":remove":
                remove_id = int(input("ROW NUMBER: "))
                try:
                    removed_item = self.final_list.pop(remove_id+1)
                    print(removed_item)
                    self.generate('csv', self.path_)
                except IndexError:
                    print("That index does not exist.")

            elif cmd == ":add":
                for item in self.fields_:
                    self.temp_list.append(input(f"{item}: "))

                self.final_list.append(self.temp_list)
                self.generate("csv", self.path_)

            elif cmd == ":update":
                self.temp_list.clear()
                update_id = int(input("ROW NUMBER: "))
                try:
                    for item in self.fields_:
                        self.temp_list.append(input(f"{item}: "))

                    self.final_list[update_id] = self.temp_list
                    self.generate("csv", self.path_)
                except IndexError:
                    print("That index does not exist.")


FileTool("data.csv", ["LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW", "City", "State"]).menu()









