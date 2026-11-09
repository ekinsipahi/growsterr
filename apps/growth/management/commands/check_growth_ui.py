"""Check the growth UI string files (apps/growth/i18n/<code>.py) against the English source:
    python manage.py check_growth_ui            # every language that has a file
    python manage.py check_growth_ui de nl      # only these (a missing file is a problem)
Imports only those languages' files, so it works while other translations are in progress.
A site language without a file is listed and shown in English on the growth pages."""
from django.core.management.base import BaseCommand, CommandError

from apps.core.languages import LANG_BY_CODE, LANGS
from apps.growth.validate import check, has_file


class Command(BaseCommand):
    help = "Validate the growth UI translations (keys, shapes, placeholders, wording rules)."
    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument("codes", nargs="*", help="Language codes (default: every language that has a file).")

    def handle(self, *args, **opts):
        codes = opts["codes"]
        if not codes:
            codes = [lang.code for lang in LANGS if has_file(lang.code)]
            missing = [lang.code for lang in LANGS if not has_file(lang.code)]
            if missing:
                self.stdout.write(f"No file yet (shown in English): {' '.join(missing)}")
        failed = False
        for code in codes:
            if code not in LANG_BY_CODE:
                problems = [f"{code}: not a site language (apps/core/languages.py)"]
            elif not has_file(code):
                problems = [f"{code}: apps/growth/i18n/{code}.py doesn't exist yet"]
            else:
                problems = check(code)
            for p in problems:
                self.stdout.write(p)
            self.stdout.write(f"{code}: {'OK' if not problems else f'{len(problems)} problem(s)'}")
            failed = failed or bool(problems)
        if failed:
            raise CommandError("UI translation check failed")
