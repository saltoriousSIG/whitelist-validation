# Generated by Django 3.2.3 on 2021-06-08 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nftbackend', '0003_signature_signature'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='claimant',
            unique_together={('whitelist', 'address')},
        ),
        migrations.AlterUniqueTogether(
            name='signature',
            unique_together={('signer', 'whitelist')},
        ),
    ]
