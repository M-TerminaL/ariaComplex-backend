from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'aria_complex_project/404.html', status=404)
