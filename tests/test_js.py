import json

import pytest

from src.js import JSONSaver


def test_del_all() -> None:
    vacancy = [{"name": "Разработчик", "pay": "100"}, {"name": "Программист", "pay": "1000"}]
    with pytest.raises(FileNotFoundError) as exc_info:
        JSONSaver("test.json").delete_vacancy()
