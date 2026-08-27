import warnings
from typing import Any, Dict, Optional

import requests
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter("ignore", InsecureRequestWarning)


class APIClient:
    def __init__(self, default_headers: Optional[Dict[str, str]] = None):
        """
        Initialize API client with base URL and optional default headers.
        """
        self.base_url = "https://be.1-thing.in"  # base_url.rstrip("/")
        self.default_headers = default_headers or {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            "Referer": "https://1-thing.in/",
            "origin": "https://1-thing.in"
        }
        self.token = None

    def _build_url(self, endpoint: str) -> str:
        """
        Construct full URL.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _parse_response(self, response: requests.Response) -> Any:
        """
        Safely parse response JSON or return text.
        """
        try:
            return response.json()
        except ValueError:
            return response.text

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Make a POST request.
        """
        url = self._build_url(endpoint)
        request_headers = {**self.default_headers, **(headers or {})}

        try:
            response = requests.post(
                url=url,
                data=data,
                json=json,
                headers=request_headers,
                params=params,
                timeout=timeout,
                files=files,
                verify=False,
                # verify=certifi.where(),
            )

            response.raise_for_status()

            return {
                "headers": response.headers,
                "status_code": response.status_code,
                "data": self._parse_response(response),
            }

        except requests.exceptions.HTTPError as http_err:
            return {"error": "HTTP error", "details": str(http_err)}

        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}

        except requests.exceptions.RequestException as err:
            return {"error": "Request failed", "details": str(err)}
