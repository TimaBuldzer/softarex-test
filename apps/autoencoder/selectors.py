from apps.autoencoder.models import Case


def get_cases(**kwargs):
    return Case.objects.filter(**kwargs).order_by('-id')
