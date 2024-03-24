from urllib.parse import unquote
from bs4 import BeautifulSoup

import requests


class ApiUrlMaker:

    def __init__(self, url):
        self._url = url  # web-site url with filters
        self._api_params_dict = {  # api request params without values
            "region[]": [],
            "vertical[]": [],
            "status[]": [],
            "page": 1,
            "search": "",
            "user_id": "",
            "featured[]": [],
            "featured_enabled": False,
        }

    def _fix_url_quote(self):  # fix the quote in url like %2F,%7E
        self._url = unquote(self._url).replace(
            "_", " ")

    def _get_url_params(self):  # get parameters from url
        self._fix_url_quote()

        # separate base url and params after. Make a list
        params_list = self._url.split("/?")[1].split("&")
        params_dict = {}

        for param in params_list:  # fill dictionary with formatted data
            param_list = param.split("=")

            params_dict.update(
                {
                    param_list[0]: param_list[1].split("~") if len(
                        param_list[1]) > 1 else param_list[1]
                }
            )

        return params_dict

    def _get_featured_params(self):  # get parameters from html (data-featured)
        response = requests.get(self._url)
        soup = BeautifulSoup(response.text, "lxml")

        # get list of numbers from html for data-featured param
        data_featured = soup.find(
            'company-index').get('data-featured').split(',')

        return {'featured': data_featured}

    def create_api_url(self):  # combine two dicts into one and transform to api url
        base_url = 'https://www.insightpartners.com/wp-json/insight/v1/get-companies'
        params_url = ''

        url_params = self._get_url_params()
        featured_params = self._get_featured_params()

        # fill _api_params_dict with values
        for key in self._api_params_dict:
            key_param = key.replace("[]", "")  # make param like in link

            if key_param in url_params.keys():
                param_value = url_params.get(key_param)
                self._api_params_dict.update(
                    {key: param_value}
                )  # if only one param - leave as a string
            elif key_param in featured_params.keys():
                param_value = featured_params.get(key_param)

                self._api_params_dict.update(
                    {key: param_value}
                )

        # transform to api url
        for key in self._api_params_dict.keys():
            values = self._api_params_dict.get(key)

            if type(values) is list:
                for value in values:
                    params_url += f'&{key}={value}'
            else:
                params_url += f'&{key}={values}'

        return base_url + params_url.replace('&', '?', 1)
