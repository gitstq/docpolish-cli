"""
AI Enhancement Module - Content polishing and translation via GLM-5.1 API.
"""

import json
import urllib.request
import urllib.error
from typing import Optional, List


class AIEnhancer:
    """AI-powered content enhancement using GLM-5.1 API."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url or "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        self.model = "glm-5.1"

    def is_available(self) -> bool:
        """Check if AI enhancement is available."""
        return self.api_key is not None and len(self.api_key) > 0

    def _call_api(self, messages: List[dict], temperature: float = 0.3) -> Optional[str]:
        """Call GLM-5.1 API."""
        if not self.is_available():
            return None

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        try:
            req = urllib.request.Request(
                self.base_url,
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=60) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"]
        except Exception:
            return None

    def polish_text(self, text: str, style: str = "professional") -> Optional[str]:
        """Polish text content for better readability."""
        system_prompt = (
            f"You are a professional technical writer. "
            f"Polish the following text in a {style} style. "
            f"Keep the original meaning but improve clarity, grammar, and flow. "
            f"Return ONLY the polished text without explanations."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ]

        return self._call_api(messages)

    def translate_text(
        self, text: str, target_lang: str, source_lang: str = "auto"
    ) -> Optional[str]:
        """Translate text to target language."""
        lang_names = {
            "zh-cn": "Simplified Chinese",
            "zh-tw": "Traditional Chinese",
            "en": "English",
            "ja": "Japanese",
            "ko": "Korean",
            "es": "Spanish",
        }

        target_name = lang_names.get(target_lang, target_lang)
        source_hint = f"from {source_lang}" if source_lang != "auto" else ""

        system_prompt = (
            f"You are a professional translator. "
            f"Translate the following text {source_hint} into {target_name}. "
            f"Preserve all Markdown formatting, code blocks, and special syntax. "
            f"Return ONLY the translated text without explanations."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ]

        return self._call_api(messages, temperature=0.2)

    def generate_readme_sections(
        self, project_info: dict, language: str = "en"
    ) -> Optional[dict]:
        """Generate README sections based on project info."""
        lang_prompt = {
            "zh-cn": "Simplified Chinese",
            "zh-tw": "Traditional Chinese",
            "en": "English",
        }.get(language, "English")

        prompt = f"""Generate a professional README for a project with the following details:
Name: {project_info.get('name', 'Project')}
Description: {project_info.get('description', 'A great project')}
Language: {project_info.get('language', 'Python')}
Features: {', '.join(project_info.get('features', []))}

Generate in {lang_prompt}. Return a JSON object with these keys:
- introduction: Project introduction paragraph
- features: List of feature descriptions
- quickstart: Quick start guide
- usage: Usage examples
- contributing: Contribution guidelines
"""

        messages = [
            {"role": "system", "content": "You are a technical documentation expert."},
            {"role": "user", "content": prompt},
        ]

        result = self._call_api(messages, temperature=0.5)
        if result:
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return None
        return None
