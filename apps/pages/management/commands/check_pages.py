"""manage.py check_pages [--lang de] [--strict]

Checks every money-page content file (apps/pages/content/) the way visitors will see it: the
required keys, unique slugs and titles per language, title and description lengths, the copy
rules (no SEO, guarantee, free...), placeholders, images (file present or marked pending),
hreflang targets and that every page's URL reaches it. Fails (exit 1) on any error."""
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Check the money-page content: keys, slugs, lengths, copy rules, images, hreflang, routes."

    def add_arguments(self, parser):
        parser.add_argument("--lang", action="append", metavar="CODE", help="only this language (repeatable)")
        parser.add_argument("--strict", action="store_true", help="warnings fail the check too")

    def handle(self, *args, **options):
        from apps.pages import registry
        from apps.pages.checks import summary, validate

        problems = validate(registry.REGISTRY, langs=options["lang"])
        errors = [p for p in problems if p.level == "error"]
        warnings = [p for p in problems if p.level == "warning"]
        for problem in problems:
            style = self.style.ERROR if problem.level == "error" else self.style.WARNING
            self.stdout.write(style(str(problem)))
        self.stdout.write(summary(registry.REGISTRY))
        if errors or (options["strict"] and warnings):
            raise CommandError(f"{len(errors)} errors, {len(warnings)} warnings.")
        self.stdout.write(self.style.SUCCESS(f"OK: 0 errors, {len(warnings)} warnings."))
