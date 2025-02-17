from markdown_dom import MarkdownSection, MarkdownSectionTitle


def test_render_prompt_section() -> None:
    prompt_section = MarkdownSection(
        MarkdownSectionTitle("Test Prompt"),
        "Hello, world!",
        MarkdownSection(
            MarkdownSectionTitle("Nested Prompt"),
            "Nested prompt content",
        ),
    )

    result = prompt_section.render()

    assert result == (
        """## Test Prompt
Hello, world!

### Nested Prompt
Nested prompt content"""
    )
