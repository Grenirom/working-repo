from rest_framework import generics
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # def post(self, request, *args, **kwargs):
    #     print(request.data.get('name'))
    #     print(args, kwargs, '11111111111111111111111111111111111111111111')
    #     return super().post(request, *args, **kwargs)

class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherUpdateView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDeleteView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentListingView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

