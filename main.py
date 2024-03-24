from urllib.parse import unquote


def main():
    url = 'https://www.insightpartners.com/portfolio/?vertical=AI_%2F_ML_%2B_Data%7EBusiness_Operations%7ECybersecurity%7EDevOps%7EFintech%7EFuture_of_Work%7EGTM_Tech%7EHealthTech%7EHorizontal_SaaS%7EHR_Tech%7EIT_Infrastructure%7ELegalTech%7ELogistics_%2F_Supply_Chain%7EOther_Vertical_SaaS%7EPropertyTech&region=North_America&status=Current_Investment'
    get_params(url)
    

def get_params(url):
    url = unquote(url).replace('_', ' ')  # fix the quote like %2F,%7E
    params = url.split("/?")[1].split('&')  # separate params and make a list
    params_dict = dict(param.split('=') for param in params)  # separate param keys and value to dict

    api_params_dict = {  # api request params
        'region[]': [],
        'vertical[]': [],
        'status[]': [],
        'page': 1,
        'search': '',
        'user_id': '',
        'featured[]': [],
        'featured_enabled': False,
    }
    
    # fill api_params_dict with values
    for key in api_params_dict:
        key_param = key.replace('[]', '')  # make param like in link
        
        if key_param in params_dict.keys():
            param_value = params_dict.get(key_param)
            
            if '[]' in key:    
                api_params_dict.update({key: param_value.split('~')})  # if more than one param - make as a list
            else:
                api_params_dict.update({key: param_value})  # if only one param - leave as a string
        
    
    print(api_params_dict)


if __name__ == '__main__':
    main()
