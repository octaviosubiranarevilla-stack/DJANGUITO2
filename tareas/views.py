from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

#READ
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})

#CREATE
@login_required
def crear_tarea(request):
    form = TareaForm(request.POST or None)

    if form.is_valid():
        tarea = form.save(commit=False)
        tarea.usuario = request.user
        tarea.save()
        return redirect('lista_tareas')

    return render(request, 'tareas/formulario.html', {'form': form})

#UPDATE
@login_required
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    form = TareaForm(request.POST or None, instance=tarea)

    if form.is_valid():
        form.save()
        return redirect('lista_tareas')

    return render(request, 'tareas/formulario.html', {'form': form})

#DELETE
@staff_member_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('lista_tareas')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')