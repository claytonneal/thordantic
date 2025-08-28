# ⚡️ thordantic

> **Pydantic models and JSON schemas for the VeChain Thor API.**  
> Typed validation and parsing of VeChain JSON requests & responses, made easy.

---

## 🚀 Features

- ✅ **Pydantic models** for VeChain Thor RPC endpoints  
- ✅ **Annotated types** (Pydantic v2 style) for core blockchain values like `Address`, `HexInt`, and `HexStr`  
  - Built on `typing.Annotated` → still plain `str`/`int` at runtime  
  - Validators ensure correct format (`0x…`, length checks, etc.)  
  - Serializers guarantee consistent JSON
- ✅ **Strict typing** for requests & responses — prevents passing invalid values  
- ✅ **Auto-generated JSON Schemas** from the models  
- ✅ **Validation** of API responses out-of-the-box  
- ✅ Works with **Thor mainnet, testnet, or solo chains**  
- ✅ Lightweight: only depends on Pydantic, no heavy runtime deps

---

## 📦 Installation

```bash
pip install thordantic
```

## Contributing

To run tests:

```bash
poetry run pytest
```
