"""Numbered sections for the legal pages.

    {% section "subscription" %} ... {% endsection %}
        <section> with an <h2 id="subscription">: the number and title come from the page's
        sections in apps/legal/pages.py (context "toc"), so the headings and the table of
        contents can't drift apart. An id that isn't in the list is an error.
    {% ref "refunds" %}
        a link to another section of the same page: <a href="#refunds">section 7</a>."""
from django import template
from django.utils.html import format_html

register = template.Library()


def _entry(context, section_id):
    for entry in context.get("toc") or ():
        if entry["id"] == section_id:
            return entry
    raise template.TemplateSyntaxError(
        f"Legal section {section_id!r} is not in this page's sections (apps/legal/pages.py)")


class SectionNode(template.Node):
    def __init__(self, section_id, nodelist):
        self.section_id = section_id
        self.nodelist = nodelist

    def render(self, context):
        entry = _entry(context, self.section_id.resolve(context))
        return format_html(
            '<section class="legal-section" aria-labelledby="{0}">'
            '<h2 id="{0}"><span class="legal-num">{1}</span> {2}</h2>{3}</section>',
            entry["id"], entry["number"], entry["title"], self.nodelist.render(context))


@register.tag
def section(parser, token):
    bits = token.split_contents()
    if len(bits) != 2:
        raise template.TemplateSyntaxError('Usage: {% section "id" %}...{% endsection %}')
    nodelist = parser.parse(("endsection",))
    parser.delete_first_token()
    return SectionNode(parser.compile_filter(bits[1]), nodelist)


@register.simple_tag(takes_context=True)
def ref(context, section_id):
    entry = _entry(context, section_id)
    return format_html('<a href="#{}">section {}</a>', entry["id"], entry["number"])
