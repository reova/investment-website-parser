from api_url_maker import ApiUrlMaker


def main():
    url: str = "https://www.insightpartners.com/portfolio/?vertical=AI_%2F_ML_%2B_Data%7EBusiness_Operations%7ECybersecurity%7EDevOps%7EFintech%7EFuture_of_Work%7EGTM_Tech%7EHealthTech%7EHorizontal_SaaS%7EHR_Tech%7EIT_Infrastructure%7ELegalTech%7ELogistics_%2F_Supply_Chain%7EOther_Vertical_SaaS%7EPropertyTech&region=North_America&status=Current_Investment"
    x = ApiUrlMaker(url=url)

    print(x.create_api_url())


if __name__ == "__main__":
    main()
