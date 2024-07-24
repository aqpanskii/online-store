from typing import Any
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from gallery.models import ContentImages
from django.db.models import Q
from .models import Content
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

class ShowContentView(ListView):
		model = Content
		template_name = 'main/main.html'
		context_object_name = 'content'
		ordering = ['-id']
		paginate_by = 8

		def get_queryset(self):
			queryset = super().get_queryset()
			search_query = self.request.GET.get('q')
			if search_query:
				queryset = queryset.filter(
				Q(title__icontains=search_query) |
				Q(material_number__icontains=search_query)
				)
			elif search_query == '':
				return queryset
			return queryset
		
		def get(self, request, *args, **kwargs):
			search_query = request.GET.get('q')
			if search_query == '':
				return redirect('home-page')
			return super().get(request, *args, **kwargs)
		
		def get_context_data(self, **kwards):
			ctx = super(ShowContentView, self).get_context_data(**kwards)
			ctx['title'] = 'Главная страница сайта'
			ctx['search_query'] = self.request.GET.get('q', '')
			return ctx


class ContentDetailView(DetailView):
	model = Content
	template_name = 'main/content_detail.html'

	def get_context_data(self, **kwards):
		ctx = super(ContentDetailView, self).get_context_data(**kwards)
		ctx['title'] = self.object.title
		ctx['images'] = ContentImages.objects.filter(content=self.object)
		return ctx

class DeleteContentView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Content
	success_url = '/'
	template_name = 'main/delete-content.html'
	permission_required = 'main.delete_content'

	def test_func(self):
		return self.request.user.has_perm('main.change_content')

class CreateContentView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	model = Content
	template_name = 'main/create_content.html'
	permission_required = 'main.add_content'
	fields = ['material_number', 'title', 'text', 'date', 'price', 'old_price']

	def get_context_data(self, **kwards):
			ctx = super(CreateContentView, self).get_context_data(**kwards)
			ctx['title'] = 'Добавление товара'
			ctx['btn_text'] = 'Добавить'
			return ctx
	
	def form_valid(self, form):
		form.instance.avtor = self.request.user
		return super().form_valid(form)

class UpdateContentView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Content
	template_name = 'main/create_content.html'
	fields = ['material_number', 'title', 'text', 'date', 'price', 'old_price']
	permission_required = 'main.change_content'

	def get_context_data(self, **kwards):
		ctx = super(UpdateContentView, self).get_context_data(**kwards)
		ctx['title'] = 'Обновление товара'
		ctx['btn_text'] = 'Обновить'
		return ctx
	
	def test_func(self):
		return self.request.user.has_perm('main.change_content')

	def form_valid(self, form):
		form.instance.avtor = self.request.user
		return super().form_valid(form)

def about(request):
		return render(request, "main/about.html")

def ar(request):
		return render(request, "main/ar.html")