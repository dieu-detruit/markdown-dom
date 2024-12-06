from __future__ import annotations


class PromptSectionTitle:
    def __init__(self, title: str):
        self._title = title

    @property
    def title(self) -> str:
        return self._title


class PromptSection:
    def __init__(
        self,
        prompt_title_or_element: PromptSectionTitle | PromptSection | str,
        *elements: PromptSection | str,
    ):
        if isinstance(prompt_title_or_element, PromptSectionTitle):
            self._prompt_title: str | None = prompt_title_or_element.title
        else:
            self._prompt_title = None

        self._elements = elements

    def render(self, *, section_level: int = 2) -> str:
        rendered_elements = []
        if self._prompt_title is not None:
            rendered_elements.append(f"{'#' * section_level} {self._prompt_title}")

        for element in self._elements:
            if isinstance(element, str):
                rendered_elements.append(element)
                continue

            # PromptSection element
            rendered_elements.append("")
            rendered_elements.append(element.render(section_level=section_level + 1))

        # remove redundant empty line at the beginning
        if self._prompt_title is None:
            rendered_elements.pop(0)

        return "\n".join(rendered_elements)
