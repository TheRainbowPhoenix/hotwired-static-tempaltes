import json
from typing import ClassVar, Dict, Optional, Any
import jinja2
from pydantic import BaseSettings, validator
from urllib.parse import urljoin


class ViteSettings(BaseSettings):
    static_url: Optional[str]

    @validator("static_url", pre=True)
    def ensure_slash_for_static_url(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> str:
        if v and v.endswith("/"):
            return v
        elif v:
            return f"{v}/"
        return "/static/"

    assets_path: str = "static/"
    manifest_path: Optional[str]

    @validator("manifest_path", pre=True, always=True)
    def assemble_manifest_path(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        path: str = "static"
        return f"{path}/manifest.json"


settings = ViteSettings()


class ViteLoader(object):
    instance = None
    manifest: ClassVar[dict]

    def __new__(cls):
        """Singleton manifest loader"""
        if cls.instance is not None:
            return cls.instance
        cls.manifest = {}
        cls.instance = super().__new__(cls)
        cls.instance.parse_manifest()

        return cls.instance

    def parse_manifest(self) -> None:
        with open(settings.manifest_path, "r") as manifest_file:
            manifest_content = manifest_file.read()
        try:
            self.manifest = json.loads(manifest_content)
        except Exception:
            raise RuntimeError(
                "Cannot read Vite manifest file at {path}".format(
                    path=settings.manifest_path,
                )
            )

    def generate_script_tag(
        self, src: str, attrs: Optional[Dict[str, str]] = None
    ) -> str:
        """Generates an HTML script tag."""
        attrs_str = ""
        if attrs is not None:
            attrs_str = " ".join(
                [
                    '{key}="{value}"'.format(key=key, value=value)
                    for key, value in attrs.items()
                ]
            )

        return f'<script {attrs_str} src="{src}"></script>'

    def generate_vite_server_url(self, path: Optional[str] = None) -> str:
        """
        Generates an URL to and asset served by the Vite development server.

        Keyword Arguments:
            path {Optional[str]} -- Path to the asset. (default: {None})

        Returns:
            str -- Full URL to the asset.
        """
        base_path = "{protocol}://{host}:{port}".format(
            protocol=settings.server_protocol,
            host=settings.server_host,
            port=settings.server_port,
        )
        return urljoin(
            base_path,
            urljoin(settings.static_url, path if path is not None else ""),
        )

    def generate_vite_asset(
        self, path: str, scripts_attrs: Optional[Dict[str, str]] = None
    ) -> str:
        if path not in self.manifest:
            raise RuntimeError(
                f"Cannot find {path} in Vite manifest at {settings.manifest_path}"
            )

        tags = []
        manifest_entry: dict = self.manifest[path]
        if not scripts_attrs:
            scripts_attrs = {"type": "module", "async": "", "defer": ""}
        # Add dependent CSS
        if "css" in manifest_entry:
            for css_path in manifest_entry.get("css"):
                tags.append(
                    self.generate_stylesheet_tag(
                        urljoin(settings.static_url, css_path))
                )

        # Add dependent "vendor"
        if "imports" in manifest_entry:
            for vendor_path in manifest_entry.get("imports"):
                tags.append(
                    self.generate_vite_asset(
                        vendor_path, scripts_attrs=scripts_attrs)
                )

         # Add the script by itself
        tags.append(
            self.generate_script_tag(
                urljoin(settings.static_url, manifest_entry["file"]),
                attrs=scripts_attrs,
            )
        )

        return "\n".join(tags)


def vite_asset(
    path: str, scripts_attrs: Optional[Dict[str, str]] = None
) -> jinja2.utils.markupsafe.Markup:
    return jinja2.utils.markupsafe.Markup(
        ViteLoader().generate_vite_asset(path, scripts_attrs=scripts_attrs)
    )


def vite_hmr_client() -> jinja2.utils.markupsafe.Markup:
    """
    Generates the script tag for the Vite WS client for HMR.
    Only used in development, in production this method returns
    an empty string.

    If react is enabled,
    Returns:
        str -- The script tag or an empty string.
    """
    tags: list = []
    # tags.append(ViteLoader().generate_vite_react_hmr())
    # tags.append(ViteLoader().generate_vite_ws_client())
    return jinja2.utils.markupsafe.Markup("\n".join(tags))
