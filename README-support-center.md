# SwarmForge in-app Help Center

## Files

- `protected/support.html` — searchable help center built from the supplied full article set and metrics glossary. Includes filters for General Manager, Manager, Staff, Owner, and Platform Ops, plus the SwarmForge logo in the header.
- `protected/assets/swarmforge-logo.jpg` — supplied brand image used by the Help Center.
- `server.py` — adds sign-in-protected `/support` and `/support-logo` routes.
- `protected/hotel-demo.html` — adds a Help center link to the User Profile menu.

## Access behavior

Both the Help Center and its logo use the existing login guard. Persona filters are navigation aids only; they do not change app permissions. The article set describes role visibility, approval tiers, operational workflows, billing, troubleshooting, and metric definitions.

## Apply

Copy the included files into the repository at the same paths. No additional dependencies or changes to the supplied Markdown files are required.
