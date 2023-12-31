# Generated by Django 4.1 on 2023-12-04 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("voting", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[
                    ("C", "Classic question"),
                    ("R", "Ranked"),
                    ("Y", "Yes/No question"),
                    ("M", "Multiple choice question"),
                    ("T", "Text question"),
                ],
                default="C",
                max_length=1,
            ),
        ),
        migrations.CreateModel(
            name="QuestionOptionRanked",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.PositiveIntegerField(blank=True, null=True)),
                ("option", models.TextField()),
                ("preference", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ranked_options",
                        to="voting.question",
                    ),
                ),
            ],
        ),
    ]
