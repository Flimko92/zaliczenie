# coding: utf-8
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from models import instruction, documentation

class InstructionListView(ListView):

    model = instruction

class InstructionCreateView(CreateView):

    model = instruction
    fields = [
        'name', 'duration', 'description', 'documentation'
    ]

class InstructionUpdateView(UpdateView):

    model = instruction
    fields = [
        'name', 'duration', 'description', 'documentation'
    ]

class InstructionDeleteView(DeleteView):
    model = instruction
    success_url = '/szkolenia/instruction_list'

class DocumentationCreateView(CreateView):

    model = documentation
    fields = [
        'name', 'document'
    ]

class InstructionDetailView(DetailView):

    model = instruction