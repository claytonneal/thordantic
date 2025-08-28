# 🐍 thordantic

[![PyPI version](https://img.shields.io/pypi/v/thordantic.svg)](https://pypi.org/project/thordantic/)
[![Python versions](https://img.shields.io/pypi/pyversions/thordantic.svg)](https://pypi.org/project/thordantic/)
[![License](https://img.shields.io/github/license/yourusername/thordantic.svg)](./LICENSE)
[![Tests](https://github.com/yourusername/thordantic/actions/workflows/tests.yml/badge.svg)](https://github.com/yourusername/thordantic/actions)

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
