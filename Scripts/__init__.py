# -*- coding: utf-8 -*-
__author__ = 'Bruno Paes'
__description__ = 'This project aims to classify, based on attributes, the asteroids hazardousness'
__email__ = 'brunopaes05@gmail.com'
__status__ = 'Finalised'

from Scripts.rForest import RandomForest

if __name__ == '__main__':
    obj = RandomForest()
    obj.main()
