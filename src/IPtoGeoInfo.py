# !/usr/bin/python3
# -*- coding: utf-8 -*-


import requests


__author__ = 'rady'


class Detective:
    
    def __init__(self, target):
        self.url = f'https://ipinfo.io/{target}/json'
        self.ip = target
        self.country = '-'
        self.region = '-'
        self.city = '-'
        self.timezone = '-'
        self.zipcode = '-'
        self.org = '-'
        self.loc = ''
        self.hostname = '-'

    def get_json(self):
        return requests.get(self.url).json()

    def json_edit(self, json):
        if 'country' in json:
            self.country = json['country']

        if 'region' in json:
            self.region = json['region']

        if 'city' in json:
            self.city = json['city']

        if 'timezone' in json:
            self.timezone = json['timezone']

        if 'postal' in json:
            self.zipcode = json['postal']

        if 'org' in json:
            self.org = json['org']

        if 'loc' in json:
            self.loc = json['loc']

        if 'hostname' in json:
            self.hostname = json['hostname']

    def return_all_var(self):
        return [self.ip, self.country, self.region, self.city, self.timezone, self.zipcode, self.org, self.loc, self.hostname]
