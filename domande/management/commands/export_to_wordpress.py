from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from domande.models import Domanda, Materia
import csv
import os

class Command(BaseCommand):
    help = "Export data from Django site into CSV files formatted for WordPress Medness Core tables"

    def handle(self, *args, **options):
        export_dir = os.path.join(settings.BASE_DIR, 'export_wp')
        os.makedirs(export_dir, exist_ok=True)

        # Export subjects -> wp_mc_subject
        subject_path = os.path.join(export_dir, 'wp_mc_subject.csv')
        with open(subject_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'channel_id', 'name'])
            for materia in Materia.objects.all():
                writer.writerow([materia.id, 1, materia.materia])

        # Export questions -> wp_mc_questions
        question_path = os.path.join(export_dir, 'wp_mc_questions.csv')
        with open(question_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'id', 'user_id', 'question', 'student', 'category', 'professor_id',
                'degree_course_id', 'channel_id', 'subject_id', 'matched_question_id',
                'status', 'created_at'
            ])
            for domanda in Domanda.objects.all():
                writer.writerow([
                    domanda.id,
                    0,
                    domanda.domanda,
                    domanda.username,
                    'generica',
                    0,
                    0,
                    1,
                    domanda.materia_id,
                    '',
                    'approved',
                    domanda.date.strftime('%Y-%m-%d %H:%M:%S'),
                ])

        # Export users -> wp_users (basic fields only)
        users_path = os.path.join(export_dir, 'wp_users.csv')
        with open(users_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'user_login', 'user_email', 'display_name'])
            for u in User.objects.all():
                display_name = u.get_full_name() or u.username
                writer.writerow([u.id, u.username, u.email, display_name])

        self.stdout.write(self.style.SUCCESS(f'Export completed in {export_dir}'))
