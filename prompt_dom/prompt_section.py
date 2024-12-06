from __future__ import annotations

from typing import TypeVar

import pydantic.dataclasses

from .renderer import BasePromptRenderer


@pydantic.dataclasses.dataclass
class PromptSectionTitle:
    title: str

    def __init__(self, title: str) -> None:
        self._title = title


PromptRenderer = TypeVar("PromptRenderer", bound=BasePromptRenderer)


@pydantic.dataclasses.dataclass
class PromptSection:
    prompt_title: str | None
    elements: list[PromptSection | str]

    def __init__(
        self,
        prompt_title_or_element: PromptSectionTitle | PromptSection | str | None,
        *elements: PromptSection | str | None,
    ):
        if isinstance(prompt_title_or_element, PromptSectionTitle):
            self.prompt_title = prompt_title_or_element.title
            self.elements = [element for element in elements if element is not None]
        else:
            self.prompt_title = None
            self.elements = [
                element
                for element in [prompt_title_or_element, *elements]
                if element is not None
            ]

    def render(self, *, section_level: int = 2, renderer: PromptRenderer) -> str:
        return renderer.render_prompt_section(self, section_level=section_level)
