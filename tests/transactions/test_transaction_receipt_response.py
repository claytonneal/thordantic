from thordantic.transactions.responses import TransactionReceiptResponse
import json

def test_transaction_receipt_response_parse_ok():
    json_payload = """
        {
            "gasUsed": 5325464,
            "gasPayer": "0x6d95e6dca01d109882fe1726a2fb9865fa41e7aa",
            "paid": "0x2e30e7cecc14f0000",
            "reward": "0xddb78be0a0648000",
            "reverted": false,
            "meta": {
                "blockID": "0x0106a0a0b7ec08f59aa90f961a4e368f7250ea64b186f2076bb171596080ddf3",
                "blockNumber": 17211552,
                "blockTimestamp": 1702641690,
                "txID": "0xb6b5b47a5eee8b14e5222ac1bb957c0bbdc3d489850b033e3e544d9ca0cef934",
                "txOrigin": "0x6d95e6dca01d109882fe1726a2fb9865fa41e7aa"
            },
            "outputs": [
                {
                    "contractAddress": "0xdb86029b0e43e150d8a36191d45b04cc58c9e90b",
                    "events": [
                        {
                            "address": "0xdb86029b0e43e150d8a36191d45b04cc58c9e90b",
                            "topics": [
                                "0xb35bf4274d4295009f1ec66ed3f579db287889444366c03d3a695539372e8951"
                            ],
                            "data": "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa"
                        },
                        {
                            "address": "0xdb86029b0e43e150d8a36191d45b04cc58c9e90b",
                            "topics": [
                                "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
                                "0x0000000000000000000000000000000000000000000000000000000000000000",
                                "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa",
                                "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa"
                            ],
                            "data": "0x"
                        },
                        {
                            "address": "0xdb86029b0e43e150d8a36191d45b04cc58c9e90b",
                            "topics": [
                                "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
                                "0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6",
                                "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa",
                                "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa"
                            ],
                            "data": "0x"
                        },
                        {
                            "address": "0xdb86029b0e43e150d8a36191d45b04cc58c9e90b",
                            "topics": [
                                "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
                                "0x65d7a28e3265b37a6474929f336521b332c1681b933f6cb9f3376673440d862a",
                                "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa",
                                "0x0000000000000000000000006d95e6dca01d109882fe1726a2fb9865fa41e7aa"
                            ],
                            "data": "0x"
                        }
                    ],
                    "transfers": []
                }
            ]
        }
    """
    model = TransactionReceiptResponse.model_validate(json.loads(json_payload))
    assert model.outputs[0].events[1].data == "" # check "0x" parsed as empty string