from thordantic.accounts.responses import InspectClauseResponse


def test_inspect_clauses_response_parse_ok():
    payload = {
        "data": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000001d6275696c74696e3a20696e73756666696369656e742062616c616e6365000000",
        "events": [],
        "transfers": [],
        "gasUsed": 1071,
        "reverted": True,
        "vmError": "execution reverted"
    }
    model = InspectClauseResponse.model_validate(payload)
    assert model.data == payload.get("data")
    assert model.vm_error == payload.get("vmError")
    assert model.gas_used == payload.get("gasUsed")

def test_inspect_clauses_response_parse_with_events():
    payload = {
        "data": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000001d6275696c74696e3a20696e73756666696369656e742062616c616e6365000000",
        "events": [
            { "address": "0x7e9c74cF9B2e8e3275F3f12D27871e2eA84C0f67", "topics": ["0x00000000"], "data": "0x00000000"}
        ],
        "transfers": [],
        "gasUsed": 1071,
        "reverted": True,
        "vmError": "execution reverted"
    }
    model = InspectClauseResponse.model_validate(payload)
    assert model.events[0].address == payload.get("events")[0].get("address").lower()
    assert model.events[0].topics == payload.get("events")[0].get("topics")
    assert model.events[0].data == payload.get("events")[0].get("data")

def test_inspect_clauses_response_parse_with_transfers():
    payload = {
        "data": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000001d6275696c74696e3a20696e73756666696369656e742062616c616e6365000000",
        "events": [],
        "transfers": [
            { "sender": "0x7e9c74cF9B2e8e3275F3f12D27871e2eA84C0f67", "recipient": "0x7e9c74cF9B2e8e3275F3f12D27871e2eA84C0f67", "amount": "0x47fdb3c3f456c0000" }
        ],
        "gasUsed": 1071,
        "reverted": True,
        "vmError": "execution reverted"
    }
    model = InspectClauseResponse.model_validate(payload)
    assert model.transfers[0].sender == payload.get("transfers")[0].get("sender").lower()
    assert model.transfers[0].recipient == payload.get("transfers")[0].get("recipient").lower()
    assert model.transfers[0].amount == int(payload.get("transfers")[0].get("amount"), 16)