from thordantic.blocks.responses import CompressedBlockResponse


def test_compressed_block_response():
    json_payload = """
        {
      "number": 22655865,
      "id": "0x0159b379f12b5a01890412718317465b5f3f75c134d8103e4363544e9a3b8f8e",
      "size": 33417,
      "parentID": "0x0159b37886c4504477aac2c806e6506ea4d74130ebb501ab4b76ac758c8c5fea",
      "timestamp": 1757088870,
      "gasLimit": 40000000,
      "beneficiary": "0x0445fab898eef8f6e7a3eea8c9fd7c59b37654ec",
      "gasUsed": 5175427,
      "totalScore": 2213574394,
      "txsRoot": "0x220e79cd409b413ed1c1872ad7cc4b845b76118f977944fed746d70f87f00525",
      "txsFeatures": 1,
      "stateRoot": "0x5aa7de3e59de790e0245d2f9919a69cf15d7a5c42837ef45648fece036b1e1c7",
      "receiptsRoot": "0x8ab966c4c1d835312fbeb8265233fcb829f76f4533f6956513c0a5f28e00c34d",
      "com": true,
      "signer": "0x948048760238b9894ba8deb6cfbf0a68ee83f52f",
      "isTrunk": true,
      "isFinalized": false,
      "baseFeePerGas": "0x9184e72a000",
      "transactions": [
        "0x0802bc6e430e7cde2a8acddb9227c76f4f287a04a40d005e85c99ca007ab576d",
        "0x51f848675b388a801fc9f906ec2ebdb20e1696c0659db4a07f86d2d5b338d44d",
        "0x0c20f0c88179c81ff417dc979ef0d081e74c82c222d75f9ebd8ac61e8598ec5d",
        "0x26942ddc41429816854dc34f58a953bb6376983f26788446c7695fce6ad986d3",
        "0x488d9b03403250be47c38f8e9e82ef20a3e87ceb27387b0d0a3f077f0d5f41c8",
        "0xb0f59351d20875c01b8c769885ac7827676483d3ef1d7a54844abeef89f0eee5",
        "0x94b803ccf7cd35a448d38ba4acade18ff5e04fdc7a4125c05c76d28337ea257d",
        "0x80d1837b01c84f190283d1099e98414dc36d5eea7f29bdfbbf41c7f1f4d873c3",
        "0xb2120d4a6fefad2f3746881e3eebed7ffbc44677a1e33f5fae31c728cf2b5559",
        "0x92a350359ce011402f33924c4b722d25a238b63df02fd5ad247aa0b0f6d249cd",
        "0x4e68526adb0b47ba9eceaf4337350603072ec1ad2fb596b14da74fd041e3ac12",
        "0xc5c3bbf3ba4841fb3abdf7f755b9a6aa6d0c9561ed4fea819eedeac09edf1e82",
        "0x14adfe2ffcd996b6d4a7b67380112338cc1d7f0d6e198b4701daad505dc61428",
        "0x07307319c2b1d6d4c3df668ed2007b9d1c0b04e27e2af9874389e0186a1c6385",
        "0x99c199b92321b4634899f534fcaf026fa0087d9543cf26f9564fc4c97cb146ff",
        "0x53243f457fd4fbcc3b4f1723fef10906c6e3d957211995a6484d8cf59894868c",
        "0x8b6ca9f10bd6bcc5739dd4bf9edb13f85c00c7505cff94a1fd18c7be3d5921ee",
        "0xda4416d5b5da1d9eaed5b813aae761210dcf755b5d0b1bc625cc47c1536c05bd"
      ]
    }
    """
    model = CompressedBlockResponse.model_validate_json(json_payload)
    assert model.number == 22655865
    assert model.transactions[1] == "0x51f848675b388a801fc9f906ec2ebdb20e1696c0659db4a07f86d2d5b338d44d"
    assert model.is_trunk == True