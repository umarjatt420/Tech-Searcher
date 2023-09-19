from django.views import View
from .models import Blog
from .models import Comment
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class Home(View):
    @staticmethod
    def get(request):
        queryset = Blog.objects.all()
        last = Blog.objects.last()
        scnd_last_obj = Blog.objects.get(pk=len(queryset)-1)
        third_last_obj = Blog.objects.get(pk=len(queryset) - 2)
        AI_blogs = Blog.objects.filter(category='AI').last()
        CN_blogs = Blog.objects.filter(category='CN').last()
        Programming_blogs = Blog.objects.filter(category='PROGRAMMING').last()
        OS_blogs = Blog.objects.filter(category='OS').last()
        Robotics_blogs = Blog.objects.filter(category='ROBOTICS').last()
        QC_blogs = Blog.objects.filter(category='QC').last()
        DS_blogs = Blog.objects.filter(category='DS').last()
        Automation_blogs = Blog.objects.filter(category='AUTOMATION').last()
        VR_blogs = Blog.objects.filter(category='VR').last()
        IT_blogs = Blog.objects.filter(category='IT').last()
        return render(request, 'home.html', {'blogs': queryset,
                                             'last': last,
                                             'second_last': scnd_last_obj,
                                             'third_last': third_last_obj,
                                             'AI_blogs': AI_blogs,
                                             'CN_blogs': CN_blogs,
                                             'Programming_blogs': Programming_blogs,
                                             'OS_blogs': OS_blogs,
                                             'Robotics_blogs': Robotics_blogs,
                                             'QC_blogs': QC_blogs,
                                             'DS_blogs': DS_blogs,
                                             'Automation_blogs': Automation_blogs,
                                             'VR_blogs': VR_blogs,
                                             'IT_blogs': IT_blogs,
                                             })

def blog_detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = CommentForm()  # Clear the form after submission
    else:
        form = CommentForm()
    return render(request, 'blog-detail.html', {'blog': post, 'comments': comments, 'form': form})


class AI(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='AI')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'artificial-intelligence.html', {'blogs': queryset})


class IT(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='IT')
        queryset = Blog.objects.all()
        last = Blog.objects.last()
        scnd_last_obj = Blog.objects.get(pk=len(queryset)-1)
        third_last_obj = Blog.objects.get(pk=len(queryset) - 2)
        AI_blogs = Blog.objects.filter(category='AI').last()
        CN_blogs = Blog.objects.filter(category='CN').last()
        Programming_blogs = Blog.objects.filter(category='PROGRAMMING').last()
        OS_blogs = Blog.objects.filter(category='OS').last()
        Robotics_blogs = Blog.objects.filter(category='ROBOTICS').last()
        QC_blogs = Blog.objects.filter(category='QC').last()
        DS_blogs = Blog.objects.filter(category='DS').last()
        Automation_blogs = Blog.objects.filter(category='AUTOMATION').last()
        VR_blogs = Blog.objects.filter(category='VR').last()
        IT_blogs = Blog.objects.filter(category='IT').last()

        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'informationTech.html', {'blogs': queryset,
                                                        'last': last,
                                                        'second_last': scnd_last_obj,
                                                        'third_last': third_last_obj,
                                                        'AI_blogs': AI_blogs,
                                                        'CN_blogs': CN_blogs,
                                                        'Programming_blogs': Programming_blogs,
                                                        'OS_blogs': OS_blogs,
                                                        'Robotics_blogs': Robotics_blogs,
                                                        'QC_blogs': QC_blogs,
                                                        'DS_blogs': DS_blogs,
                                                        'Automation_blogs': Automation_blogs,
                                                        'VR_blogs': VR_blogs,
                                                        'IT_blogs': IT_blogs,
                                                        })


class CN(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='CN')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'computer-network.html', {'blogs': queryset})


class Programming(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='PROGRAMMING')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'programming.html', {'blogs': queryset})


class OS(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='OS')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'operating-systems.html', {'blogs': queryset})


class Robotics(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='ROBOTICS')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'robotics.html', {'blogs': queryset})


class QC(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='QC')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'quantum-computing.html', {'blogs': queryset})


class DS(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='DS')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'data-science.html', {'blogs': queryset})


class Automation(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='AUTOMATION')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'automation.html', {'blogs': queryset})


class VR(View):
    @staticmethod
    def get(request):
        query = Blog.objects.filter(category='VR')
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'virtual-reality.html', {'blogs': queryset})

class Blogs(View):
    @staticmethod
    def get(request):
        query = Blog.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(query, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, 'blogs.html', {'blogs': queryset})
class Contact(View):
    @staticmethod
    def get(request):
        return render(request, 'contact-us.html')

class About(View):
    @staticmethod
    def get(request):
        return render(request, 'about-us.html')

class Terms(View):
    @staticmethod
    def get(request):
        return render(request, 'terms&conditions.html')

class PrivacyPolicy(View):
    @staticmethod
    def get(request):
        return render(request, 'privacy-policy.html')

