import json
import allure

from petstore_api_test_project.api.api_requests import post_request, put_request


def update_existing_pet(url, pet_name):
    payload = json.dumps({
        "name": pet_name
    })
    headers = {
        'Content-Type': 'application/json'
    }
    endpoint = '/v2/pet'

    url = url + endpoint

    with allure.step('Отправить запрос для переименования питомца в магазине.'):
        new_pet = put_request(url, headers, payload)

    return new_pet
