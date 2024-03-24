import requests
import json
from api_url_maker import ApiUrlMaker


def main():
    headers = {}
    # example url
    url = "https://www.insightpartners.com/portfolio/?vertical=AI_%2F_ML_%2B_Data%7EBusiness_Operations%7ECybersecurity%7EDevOps%7EFintech%7EFuture_of_Work%7EGTM_Tech%7EHealthTech%7EHorizontal_SaaS%7EHR_Tech%7EIT_Infrastructure%7ELegalTech%7ELogistics_%2F_Supply_Chain%7EOther_Vertical_SaaS%7EPropertyTech&region=North_America&status=Current_Investment"

    # create api url
    api_url = ApiUrlMaker(url=url)
    api_url = api_url.create_api_url()

    companies_dict = dict()
    page_number = 1
    count = 1

    while True:
        companies = get_request(api_url, page_number, headers)  # get list of 12 companies
        
        for company in companies['rows']:
            companies_dict.update({count: company})  # write each company in dict
            count += 1

        page_number += 1

        if not companies["rows"]:  # if list companies is empty - break
            break

    with open('data.json', 'a') as f:  # save data to json file
        f.write(json.dumps(companies_dict, indent=4))


def get_request(url, page_number, headers):  # make api request and get json with companies
    page = url.replace('&page=1', f'&page={page_number}')
    response = requests.request('GET', page, headers=headers)
    response_dict = json.loads(json.loads(response.text))  # run json.loads() twice to convert to dict

    return response_dict


if __name__ == "__main__":
    main()
