from .prompt_section import PromptSection


class BasePromptRenderer:
    @classmethod
    def render_prompt_section(
        cls, prompt_section: PromptSection, *, section_level: int = 2
    ) -> str:
        raise NotImplementedError


class MarkdownPromptRenderer(BasePromptRenderer):
    @classmethod
    def render_prompt_section(
        cls, prompt_section: PromptSection, *, section_level: int = 2
    ) -> str:
        rendered_elements = []
        if prompt_section.prompt_title is not None:
            rendered_elements.append(
                f"{'#' * section_level} {prompt_section.prompt_title}"
            )

        for i, element in enumerate(prompt_section.elements):
            if isinstance(element, str):
                rendered_elements.append(element)
                continue

            # PromptSection element
            if i > 0:
                rendered_elements.append("")
            rendered_elements.append(
                cls.render_prompt_section(element, section_level=section_level + 1)
            )

        return "\n".join(rendered_elements)
