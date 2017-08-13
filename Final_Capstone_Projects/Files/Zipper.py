# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 2017

@author: Ethan Shapiro
"""

import zipfile
import os
from Final_Capstone_Projects.Files import HuffmanCoding

class Zipper(object):

    def zip(self, file_name, string=None):
        """
        Pass a file name to save to a zip
        Pass a file name and a string to save to a text file and then to a zip
        :param file_name:
        :param string:
        :return:
        """
        # Make file if user has passed a string
        if string:
            new_file_name = file_name + '.txt'
            with open(new_file_name, 'w') as f:
                f.write(string)

        with zipfile.ZipFile(file_name+'.zip', 'w') as f:
            f.write(file_name+'.txt')

        if string:
            os.remove(new_file_name)

    def zip_compress_huffman(self, string):
        pass


    def zip_decompress_huffman(self, zip_file):
        pass

z = Zipper()
test_string = 'a' + 'b'*3 + 'c'*10 + 'o'*12 + 'd'*15 + 'f'*20
z.zip_compress_huffman(test_string)


