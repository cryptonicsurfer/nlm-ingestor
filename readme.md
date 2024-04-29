### Instruction for pulling Docker Image for NLM_ingestor:
```bash
docker pull ghcr.io/nlmatics/nlm-ingestor:latest
```
### Instructions for Running Docker Container

To run the Docker container, execute the following command:
```bash
docker run -p 5010:5001 ghcr.io/nlmatics/nlm-ingestor:latest
```

### Server Output
After running the Docker command, you should see output similar to this:

```bash
* Serving Flask app '__main__'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5001
* Running on http://172.17.0.2:5001
Press CTRL+C to quit
192.168.65.1 - - [26/Apr/2024 08:42:28] "POST / HTTP/1.1" 404 -
192.168.65.1 - - [26/Apr/2024 08:43:22] "POST / HTTP/1.1" 404 -
192.168.65.1 - - [26/Apr/2024 08:45:31] "POST / HTTP/1.1" 404 -
192.168.65.1 - - [26/Apr/2024 08:49:57] "POST /api/parseDocument?renderFormat=all HTTP/1.1" 200 -
```

API Usage
URL to use for parsing without OCR:
```bash
api_url = 'http://127.0.0.1:5010/api/parseDocument?renderFormat=all'
```

URL to use for parsing pdf with OCR:
```bash
ocr_api_url = 'http://127.0.0.1:5010/api/parseDocument?renderFormat=all&applyOcr=yes'
```

Additional Resources
LLM_sherpa docs:
```bash
sherpa_docs_url = https://llmsherpa.readthedocs.io/en/latest/llmsherpa.readers.html
```

github_llm_sherpa (pip install llmsherpa):
```bash
github url = https://github.com/nlmatics/llmsherpa
```

github_NLM_ingestor (that contains the docker code for serving locally):
```bash
url = https://github.com/nlmatics/nlm-ingestor
```
