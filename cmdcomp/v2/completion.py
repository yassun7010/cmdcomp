from pathlib import Path
from typing import Any

from cmdcomp.shell import ShellType
from cmdcomp.v2.config import V2Config


def generate_v2(shell: ShellType, config: V2Config) -> str:
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
    )
    template = env.get_template(f"{shell.value}.sh.jinja")

    return template.render(
        app_name=config.app.name,
        app_aliases=config.app.aliases + config.root.aliases,
        commands={config.app.name: config.root},
        append_key_tag=_append_key_tag,
    )


def _append_key_tag(d: dict[str, Any], tag: str) -> dict[tuple[str, str], Any]:
    return {(tag, k): v for k, v in d.items()}
