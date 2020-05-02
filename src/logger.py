# !/usr/bin/python3
# -*- coding: utf-8 -*-


from datetime import datetime


__author__ = 'rady'


class Logger:

    def __init__(self):
        self.filename = 'log/' + str(datetime.now()) + '.log'

    def save_log(self, info_list):
        log = open(self.filename, 'w', encoding='utf-8')

        log.write(str(datetime.now()) + '\n')
        log.write('IP To Info Detective\n\n')
        log.write('IP: ' + info_list[0] + '\n')
        log.write('Country: ' + info_list[1] + '\n')
        log.write('Region: ' + info_list[2] + '\n')
        log.write('City: ' + info_list[3] + '\n')
        log.write('Time Zone: ' + info_list[4] + '\n')
        log.write('Zip Code: ' + info_list[5] + '\n')
        log.write('Organization: ' + info_list[6] + '\n')
        log.write('Location: ' + info_list[7] + '\n')
        log.write('Host Name: ' + info_list[8] + '\n')

        log.close()

    
        
        
        
        
