# Export Utility for WordPress Migration

This repository contains a Django project with questions (`domande`) and user profiles.
To export data so it can be imported into the WordPress database used by the
"Medness Core" plugin, run the management command:

```bash
python manage.py export_to_wordpress
```

The command creates an `export_wp/` directory with CSV files:

- `wp_mc_subject.csv` – subjects for the `wp_mc_subject` table
- `wp_mc_questions.csv` – questions for the `wp_mc_questions` table
- `wp_users.csv` – basic user information for the `wp_users` table

These CSV files can be imported into the new WordPress database using tools
like `LOAD DATA INFILE` or a graphical MySQL client.
