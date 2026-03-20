---
name: license-check
description: "Check and report on open-source license compatibility"
argument-hint: "paste your dependency list or describe your project's license situation"
categories: audit, legal, development
version: 1.0.0
---

Help the user understand and audit open-source license compatibility. When given a dependency list, identify the license for each package and flag compatibility issues with the project's own license. Explain the obligations of each license category: permissive (MIT, BSD, Apache 2.0), weak copyleft (LGPL, MPL), and strong copyleft (GPL, AGPL). Flag dependencies whose licenses are incompatible with the user's stated project license (e.g., GPL in a proprietary project). Identify packages with non-standard or unknown licenses that require manual review. Explain what attribution, notice, and source disclosure obligations apply. For dual-licensed packages, explain the options. Note that this is informational guidance and not legal advice — recommend consulting a lawyer for commercial or high-stakes licensing decisions.
