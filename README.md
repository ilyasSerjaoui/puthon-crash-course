# Python Automation for Bug Bounty Hunters

A collection of lightweight Python scripts and utilities to speed up recon, discovery, and lightweight vulnerability verification for web bug bounty hunting. These scripts are intended for educational and ethical use only — use them only on targets you own or are authorized to test.

---

## Features

* Simple, single-purpose scripts focused on common bug-bounty tasks:

  * GitHub / public-repo link scrapers
  * Subdomain / domain live-checkers
  * Shodan query helpers
  * Django debug / admin endpoint detectors
  * JavaScript S3/bucket exposer scanners
  * Helpers to extract and normalize domains/URLs

* Minimal dependencies: `requests`, `beautifulsoup4`, `shodan`, and standard library modules.

* Designed to be readable and easy to adapt — the code favors clarity over cleverness so you can customize it quickly for different scopes.

---

## Getting started

### Requirements

* Python 3.8+
* Install dependencies (recommended in a virtualenv):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

A sample `requirements.txt` might contain:

```
requests
beautifulsoup4
shodan
```

### Configuration

* Create files with inputs the scripts expect, for example:

  * `bug-bounty-wordlist.txt` — words you want to feed into Shodan queries
  * `bug-bounty-domains-2.txt` — domain list
  * `bug-bounty-sites.txt` / `bug-bounty-domain.txt` — intermediate outputs
  * `django-debug-list.txt` — discovered Django admin endpoints to test

* If using Shodan scripts, set your API key in an environment variable or within the script (safer: use `SHODAN_API_KEY` env var).

```bash
export SHODAN_API_KEY=your_key_here
```

---

## Usage examples

Below are example usages for typical scripts (update filenames to those in the repo):

**1) GitHub scraper**

```bash
python github_scraper.py
# writes hrefs to bug-bounty-sites.txt and domains to bug-bounty-domain.txt
```

**2) Shodan search helper**

```bash
python shodan_search.py
# reads bug-bounty-wordlist.txt and writes discovered hosts to django-debug-list.txt
```

**3) Django admin/debug checker**

```bash
python django_debug_checker.py
# reads django-debug-list.txt and performs lightweight POST checks for debug leakage
```

**4) JS / S3 bucket finder (JS scanner)**

```bash
python js_s3_scanner.py
# uses subdomain lists and scans HTML/JS for s3.amazonaws.com references
```

---

## Best practices & safety

* **Authorization:** Only test domains you own or are explicitly authorized to test.
* **Rate limits & courtesy:** Add timeouts, error handling, and `time.sleep()` between service/API calls (e.g., Shodan rate limits). Do not overwhelm targets.
* **Secrets:** Never commit API keys or credentials. Use environment variables or a local config file ignored by git.
* **Legal & ethical:** The repository is educational. Use it responsibly.

---

## Contributing

Contributions are welcome. If you want to add a script or improve an existing one:

1. Fork the repository
2. Create a branch (`git checkout -b feature/foo`)
3. Add tests or examples when applicable
4. Open a pull request with a clear description of changes

Make sure your contributions follow the ethical use guidelines above.

---

## Roadmap / Ideas

* Add optional headless browser (Playwright) flows for JS-heavy pages
* Add deduplication, canonicalization, and output CSV/JSON support
* Improve detection heuristics for cloud storage URLs and auto-verify public-read access
* Add simple reporting / CSV export for triaging findings

---

## License

Choose a license for your repo (e.g., MIT). Add a `LICENSE` file.

---

If you want a tailored README that lists the exact filenames and short descriptions from your repository, tell me and I’ll update the README to reference them specifically.
