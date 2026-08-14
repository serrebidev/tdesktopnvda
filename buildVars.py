# Build customizations.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _


addon_info = AddonInfo(
	addon_name="telegramDesktop",
	addon_summary=_("Telegram Desktop Accessibility"),
	addon_description=_(
		"""Improves Telegram Desktop accessibility for NVDA users.

Adds Alt+1 to move focus to the chat list, Alt+M to open Telegram's main menu, Ctrl+Tab to announce the chat you switch to, and Ctrl+Enter to open the links and files a message holds. The add-on uses Telegram's stable UIA class information and leaves Telegram's native accessible names unchanged."""
	),
	addon_version="0.2.3",
	addon_changelog=_(
		"""Alt+1 and Alt+M now find Telegram's main window while one of Telegram's notification popups is in front, instead of reporting the chat list or the main menu as unavailable. The main menu, the profile button and the account switcher are announced by name instead of by Telegram's internal class path, and so is the top bar suggestion, which is read by its own wording. A control the add-on has no name for is no longer announced by that class path at all. The shortcuts keep working when another installed add-on also supplies Telegram's app module, and they are bound only while Telegram is the foreground application."""
	),
	addon_author="Ken Chang <lindsay714322@gmail.com>",
	addon_url=None,
	addon_sourceURL=None,
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2024.1.0",
	addon_lastTestedNVDAVersion="2026.1.0",
	addon_updateChannel=None,
	addon_license="GNU General Public License version 2",
	addon_licenseURL=None,
)

pythonSources: list[str] = [
	"addon/appModules/*.py",
	"addon/globalPlugins/*.py",
]
i18nSources: list[str] = pythonSources + ["buildVars.py"]
excludedFiles: list[str] = [
	"**/__pycache__/*",
	"**/*.pyc",
	"**/*.pyo",
]
baseLanguage: str = "en"
markdownExtensions: list[str] = ["tables"]
brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
