import json
from pathlib import Path

from jsonschema import Draft202012Validator

import request_module

api_key = "API_KEY_HERE"
SCHEMA_PATH = Path(__file__).with_name("nasa_software_schema.json")


def test_software_search_response_matches_json_schema():
    response = request_module.make_request(API_KEY)
    assert response.status_code == 200
    payload = response.json()

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.absolute_path),
    )

    assert not errors, "Response does not match schema:\n" + "\n".join(
        f"{list(error.absolute_path)}: {error.message}" for error in errors
    )
