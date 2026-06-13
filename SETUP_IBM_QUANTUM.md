# Qiskit IBM Quantum Setup Guide

To run experiments on real quantum hardware or advanced simulators provided by IBM Quantum, you need to configure your environment with an IBM Quantum API token.

## 1. Get an API Token
1. Go to [IBM Quantum Platform](https://quantum-computing.ibm.com/).
2. Create an account or log in.
3. On your dashboard, copy your **API token**.

## 2. Configure Your Environment

We recommend using the standard Qiskit method:

```python
from qiskit_ibm_provider import IBMProvider

# Save account credentials locally (run once)
IBMProvider.save_account(token='YOUR_API_TOKEN', overwrite=True)
```

## 3. Configuration Template
You can copy `config.template.json` to `config.json` and insert your credentials if your experiments load them dynamically:

```json
{
  "ibm_quantum": {
    "token": "YOUR_API_TOKEN",
    "hub": "ibm-q",
    "group": "open",
    "project": "main"
  }
}
```
