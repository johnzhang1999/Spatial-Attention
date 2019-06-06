# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
import os.path as osp
import numpy as np
import pdb
from glob import glob
import re
import csv

def write(path, content):
    with open(path, "a+") as dst_file:
        dst_file.write(content)
class MVB(object):

    def __init__(self, root):

        self.images_dir = osp.join(root)
        self.train_path = 'Info/sa_train.csv'
        self.gallery_path = 'Info/sa_gallery.csv'
        self.query_path = 'Info/sa_query.csv'
#        self.camstyle_path = 'bounding_box_train_camstyle'
        self.train, self.query, self.gallery = [], [], []
        self.num_train_ids, self.num_query_ids, self.num_gallery_ids = 0, 0, 0
        self.load()

    def preprocess(self, path, relabel=True):
        ret = []
        pids = set()
        with open(osp.join(images_dir,path)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                filename,pid,cam = row[0],row[1],row[2]
                pids.add(pid)
                ret.append((filename,pid,cam))
        return ret, len(pids)

    def load(self):
        self.train, self.num_train_ids = self.preprocess(self.train_path)              #[('0002_c1s1_000551_01.jpg', 0, 0),(),(), ...]
        self.gallery, self.num_gallery_ids = self.preprocess(self.gallery_path, False)
        self.query, self.num_query_ids = self.preprocess(self.query_path, False)

        print(self.__class__.__name__, "dataset loaded")
        print("  subset   | # ids | # images")
        print("  ---------------------------")
        print("  train    | {:5d} | {:8d}"
              .format(self.num_train_ids, len(self.train)))
        print("  query    | {:5d} | {:8d}"
              .format(self.num_query_ids, len(self.query)))
        print("  gallery  | {:5d} | {:8d}"
              .format(self.num_gallery_ids, len(self.gallery)))
