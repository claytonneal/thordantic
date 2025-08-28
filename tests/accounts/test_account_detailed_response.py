from thordantic.accounts.responses import AccountDetailResponse


def test_account_detail_response_parse_ok():
    payload = {
        "balance": "0x0de0b6b3a7640000",
        "energy":  "0x00",
        "hasCode": False,
    }
    model = AccountDetailResponse.model_validate(payload)
    assert int(model.balance) == int(payload.get("balance"), 16)
    assert int(model.energy) == 0
    assert model.has_code is False
