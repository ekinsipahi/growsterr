"""What each language is missing compared to English, and what is wrong (docs/I18N.md):

    python manage.py check_i18n               # every language: a summary line each, details for started ones
    python manage.py check_i18n de pt         # these languages, in full
    python manage.py check_i18n de --same     # also list texts still identical to English

Per language it checks the two files a translator writes for the site's own strings:
    apps/core/i18n/<code>.py     chrome + core pages, against apps/core/i18n/en.py (apps.core.i18n_check)
    apps/growth/i18n/<code>.py   packages, order page, account area, against en.py (apps.growth.validate)
The money pages (apps/pages/content/<code>/) have their own check: manage.py check_pages --lang <code>.

Fails (exit code 1) when a file that exists has missing keys or problems, or a language named
on the command line has no file. A language nobody has started yet is listed, not a failure."""
from django.core.management.base import BaseCommand, CommandError

from apps.core import i18n_check
from apps.core.languages import LANG_BY_CODE, LANGS


def growth_report(code):
    """(exists, problems) of apps/growth/i18n/<code>.py; missing keys are among the problems."""
    from apps.growth import validate

    if not validate.has_file(code):
        return False, []
    return True, validate.check(code)


class Command(BaseCommand):
    help = "List, per language, the translation keys missing compared to English, and the problems."
    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument("codes", nargs="*", help="Language codes (default: all 41).")
        parser.add_argument("--same", action="store_true", help="Also list texts identical to English.")

    def handle(self, *args, **opts):
        named = opts["codes"]
        codes = named or [lang.code for lang in LANGS]
        failed = []
        for code in codes:
            if code not in LANG_BY_CODE:
                self.stdout.write(f"{code}: not a site language (apps/core/languages.py)")
                failed.append(code)
                continue
            if not self.language(code, opts["same"], explicit=bool(named)):
                failed.append(code)
        if failed:
            raise CommandError(f"translations to fix: {' '.join(failed)}")

    def language(self, code, same, explicit):
        """Prints one language's report; False when it fails the check."""
        core = i18n_check.check(code)
        growth_exists, growth_problems = growth_report(code)
        name = LANG_BY_CODE[code].name
        if not core.exists and not core.problems and not growth_exists:
            self.stdout.write(f"{code} ({name}): not started: no apps/core/i18n/{code}.py, no apps/growth/i18n/{code}.py "
                              "(English chrome, no core pages, English growth pages)")
            return not explicit

        to_fix = bool(core.problems) or (core.exists and bool(core.missing)) or bool(growth_problems)
        complete = core.exists and growth_exists and not to_fix
        self.stdout.write(f"{code} ({name})")
        if core.exists or core.problems:
            counts = f"{len(core.missing)} missing, {len(core.problems)} problem(s)"
            self.stdout.write(f"  core    apps/core/i18n/{code}.py: {'OK' if core.ok else counts}")
            for where in core.missing:
                self.stdout.write(f"    missing  {where}")
            for problem in core.problems:
                self.stdout.write(f"    problem  {problem}")
        else:
            self.stdout.write(f"  core    apps/core/i18n/{code}.py: not started (English chrome, no core pages)")
        if same:
            for where in core.same:
                self.stdout.write(f"    same as English  {where}")
        if growth_exists:
            self.stdout.write(f"  growth  apps/growth/i18n/{code}.py: {'OK' if not growth_problems else f'{len(growth_problems)} problem(s)'}")
            for problem in growth_problems:
                self.stdout.write(f"    problem  {problem}")
        else:
            self.stdout.write(f"  growth  apps/growth/i18n/{code}.py: not started (the growth pages show in English)")
        self.stdout.write(f"{code}: {'OK' if complete else 'to fix' if to_fix else 'not finished'}")
        return complete or (not to_fix and not explicit)
