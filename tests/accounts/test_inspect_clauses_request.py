import json

from thordantic.accounts.requests import InspectClausesRequest
from thordantic.common.clause import Clause
import json

def test_inspect_clauses_request_serialize_ok():
    request = InspectClausesRequest(
        provedWork=1000,
        gasPayer="0xd3ae78222beadb038203be21ed5ce7c9b1bff602",
        expiration=1000,
        blockRef="0x00000000851caf3c",
        clauses=[
            Clause(to="0x0000000000000000000000000000456E65726779",
                   value="0x0",
                   data="0xa9059cbb0000000000000000000000000f872421dc479f3c11edd89512731814d0598db50000000000000000000000000000000000000000000000013f306a2409fc0000"
                   )
        ]
    )
    json_str = request.model_dump_json()
    json_dict = json.loads(json_str)
    deserialized = InspectClausesRequest.model_validate(json_dict)
    assert request == deserialized


