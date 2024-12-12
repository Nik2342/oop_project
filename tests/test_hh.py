from unittest.mock import Mock, patch

from src.hh import HeadHunterAPI


@patch("requests.get")
def testHeadHunterAPI(mocked_get):
    response = Mock(status_code=200)
    response.json.return_value = {"items": [{"name": "python developer"}]}
    mocked_get.return_value = response
    result = HeadHunterAPI().get_vacancies(["python"])
    assert result == [
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
        {"name": "python developer"},
    ]
