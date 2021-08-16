from trie import Trie
import os, pickle
from utils import filter_chars, get_file_content


# Creates an organize database from sentences for effective search
class CreateDB:
    def __init__(self):
        self.__database = Trie()
        self.__auto_comp_dict = {}  # full sent, and the src
        self.__counter = 0

    # Gets a directory path and read and save all of files data to the database
    def create_db(self, folder):
        try:
            self.read_from_file()
        except FileNotFoundError:
            files = []
            folders = [folder]
            for folder in folders:
                directory = os.fsencode(folder)
                for file in os.listdir(directory):
                    path = str(folder) + "/" + str(file)[2:-1]
                    if os.path.isdir(path):
                        folders.append(path)
                    else:
                        files.append(path)
            for path in files:
                self.insert_file(path)
            self.save_to_file()

    # Reads the organize database from a file instead of over all the files a few times
    def read_from_file(self):
        try:
            with open("database.txt", "rb") as f:
                database = pickle.Unpickler(f).load()
                self.set_auto_complete(database.get(2))
                self.set_database(database.get(1))
            f.close()
        except EOFError:
            return {}
        except FileNotFoundError:
            raise FileNotFoundError
        except Exception as exp:
            print(exp)

    # Saves the organize database to a file
    def save_to_file(self):
        try:
            with open("database.txt", "wb") as f:
                pickle.dump({1: self.get_database(), 2: self.get_auto_complete()}, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        except Exception as exp:
            print(exp)

    def get_database(self):
        return self.__database

    def get_auto_complete(self):
        return self.__auto_comp_dict

    def set_database(self, db):
        self.__database = db

    def set_auto_complete(self, auto):
        self.__auto_comp_dict = auto

    # Gets file path and write is content into the db
    def insert_file(self, file):
        try:
            with open(file, "r", encoding="utf8") as f:
                for sentence in f:
                    if sentence.strip():
                        sentence = sentence.strip()
                        self.__auto_comp_dict[self.__counter] = [sentence, file]
                        self.__database.insert_seq(filter_chars(sentence), self.__counter)
                        self.__counter += 1
                f.close()
        except Exception as exp:
            print(exp)




