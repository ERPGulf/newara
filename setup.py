[project]
name = "newara"
authors = [
    { name = "ERPGulf", email = "support@ERPGUlf.com"}
]
description = " App to accomadate Weighing scale barcode with ERPNext POS"
requires-python = ">=3.10"
readme = "README.md"
dynamic = ["version"]
dependencies = [
    # "frappe~=15.0.0" # Installed and managed by bench.
]

[build-system]

# These dependencies are only installed when developer mode is enabled
[tool.bench.dev-dependencies]
# package_name = "~=1.1.0"
